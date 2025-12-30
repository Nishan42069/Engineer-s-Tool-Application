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


def _df_to_excel_bytes(
    df: pd.DataFrame,
    meta: BOQMeta,
    vat_pct: float,
    profit_pct: float,
    subtotal: float,
    profit_amt: float,
    vat_amt: float,
    grand_total: float,
) -> bytes:
    out = io.BytesIO()
    clean = df[["S.N.", "Description", "Unit", "Qty", "Rate", "Amount"]].copy()

    with pd.ExcelWriter(out, engine="openpyxl") as writer:
        meta_df = pd.DataFrame(
            [
                ["Project", meta.project_name],
                ["Prepared by", meta.writer_name],
                ["Date", meta.date_str],
                ["", ""],
                ["Subtotal", round(subtotal, 3)],
                ["Contractor Profit (%)", float(profit_pct)],
                ["Contractor Profit Amount", round(profit_amt, 3)],
                ["VAT (%)", float(vat_pct)],
                ["VAT Amount", round(vat_amt, 3)],
                ["Grand Total", round(grand_total, 3)],
            ],
            columns=["Field", "Value"],
        )
        meta_df.to_excel(writer, index=False, sheet_name="Meta")
        clean.to_excel(writer, index=False, sheet_name="BOQ")

    return out.getvalue()


def _df_to_pdf_bytes(
    df: pd.DataFrame,
    meta: BOQMeta,
    vat_pct: float,
    profit_pct: float,
    subtotal: float,
    profit_amt: float,
    vat_amt: float,
    grand_total: float,
) -> bytes:
    out = io.BytesIO()
    doc = SimpleDocTemplate(
        out,
        pagesize=landscape(A4),
        rightMargin=18,
        leftMargin=18,
        topMargin=18,
        bottomMargin=18,
    )
    styles = getSampleStyleSheet()

    story = []
    story.append(Paragraph("Bill of Quantities (BOQ)", styles["Title"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(f"<b>Project:</b> {meta.project_name}", styles["Normal"]))
    story.append(Paragraph(f"<b>Prepared by:</b> {meta.writer_name}", styles["Normal"]))
    story.append(Paragraph(f"<b>Date:</b> {meta.date_str}", styles["Normal"]))
    story.append(Spacer(1, 10))

    clean = df[["S.N.", "Description", "Unit", "Qty", "Rate", "Amount"]].copy()

    data = [list(clean.columns)]
    for _, r in clean.iterrows():
        data.append(
            [
                str(int(r["S.N."])) if str(r["S.N."]).strip() else "",
                str(r["Description"])[:120],
                str(r["Unit"]),
                f'{float(r["Qty"]):.3f}',
                f'{float(r["Rate"]):.3f}',
                f'{float(r["Amount"]):.3f}',
            ]
        )

    tbl = Table(data, repeatRows=1, colWidths=[40, 420, 70, 80, 80, 90])
    tbl.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.6, colors.grey),
                ("BACKGROUND", (0, 0), (-1, 0), colors.whitesmoke),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (0, 0), (0, -1), "CENTER"),
                ("ALIGN", (2, 1), (-1, -1), "RIGHT"),
            ]
        )
    )
    story.append(tbl)

    story.append(Spacer(1, 12))
    story.append(Paragraph(f"<b>Subtotal:</b> {subtotal:,.3f}", styles["Heading3"]))
    story.append(Paragraph(f"<b>Contractor Profit ({profit_pct:.2f}%):</b> {profit_amt:,.3f}", styles["Heading3"]))
    story.append(Paragraph(f"<b>VAT ({vat_pct:.2f}%):</b> {vat_amt:,.3f}", styles["Heading3"]))
    story.append(Paragraph(f"<b>Grand Total:</b> {grand_total:,.3f}", styles["Heading2"]))

    doc.build(story)
    return out.getvalue()


def render():
    st.header("BOQ (Bill of Quantities)")

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
        st.session_state["boq_last_calc_hash"] = ""

    # Defaults for contractor fields
    if "boq_vat_pct" not in st.session_state:
        st.session_state["boq_vat_pct"] = 0.0
    if "boq_profit_pct" not in st.session_state:
        st.session_state["boq_profit_pct"] = 0.0

    df: pd.DataFrame = st.session_state["boq_df"]

    # Hash only what the user can edit
    def _hash_editable(d: pd.DataFrame, vat_pct: float, profit_pct: float) -> str:
        clean = d[["Description", "Unit", "Qty", "Rate"]].copy()
        base = str(pd.util.hash_pandas_object(clean, index=False).sum())
        return base + f"|vat={float(vat_pct):.6f}|profit={float(profit_pct):.6f}"

    # Hash full calc outputs (to detect when Amount/internal changes)
    def _hash_calc(d: pd.DataFrame) -> str:
        clean = d[["Description", "Unit", "Qty", "Rate", "Amount", "_QtyBase", "_UnitPrev", "_QtyPrev"]].copy()
        return str(pd.util.hash_pandas_object(clean, index=False).sum())

    # -----------------------------
    # Editable table
    # -----------------------------
    st.subheader("BOQ Items")

    units = list_units()
    visible_cols = ["S.N.", "Description", "Unit", "Qty", "Rate", "Amount"]
    editor_df = df[visible_cols].copy()

    edited_visible = st.data_editor(
        editor_df,
        key="boq_editor",
        use_container_width=True,
        hide_index=True,
        num_rows="fixed",
        column_config={
            "S.N.": st.column_config.NumberColumn("S.N.", disabled=True, width="small"),
            "Description": st.column_config.TextColumn("Description", width="large"),
            "Unit": st.column_config.SelectboxColumn("Unit", options=units, width="small"),
            "Qty": st.column_config.NumberColumn("Quantity", min_value=0.0, step=0.01, format="%.3f", width="small"),
            "Rate": st.column_config.NumberColumn("Rate per unit", min_value=0.0, step=0.01, format="%.3f", width="small"),
            "Amount": st.column_config.NumberColumn("Amount", disabled=True, format="%.3f", width="small"),
        },
    )

    # Merge edited visible columns back into full df
    working = df.copy()
    for col in ["Description", "Unit", "Qty", "Rate"]:
        working[col] = edited_visible[col]

    working = apply_unit_qty_rules(working)
    working = recalc_amounts(working)

    # Save df
    st.session_state["boq_df"] = working

    # Force a rerun once when calc outputs changed (amount updates)
    calc_hash = _hash_calc(working)
    if st.session_state.get("boq_last_calc_hash") != calc_hash:
        st.session_state["boq_last_calc_hash"] = calc_hash
        st.rerun()

    # -----------------------------
    # Contractor inputs (AFTER table, BEFORE finalize button)
    # -----------------------------
    st.divider()
    st.subheader("Contractor Add-ons")

    c1, c2 = st.columns(2)
    with c1:
        vat_pct = st.number_input(
            "VAT (%)",
            min_value=0.0,
            step=0.1,
            value=float(st.session_state.get("boq_vat_pct", 0.0)),
        )
    with c2:
        profit_pct = st.number_input(
            "Contractor Profit / Margin (%)",
            min_value=0.0,
            step=0.1,
            value=float(st.session_state.get("boq_profit_pct", 0.0)),
        )

    st.session_state["boq_vat_pct"] = float(vat_pct)
    st.session_state["boq_profit_pct"] = float(profit_pct)

    # Totals
    subtotal = total_amount(working)
    profit_amt = subtotal * (float(profit_pct) / 100.0)
    vat_base = subtotal + profit_amt
    vat_amt = vat_base * (float(vat_pct) / 100.0)
    grand_total = vat_base + vat_amt

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Subtotal", f"{subtotal:,.3f}")
    m2.metric("Profit Amount", f"{profit_amt:,.3f}")
    m3.metric("VAT Amount", f"{vat_amt:,.3f}")
    m4.metric("Grand Total", f"{grand_total:,.3f}")

    # -----------------------------
    # Auto-unfinalize if anything editable changed (df or vat/profit)
    # -----------------------------
    editable_hash = _hash_editable(working, vat_pct, profit_pct)
    if st.session_state.get("boq_finalized") and st.session_state.get("boq_snapshot_hash") != editable_hash:
        st.session_state["boq_finalized"] = False

    # -----------------------------
    # Finalize (button is AFTER inputs)
    # -----------------------------
    st.divider()

    top = st.columns([2, 1])
    with top[0]:
        if st.session_state.get("boq_finalized"):
            st.success("Finalized")
        else:
            st.info("Not finalized")

    with top[1]:
        if st.button("Finalize BOQ", type="primary"):
            st.session_state["boq_finalized"] = True
            st.session_state["boq_snapshot_hash"] = editable_hash
            st.rerun()

    # -----------------------------
    # Exports
    # -----------------------------
    st.subheader("Export")

    excel_bytes = _df_to_excel_bytes(
        working, meta,
        vat_pct=float(vat_pct),
        profit_pct=float(profit_pct),
        subtotal=float(subtotal),
        profit_amt=float(profit_amt),
        vat_amt=float(vat_amt),
        grand_total=float(grand_total),
    )
    st.download_button(
        "Download Excel",
        data=excel_bytes,
        file_name="BOQ.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        disabled=not st.session_state.get("boq_finalized", False),
    )

    pdf_bytes = _df_to_pdf_bytes(
        working, meta,
        vat_pct=float(vat_pct),
        profit_pct=float(profit_pct),
        subtotal=float(subtotal),
        profit_amt=float(profit_amt),
        vat_amt=float(vat_amt),
        grand_total=float(grand_total),
    )
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

    summary_lines = [
        "BOQ Summary",
        f"Project: {meta.project_name}" if meta.project_name.strip() else "",
        f"Prepared by: {meta.writer_name}" if meta.writer_name.strip() else "",
        f"Date: {meta.date_str}" if meta.date_str.strip() else "",
        f"Subtotal: {subtotal:,.3f}",
        f"Profit ({float(profit_pct):.2f}%): {profit_amt:,.3f}",
        f"VAT ({float(vat_pct):.2f}%): {vat_amt:,.3f}",
        f"Grand Total: {grand_total:,.3f}",
        "",
        "Tip: Download the BOQ PDF and attach it in WhatsApp.",
    ]
    summary_lines = [x for x in summary_lines if x != ""]

    msg = "\n".join(summary_lines)
    wa_url = "https://wa.me/?text=" + urllib.parse.quote(msg)

    st.link_button(
        "Open WhatsApp Share",
        wa_url,
        disabled=not st.session_state.get("boq_finalized", False),
    )
