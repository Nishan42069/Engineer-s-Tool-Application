import streamlit as st
from calculators.conversion.unit_conversion.energy import WORK_UNITS, WorkInput, convert_work

def render():
    st.header("Work / Energy Converter")

    units = list(WORK_UNITS.keys())

    c = st.columns(3)
    with c[0]:
        value = st.number_input("Value", value=1.0)
    with c[1]:
        from_unit = st.selectbox("From", units, index=units.index("J"))
    with c[2]:
        to_unit = st.selectbox("To", units, index=units.index("kWh") if "kWh" in units else 0)

    if st.button("Convert"):
        try:
            out = convert_work(WorkInput(value=value, from_unit=from_unit, to_unit=to_unit))
            st.success(f"{value:g} {from_unit} = {out.value_out:.6g} {to_unit}")
        except Exception as e:
            st.error(str(e))
