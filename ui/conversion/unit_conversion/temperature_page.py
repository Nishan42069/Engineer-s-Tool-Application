import streamlit as st
from calculators.conversion.unit_conversion.temperature import (
    TEMP_UNITS,
    TemperatureInput,
    convert_temperature,
)

def render():
    st.header("Temperature Converter")

    c = st.columns(3)
    with c[0]:
        value = st.number_input("Value", value=25.0)
    with c[1]:
        from_unit = st.selectbox("From", TEMP_UNITS, index=0)
    with c[2]:
        to_unit = st.selectbox("To", TEMP_UNITS, index=1)

    if st.button("Convert"):
        try:
            out = convert_temperature(TemperatureInput(value=value, from_unit=from_unit, to_unit=to_unit))
            st.success(f"{value:g}°{from_unit} = {out.value_out:.6g}°{to_unit}")
        except Exception as e:
            st.error(str(e))
