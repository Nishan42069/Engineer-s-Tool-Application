import streamlit as st
from calculators.conversion.unit_conversion.speed import SPEED_UNITS, SpeedInput, convert_speed

def render():
    st.header("Speed Converter")

    units = list(SPEED_UNITS.keys())

    c = st.columns(3)
    with c[0]:
        value = st.number_input("Value", value=10.0)
    with c[1]:
        from_unit = st.selectbox("From", units, index=units.index("km/h") if "km/h" in units else 0)
    with c[2]:
        to_unit = st.selectbox("To", units, index=units.index("m/s") if "m/s" in units else 0)

    if st.button("Convert"):
        try:
            out = convert_speed(SpeedInput(value=value, from_unit=from_unit, to_unit=to_unit))
            st.success(f"{value:g} {from_unit} = {out.value_out:.6g} {to_unit}")
        except Exception as e:
            st.error(str(e))
