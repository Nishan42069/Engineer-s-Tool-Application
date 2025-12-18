import streamlit as st
from calculators.measurement.land_area_converter.land_area_converter import (
    LAND_AREA_UNITS,
    LandAreaInput,
    convert_land_area,
)

def render():
    st.header("Land Area Converter (Nepal, India, Pakistan, International)")

    st.subheader("Input")

    cols = st.columns(3)
    with cols[0]:
        value = st.number_input("Value", min_value=0.0, value=1.0)
    with cols[1]:
        from_unit = st.selectbox("From", LAND_AREA_UNITS, index=0)  # Ropani
    with cols[2]:
        # choose Sq.ft by default if it exists
        default_to = LAND_AREA_UNITS.index("Sq.ft") if "Sq.ft" in LAND_AREA_UNITS else 0
        to_unit = st.selectbox("To", LAND_AREA_UNITS, index=default_to)

    st.subheader("India Unit Settings (Optional)")
    st.caption("Bigha/Kattha/Dhur sizes vary by region. Adjust if needed.")

    c2 = st.columns(3)
    with c2[0]:
        bigha_to_sqm = st.number_input("1 Bigha = (sq.m)", min_value=1.0, value=2500.0)
    with c2[1]:
        kattha_to_sqm = st.number_input("1 Kattha = (sq.m)", min_value=1.0, value=338.63)
    with c2[2]:
        # default dhur based on common assumption
        dhur_to_sqm = st.number_input("1 Dhur = (sq.m)", min_value=0.0001, value=16.9315)

    if st.button("Convert"):
        try:
            inp = LandAreaInput(
                value=value,
                from_unit=from_unit,
                to_unit=to_unit,
                bigha_to_sqm=bigha_to_sqm,
                kattha_to_sqm=kattha_to_sqm,
                dhur_to_sqm=dhur_to_sqm,
            )
            out = convert_land_area(inp)

            r = st.columns(2)
            r[0].metric(f"Output ({to_unit})", f"{out.value_out:.6f}")
            r[1].metric("Square meters (sq.m)", f"{out.sqm:.6f}")

        except Exception as e:
            st.error(str(e))
