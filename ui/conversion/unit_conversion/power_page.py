import streamlit as st
from calculators.conversion.unit_conversion.power import POWER_UNITS, PowerInput, convert_power

def render():
    st.header("Power Converter")

    units = list(POWER_UNITS.keys())

    c = st.columns(3)
    with c[0]:
        value = st.number_input("Value", value=1.0)
    with c[1]:
        from_unit = st.selectbox("From", units, index=units.index("kW") if "kW" in units else 0)
    with c[2]:
        to_unit = st.selectbox("To", units, index=units.index("hp") if "hp" in units else 0)

    if st.button("Convert"):
        try:
            out = convert_power(PowerInput(value=value, from_unit=from_unit, to_unit=to_unit))
            st.success(f"{value:g} {from_unit} = {out.value_out:.6g} {to_unit}")
        except Exception as e:
            st.error(str(e))
