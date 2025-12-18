import streamlit as st
from calculators.quantity_n_material.other_quantities.formwork_slab import (
    FormworkSlabInput,
    calculate_formwork_slab,
)


def render():
    st.header("Formwork Area – Slab")

    c1, c2, c3 = st.columns(3)
    with c1:
        L = st.number_input("Slab length (m)", min_value=0.0, value=5.0)
    with c2:
        B = st.number_input("Slab width (m)", min_value=0.0, value=4.0)
    with c3:
        t = st.number_input("Slab thickness (m)", min_value=0.0, value=0.15)

    include_edges = st.checkbox("Include edge formwork", value=True)

    if st.button("Calculate formwork area"):
        inp = FormworkSlabInput(
            slab_length_m=L,
            slab_width_m=B,
            slab_thickness_m=t,
            include_edges=include_edges,
        )
        out = calculate_formwork_slab(inp)

        st.subheader("Results")
        st.write(f"Soffit area: **{out.soffit_area_m2:.2f} m²**")
        st.write(f"Edge area: **{out.edge_area_m2:.2f} m²**")
        st.success(f"Total formwork area: **{out.total_formwork_area_m2:.2f} m²**")
