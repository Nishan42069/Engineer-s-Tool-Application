import io
import urllib.parse
import pandas as pd
import streamlit as st

from calculators.boq.boq import (
    BOQMeta,
    list_units,
    new_boq_df,
    apply_unit_qty_rules,
    recalc_amounts,
    total_amount,
)

# Optional PDF export (ReportLab)
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


def _df_to_excel_bytes(df: pd.DataFrame, meta: BOQMeta) -> bytes:
    out = io.BytesIO()
    clean = df[["S.N.", "Description", "Unit", "Qty", "Rate", "Amount"]].copy()

    with pd.ExcelWriter(out, engine="openpyxl") as writer:
        # Meta sheet
        meta_df = pd.DataFrame(
            [
                ["Project", meta.project_name],
                ["Prepared by", meta.writer_name],
                ["Date", meta.date_str],
            ],
            columns=["Field", "Value"],
        )
        meta_df.to_excel(writer, index=False, sheet_name="Meta")
        clean.to_excel(writer, index=False, sheet_name="BOQ")

    return out.getvalue()


def _df_to_pdf_bytes(df: pd.DataFrame, meta: BOQMeta) -> bytes:
    out = io.BytesIO()
    doc = SimpleDocTemplate(out, pagesize=landscape(A4), rightMargin=18, leftMargin=18, topMargin=18, bottomMargin=18)
    styles = getSampleStyleSheet()

    story = []
    story.append(Paragraph("Bill of Quantities (BOQ)", styles["Title"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(f"<b>Project:</b> {meta.project_name}", styles["Normal"]))
    story.append(Paragraph(f"<b>Prepared by:</b> {meta.writer_name}", styles["Normal"]))
    story.append(Paragraph(f"<b>Date:</b> {meta.date_str}", styles["Normal"]))
    story.append(Spacer(1, 10))

    clean = df[["S.N.", "Description", "Unit", "Qty", "Rate", "Amount"]].copy()

    # Convert to strings for table
    data = [list(clean.columns)]
    for _, r in clean.iterrows():
        data.append([
            str(int(r["S.N."])) if str(r["S.N."]).strip() else "",
            str(r["Description"])[:120],
            str(r["Unit"]),
            f'{float(r["Qty"]):.3f}',
            f'{float(r["Rate"]):.3f}',
            f'{float(r["Amount"]):.3f}',
        ])

    tbl = Table(data, repeatRows=1, colWidths=[40, 420, 70, 80, 80, 90])
    tbl.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.6, colors.grey),
        ("BACKGROUND", (0, 0), (-1, 0), colors.whitesmoke),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 0), (0, -1), "CENTER"),
        ("ALIGN", (2, 1), (-1, -1), "RIGHT"),
    ]))
    story.append(tbl)

    story.append(Spacer(1, 10))
    story.append(Paragraph(f"<b>Total Amount:</b> {total_amount(df):,.3f}", styles["Heading2"]))

    doc.build(story)
    return out.getvalue()


def render():
    st.header("BOQ (Bill of Quantities)")

    # Page wide layout recommended in your main app:
    # st.set_page_config(layout="wide")

    # -----------------------------
    # Meta info
    # -----------------------------
    meta_cols = st.columns(3)
    with meta_cols[0]:
        project_name = st.text_input("Project / Work Name", value=st.session_state.get("boq_project", ""))
    with meta_cols[1]:
        writer_name = st.text_input("Prepared by", value=st.session_state.get("boq_writer", ""))
    with meta_cols[2]:
        date_str = st.text_input("Date", value=st.session_state.get("boq_date", ""))

    st.session_state["boq_project"] = project_name
    st.session_state["boq_writer"] = writer_name
    st.session_state["boq_date"] = date_str

    meta = BOQMeta(project_name=project_name, writer_name=writer_name, date_str=date_str)

    st.divider()

    # -----------------------------
    # Init table in session
    # -----------------------------
    if "boq_df" not in st.session_state:
        st.session_state["boq_df"] = new_boq_df(n_rows=40)
        st.session_state["boq_finalized"] = False
        st.session_state["boq_snapshot_hash"] = ""

    df: pd.DataFrame = st.session_state["boq_df"]

    # If user edited after finalize, we will auto-unfinalize
    # by comparing a simple hash of key visible columns.
    def _hash_df(d: pd.DataFrame) -> str:
        clean = d[["Description", "Unit", "Qty", "Rate"]].copy()
        return str(pd.util.hash_pandas_object(clean, index=False).sum())

    current_hash = _hash_df(df)
    if st.session_state.get("boq_finalized") and st.session_state.get("boq_snapshot_hash") != current_hash:
        st.session_state["boq_finalized"] = False

    # -----------------------------
    # Editable table (looks like BOQ grid)
    # -----------------------------
    st.subheader("BOQ Items")

    # Only allow editing these; S.N. is display-only
    units = list_units()

    edited = st.data_editor(
        df[["S.N.", "Description", "Unit", "Qty", "Rate", "Amount", "_QtyBase", "_UnitPrev", "_QtyPrev"]],
        use_container_width=True,
        hide_index=True,
        num_rows="fixed",  # keep 40 rows; you can switch to "dynamic" later
        column_config={
            "S.N.": st.column_config.NumberColumn("S.N.", disabled=True, width="small"),
            "Description": st.column_config.TextColumn("Description", width="large"),
            "Unit": st.column_config.SelectboxColumn("Unit", options=units, width="small"),
            "Qty": st.column_config.NumberColumn("Quantity", min_value=0.0, step=0.01, format="%.3f", width="small"),
            "Rate": st.column_config.NumberColumn("Rate per unit", min_value=0.0, step=0.01, format="%.3f", width="small"),
            "Amount": st.column_config.NumberColumn("Amount", disabled=True, format="%.3f", width="small"),
            "_QtyBase": st.column_config.NumberColumn("_QtyBase", disabled=True, width="small"),
            "_UnitPrev": st.column_config.TextColumn("_UnitPrev", disabled=True, width="small"),
            "_QtyPrev": st.column_config.NumberColumn("_QtyPrev", disabled=True, width="small"),
        },
    )

    # Update internal conversion tracking + amounts
    edited = apply_unit_qty_rules(edited)
    edited = recalc_amounts(edited)

    # Put back into session
    st.session_state["boq_df"] = edited

    # -----------------------------
    # Totals + finalize
    # -----------------------------
    st.divider()

    total = total_amount(edited)

    top = st.columns([2, 1])
    with top[0]:
        st.metric("Total Amount", f"{total:,.3f}")
        if st.session_state.get("boq_finalized"):
            st.success("Finalized")
        else:
            st.info("Not finalized")

    with top[1]:
        if st.button("Finalize BOQ", type="primary"):
            st.session_state["boq_finalized"] = True
            st.session_state["boq_snapshot_hash"] = _hash_df(st.session_state["boq_df"])
            st.success("BOQ finalized. If you edit anything, it will require finalizing again.")

    # -----------------------------
    # Exports
    # -----------------------------
    st.subheader("Export")

    excel_bytes = _df_to_excel_bytes(edited, meta)
    st.download_button(
        "Download Excel",
        data=excel_bytes,
        file_name="BOQ.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        disabled=not st.session_state.get("boq_finalized", False),
    )

    pdf_bytes = _df_to_pdf_bytes(edited, meta)
    st.download_button(
        "Download PDF",
        data=pdf_bytes,
        file_name="BOQ.pdf",
        mime="application/pdf",
        disabled=not st.session_state.get("boq_finalized", False),
    )

    # -----------------------------
    # WhatsApp share (message link)
    # -----------------------------
    st.subheader("Share")

    # Streamlit cannot directly send a file via WhatsApp.
    # This creates a WhatsApp message with summary. User can attach PDF manually.
    summary_lines = []
    summary_lines.append(f"BOQ Summary")
    if meta.project_name.strip():
        summary_lines.append(f"Project: {meta.project_name}")
    if meta.writer_name.strip():
        summary_lines.append(f"Prepared by: {meta.writer_name}")
    if meta.date_str.strip():
        summary_lines.append(f"Date: {meta.date_str}")
    summary_lines.append(f"Total Amount: {total:,.3f}")
    summary_lines.append("")
    summary_lines.append("Tip: Download the BOQ PDF and attach it in WhatsApp.")

    msg = "\n".join(summary_lines)
    wa_url = "https://wa.me/?text=" + urllib.parse.quote(msg)

    st.link_button(
        "Open WhatsApp Share",
        wa_url,
        disabled=not st.session_state.get("boq_finalized", False),
    )
