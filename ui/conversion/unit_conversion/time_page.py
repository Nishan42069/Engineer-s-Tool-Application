import streamlit as st
from calculators.conversion.unit_conversion.time import TIME_UNITS, TimeInput, convert_time

def render():
    st.header("Time Converter")

    units = list(TIME_UNITS.keys())

    c = st.columns(3)
    with c[0]:
        value = st.number_input("Value", value=60.0)
    with c[1]:
        from_unit = st.selectbox("From", units, index=units.index("sec"))
    with c[2]:
        to_unit = st.selectbox("To", units, index=units.index("hour") if "hour" in units else 0)

    if st.button("Convert"):
        try:
            out = convert_time(TimeInput(value=value, from_unit=from_unit, to_unit=to_unit))
            st.success(f"{value:g} {from_unit} = {out.value_out:.6g} {to_unit}")
        except Exception as e:
            st.error(str(e))
