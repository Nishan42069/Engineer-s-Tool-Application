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

from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate_pdf(df, meta, subtotal, profit_amt, vat_amt, grand_total):
    out = io.BytesIO()
    doc = SimpleDocTemplate(out, pagesize=landscape(A4))
    styles = getSampleStyleSheet()

    story = [
        Paragraph("Bill of Quantities (BOQ)", styles["Title"]),
        Paragraph(f"<b>Company:</b> {meta.company_name}", styles["Normal"]),
        Paragraph(f"<b>Project:</b> {meta.project_name}", styles["Normal"]),
        Spacer(1, 10),
    ]

    clean = df[df["Description"].str.strip() != ""]
    table_data = [["S.N.", "Description", "Unit", "Qty", "Rate", "Amount", "Remarks"]]

    for _, r in clean.iterrows():
        table_data.append([
            r["S.N."],
            r["Description"],
            r["Unit"],
            f"{r['Qty']:.3f}",
            f"{r['Rate']:.3f}",
            f"{r['Amount']:.3f}",
            r["Remarks"],
        ])

    table = Table(table_data, repeatRows=1)
    table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("BACKGROUND", (0, 0), (-1, 0), colors.whitesmoke),
    ]))

    story.append(table)
    story.append(Spacer(1, 10))
    story.append(Paragraph(f"<b>Grand Total:</b> {grand_total:.3f}", styles["Heading2"]))

    doc.build(story)
    return out.getvalue()


def render():
    st.header("BOQ (Bill of Quantities)")

    # ---------------- META ----------------
    c1, c2, c3, c4 = st.columns(4)
    project = c1.text_input("Project Name")
    company = c2.text_input("Company Name")
    writer = c3.text_input("Prepared By")
    date = c4.text_input("Date")

    meta = BOQMeta(project, writer, date, company)

    # ---------------- INIT ----------------
    if "boq_df" not in st.session_state:
        st.session_state["boq_df"] = new_boq_df()
        st.session_state["finalized"] = False

    df = st.session_state["boq_df"]

    # ---------------- TABLE ----------------
    visible_cols = ["S.N.", "Description", "Unit", "Qty", "Rate", "Amount", "Remarks"]

    edited = st.data_editor(
        df[visible_cols],
        hide_index=True,
        use_container_width=True,
        column_config={
            "S.N.": st.column_config.TextColumn("S.N."),
            "Description": st.column_config.TextColumn("Description", width="large"),
            "Unit": st.column_config.SelectboxColumn("Unit", options=list_units()),
            "Qty": st.column_config.NumberColumn("Quantity", format="%.3f"),
            "Rate": st.column_config.NumberColumn("Rate per unit", format="%.3f"),
            "Amount": st.column_config.NumberColumn("Amount", disabled=True),
            "Remarks": st.column_config.TextColumn("Remarks"),
        },
    )

    df.update(edited)
    df = apply_unit_qty_rules(df)
    df = recalc_amounts(df)
    st.session_state["boq_df"] = df

    # ---------------- ADD ROWS ----------------
    if st.button("➕ Add more rows"):
        st.session_state["boq_df"] = pd.concat([df, new_boq_df(10)], ignore_index=True)
        st.rerun()

    # ---------------- TOTALS ----------------
    vat = st.number_input("VAT (%)", 0.0)
    profit = st.number_input("Contractor Profit (%)", 0.0)

    subtotal = total_amount(df)
    profit_amt = subtotal * profit / 100
    vat_amt = (subtotal + profit_amt) * vat / 100
    grand_total = subtotal + profit_amt + vat_amt

    st.metric("Grand Total", f"{grand_total:.3f}")

    # ---------------- FINALIZE ----------------
    if st.button("Finalize BOQ"):
        st.session_state["finalized"] = True

    # ---------------- EXPORT ----------------
    st.subheader("Export")

    excel = io.BytesIO()
    df[df["Description"].str.strip() != ""].to_excel(excel, index=False)
    st.download_button("Download Excel", excel.getvalue(), "BOQ.xlsx",
                       disabled=not st.session_state["finalized"])

    pdf_bytes = generate_pdf(df, meta, subtotal, profit_amt, vat_amt, grand_total)
    st.download_button("Download PDF", pdf_bytes, "BOQ.pdf",
                       disabled=not st.session_state["finalized"])

    # ---------------- SHARE ----------------
    msg = f"BOQ Summary\nProject: {project}\nGrand Total: {grand_total:.3f}"
    wa = "https://wa.me/?text=" + urllib.parse.quote(msg)
    st.link_button("Open WhatsApp Share", wa)
