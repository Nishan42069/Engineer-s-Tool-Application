import streamlit as st
from calculators.volume.solid_geometrys.hollow_volume import (
    HollowRectangularInput,
    HollowCylindricalInput,
    calculate_hollow_rectangular_volume,
    calculate_hollow_cylindrical_volume,
)

# -------------------------
# UNIT CONFIG
# -------------------------
UNIT_CONFIG = {
    "Metric (m)": {"to_m": 1.0, "unit": "m", "vol": "m³"},
    "Imperial (ft)": {"to_m": 0.3048, "unit": "ft", "vol": "ft³"},
}


def render():
    st.header("Hollow Space Volume Calculator")

    # -------------------------
    # GEOMETRY TYPE
    # -------------------------
    geometry_type = st.selectbox(
        "Hollow geometry type",
        ["Rectangular", "Cylindrical"],
    )

    unit_choice = st.selectbox(
        "Unit system",
        list(UNIT_CONFIG.keys()),
    )

    cfg = UNIT_CONFIG[unit_choice]
    to_m = cfg["to_m"]
    u = cfg["unit"]
    vol_u = cfg["vol"]

    # =========================
    # RECTANGULAR
    # =========================
    if geometry_type == "Rectangular":
        st.subheader("Outer Dimensions")

        o = st.columns(3)
        with o[0]:
            L_o = st.number_input(f"Outer length ({u})", min_value=0.0, value=5.0)
        with o[1]:
            B_o = st.number_input(f"Outer width ({u})", min_value=0.0, value=4.0)
        with o[2]:
            H_o = st.number_input(f"Outer height ({u})", min_value=0.0, value=3.0)

        st.subheader("Inner (Hollow) Dimensions")

        i = st.columns(3)
        with i[0]:
            L_i = st.number_input(f"Inner length ({u})", min_value=0.0, value=4.0)
        with i[1]:
            B_i = st.number_input(f"Inner width ({u})", min_value=0.0, value=3.0)
        with i[2]:
            H_i = st.number_input(f"Inner height ({u})", min_value=0.0, value=3.0)

        if st.button("Calculate Hollow Volume"):
            inp = HollowRectangularInput(
                outer_length_m=L_o * to_m,
                outer_width_m=B_o * to_m,
                outer_height_m=H_o * to_m,
                inner_length_m=L_i * to_m,
                inner_width_m=B_i * to_m,
                inner_height_m=H_i * to_m,
            )

            out = calculate_hollow_rectangular_volume(inp)

            factor = 1 if vol_u == "m³" else (1 / (0.3048**3))

            st.subheader("Results")
            st.metric(f"Outer volume ({vol_u})", f"{out.outer_volume_m3 * factor:.3f}")
            st.metric(f"Inner volume ({vol_u})", f"{out.inner_volume_m3 * factor:.3f}")
            st.metric(
                f"Hollow space volume ({vol_u})",
                f"{out.hollow_volume_m3 * factor:.3f}",
            )

    # =========================
    # CYLINDRICAL
    # =========================
    else:
        st.subheader("Cylinder Dimensions")

        c = st.columns(3)
        with c[0]:
            d_o = st.number_input(f"Outer diameter ({u})", min_value=0.0, value=3.0)
        with c[1]:
            d_i = st.number_input(f"Inner diameter ({u})", min_value=0.0, value=2.0)
        with c[2]:
            h = st.number_input(f"Height ({u})", min_value=0.0, value=4.0)

        if st.button("Calculate Hollow Volume"):
            inp = HollowCylindricalInput(
                outer_diameter_m=d_o * to_m,
                inner_diameter_m=d_i * to_m,
                height_m=h * to_m,
            )

            out = calculate_hollow_cylindrical_volume(inp)

            factor = 1 if vol_u == "m³" else (1 / (0.3048**3))

            st.subheader("Results")
            st.metric(f"Outer volume ({vol_u})", f"{out.outer_volume_m3 * factor:.3f}")
            st.metric(f"Inner volume ({vol_u})", f"{out.inner_volume_m3 * factor:.3f}")
            st.metric(
                f"Hollow space volume ({vol_u})",
                f"{out.hollow_volume_m3 * factor:.3f}",
            )
