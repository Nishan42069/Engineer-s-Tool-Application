import streamlit as st
from calculators.area.composite_shape.hollow_area_volume import (
    HollowRectangularInput,
    HollowCylindricalInput,
    calculate_hollow_rectangular,
    calculate_hollow_cylindrical,
)

UNIT_CONFIG = {
    "Metric (m)": {"to_m": 1.0, "area": "m²", "vol": "m³", "unit": "m"},
    "Imperial (ft)": {"to_m": 0.3048, "area": "ft²", "vol": "ft³", "unit": "ft"},
}


def render():
    st.header("Hollow Area & Volume Calculator")

    shape = st.selectbox("Hollow shape", ["Rectangular", "Cylindrical"])
    unit_choice = st.selectbox("Unit system", list(UNIT_CONFIG.keys()))

    cfg = UNIT_CONFIG[unit_choice]
    to_m = cfg["to_m"]
    u = cfg["unit"]
    area_u = cfg["area"]
    vol_u = cfg["vol"]

    area_factor = 1 if area_u == "m²" else 1 / (0.3048 ** 2)
    vol_factor = 1 if vol_u == "m³" else 1 / (0.3048 ** 3)

    # =========================
    # RECTANGULAR
    # =========================
    if shape == "Rectangular":
        st.subheader("Outer Dimensions")

        o = st.columns(3)
        with o[0]:
            L_o = st.number_input(f"Outer length ({u})", value=5.0)
        with o[1]:
            B_o = st.number_input(f"Outer width ({u})", value=4.0)
        with o[2]:
            H_o = st.number_input(f"Outer height ({u})", value=3.0)

        st.subheader("Inner (Hollow) Dimensions")

        i = st.columns(3)
        with i[0]:
            L_i = st.number_input(f"Inner length ({u})", value=4.0)
        with i[1]:
            B_i = st.number_input(f"Inner width ({u})", value=3.0)
        with i[2]:
            H_i = st.number_input(f"Inner height ({u})", value=3.0)

        if st.button("Calculate"):
            inp = HollowRectangularInput(
                outer_length_m=L_o * to_m,
                outer_width_m=B_o * to_m,
                outer_height_m=H_o * to_m,
                inner_length_m=L_i * to_m,
                inner_width_m=B_i * to_m,
                inner_height_m=H_i * to_m,
            )

            out = calculate_hollow_rectangular(inp)

            st.subheader("Results")
            st.metric(f"Hollow area ({area_u})", f"{out.hollow_area_m2 * area_factor:.3f}")
            st.metric(f"Hollow volume ({vol_u})", f"{out.hollow_volume_m3 * vol_factor:.3f}")

    # =========================
    # CYLINDRICAL
    # =========================
    else:
        st.subheader("Cylinder Dimensions")

        c = st.columns(3)
        with c[0]:
            d_o = st.number_input(f"Outer diameter ({u})", value=3.0)
        with c[1]:
            d_i = st.number_input(f"Inner diameter ({u})", value=2.0)
        with c[2]:
            h = st.number_input(f"Height ({u})", value=4.0)

        if st.button("Calculate"):
            inp = HollowCylindricalInput(
                outer_diameter_m=d_o * to_m,
                inner_diameter_m=d_i * to_m,
                height_m=h * to_m,
            )

            out = calculate_hollow_cylindrical(inp)

            st.subheader("Results")
            st.metric(f"Hollow area ({area_u})", f"{out.hollow_area_m2 * area_factor:.3f}")
            st.metric(f"Hollow volume ({vol_u})", f"{out.hollow_volume_m3 * vol_factor:.3f}")
