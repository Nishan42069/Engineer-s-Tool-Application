import streamlit as st
from calculators.quantity_n_material.other_quantities.boq_pad import (
    BoqItemInput,
    calculate_boq,
)


def render():
    st.header("BOQ Pad (Quick Estimate)")

    st.caption("Enter up to three items for a quick estimate.")

    desc1 = st.text_input("Item 1 description", "Excavation")
    q1 = st.number_input("Item 1 quantity", min_value=0.0, value=10.0, key="q1")
    r1 = st.number_input("Item 1 rate (Rs.)", min_value=0.0, value=500.0, key="r1")

    desc2 = st.text_input("Item 2 description", "PCC")
    q2 = st.number_input("Item 2 quantity", min_value=0.0, value=5.0, key="q2")
    r2 = st.number_input("Item 2 rate (Rs.)", min_value=0.0, value=6000.0, key="r2")

    desc3 = st.text_input("Item 3 description", "Brickwork")
    q3 = st.number_input("Item 3 quantity", min_value=0.0, value=8.0, key="q3")
    r3 = st.number_input("Item 3 rate (Rs.)", min_value=0.0, value=8000.0, key="r3")

    if st.button("Calculate BOQ total"):
        items = [
            BoqItemInput(desc1, q1, r1),
            BoqItemInput(desc2, q2, r2),
            BoqItemInput(desc3, q3, r3),
        ]
        out = calculate_boq(items)

        st.subheader("Items")
        for item in out.items:
            st.write(
                f"- {item.description}: {item.quantity} × {item.rate} = **Rs. {item.amount:,.2f}**"
            )

        st.subheader("Total")
        st.success(f"Grand total: **Rs. {out.total_amount:,.2f}**")
