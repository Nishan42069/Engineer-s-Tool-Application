import streamlit as st
from calculators.conversion.unit_conversion.pressure import PRESSURE_UNITS, PressureInput, convert_pressure

def render():
    st.header("Pressure Converter")

    units = list(PRESSURE_UNITS.keys())

    c = st.columns(3)
    with c[0]:
        value = st.number_input("Value", value=101.325)  # nice default (kPa-ish)
    with c[1]:
        from_unit = st.selectbox("From", units, index=units.index("kPa") if "kPa" in units else 0)
    with c[2]:
        to_unit = st.selectbox("To", units, index=units.index("MPa") if "MPa" in units else 0)

    if st.button("Convert"):
        try:
            out = convert_pressure(PressureInput(value=value, from_unit=from_unit, to_unit=to_unit))
            st.success(f"{value:g} {from_unit} = {out.value_out:.6g} {to_unit}")
        except Exception as e:
            st.error(str(e))
