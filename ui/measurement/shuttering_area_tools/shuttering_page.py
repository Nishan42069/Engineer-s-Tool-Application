import streamlit as st

from calculators.measurement.shuttering_area_tools.shuttering_slab import SlabShutteringInput, calculate_slab_shuttering
from calculators.measurement.shuttering_area_tools.shuttering_beam import BeamShutteringInput, calculate_beam_shuttering
from calculators.measurement.shuttering_area_tools.shuttering_column import ColumnShutteringInput, calculate_column_shuttering
from calculators.measurement.shuttering_area_tools.shuttering_footing import FootingShutteringInput, calculate_footing_shuttering


def render():
    st.header("Shuttering Area")

    tab1, tab2, tab3, tab4 = st.tabs(["Slab", "Beam", "Column", "Footing"])

    # -------------------------
    # Slab
    # -------------------------
    with tab1:
        st.subheader("Slab Shuttering Area")
        cols = st.columns(4)
        with cols[0]:
            L = st.number_input("Length (ft)", min_value=0.0, value=12.0, key="slab_L")
        with cols[1]:
            B = st.number_input("Width (ft)", min_value=0.0, value=10.0, key="slab_B")
        with cols[2]:
            qty = st.number_input("Quantity", min_value=1, value=1, step=1, key="slab_qty")
        with cols[3]:
            include_edges = st.checkbox("Include edges", value=False, key="slab_edges")

        t = 0.0
        if include_edges:
            t = st.number_input("Slab thickness for edge shuttering (ft)", min_value=0.0, value=0.5, key="slab_t")

        if st.button("Calculate Slab Shuttering"):
            out = calculate_slab_shuttering(
                SlabShutteringInput(
                    length_ft=L,
                    width_ft=B,
                    quantity=int(qty),
                    include_edges=include_edges,
                    thickness_ft=t,
                )
            )
            r = st.columns(2)
            r[0].metric("Area (ft²)", f"{out.area_ft2:.3f}")
            r[1].metric("Area (m²)", f"{out.area_m2:.3f}")

    # -------------------------
    # Beam
    # -------------------------
    with tab2:
        st.subheader("Beam Sides Shuttering Area")
        cols = st.columns(5)
        with cols[0]:
            L = st.number_input("Length (ft)", min_value=0.0, value=12.0, key="beam_L")
        with cols[1]:
            W = st.number_input("Width (ft)", min_value=0.0, value=1.0, key="beam_W")
        with cols[2]:
            D = st.number_input("Depth (ft)", min_value=0.0, value=1.5, key="beam_D")
        with cols[3]:
            qty = st.number_input("Quantity", min_value=1, value=1, step=1, key="beam_qty")
        with cols[4]:
            ends = st.checkbox("Include end faces", value=False, key="beam_ends")

        if st.button("Calculate Beam Shuttering"):
            out = calculate_beam_shuttering(
                BeamShutteringInput(
                    length_ft=L,
                    width_ft=W,
                    depth_ft=D,
                    quantity=int(qty),
                    include_end_faces=ends,
                )
            )
            r = st.columns(2)
            r[0].metric("Area (ft²)", f"{out.area_ft2:.3f}")
            r[1].metric("Area (m²)", f"{out.area_m2:.3f}")

    # -------------------------
    # Column
    # -------------------------
    with tab3:
        st.subheader("Column Sides Shuttering Area")
        cols = st.columns(4)
        with cols[0]:
            ctype = st.selectbox("Column type", ["Square", "Round"], key="col_type")
        with cols[1]:
            H = st.number_input("Height (ft)", min_value=0.0, value=10.0, key="col_H")
        with cols[2]:
            qty = st.number_input("Quantity", min_value=1, value=1, step=1, key="col_qty")
        with cols[3]:
            st.write("")  # spacer

        if ctype == "Square":
            dims = st.columns(2)
            with dims[0]:
                W = st.number_input("Width (ft)", min_value=0.0, value=1.0, key="col_W")
            with dims[1]:
                D = st.number_input("Depth (ft)", min_value=0.0, value=1.0, key="col_D")
            inp = ColumnShutteringInput(column_type="Square", height_ft=H, quantity=int(qty), width_ft=W, depth_ft=D)
        else:
            dia = st.number_input("Diameter (ft)", min_value=0.0, value=1.0, key="col_dia")
            inp = ColumnShutteringInput(column_type="Round", height_ft=H, quantity=int(qty), diameter_ft=dia)

        if st.button("Calculate Column Shuttering"):
            out = calculate_column_shuttering(inp)
            r = st.columns(2)
            r[0].metric("Area (ft²)", f"{out.area_ft2:.3f}")
            r[1].metric("Area (m²)", f"{out.area_m2:.3f}")

    # -------------------------
    # Footing
    # -------------------------
    with tab4:
        st.subheader("Footing Shuttering Area (Sides)")
        cols = st.columns(4)
        with cols[0]:
            ftype = st.selectbox("Footing type", ["Rectangular", "Circular"], key="foot_type")
        with cols[1]:
            t = st.number_input("Thickness/Depth (ft)", min_value=0.0, value=1.0, key="foot_t")
        with cols[2]:
            qty = st.number_input("Quantity", min_value=1, value=1, step=1, key="foot_qty")
        with cols[3]:
            st.write("")

        if ftype == "Rectangular":
            dims = st.columns(2)
            with dims[0]:
                L = st.number_input("Length (ft)", min_value=0.0, value=6.0, key="foot_L")
            with dims[1]:
                B = st.number_input("Width (ft)", min_value=0.0, value=5.0, key="foot_B")
            inp = FootingShutteringInput(
                footing_type="Rectangular",
                thickness_ft=t,
                quantity=int(qty),
                length_ft=L,
                width_ft=B,
            )
        else:
            dia = st.number_input("Diameter (ft)", min_value=0.0, value=6.0, key="foot_dia")
            inp = FootingShutteringInput(
                footing_type="Circular",
                thickness_ft=t,
                quantity=int(qty),
                diameter_ft=dia,
            )

        if st.button("Calculate Footing Shuttering"):
            out = calculate_footing_shuttering(inp)
            r = st.columns(2)
            r[0].metric("Area (ft²)", f"{out.area_ft2:.3f}")
            r[1].metric("Area (m²)", f"{out.area_m2:.3f}")
