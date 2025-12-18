import streamlit as st
from calculators.conversion.unit_conversion.length import LENGTH_UNITS, LengthInput, convert_length

def render():
    st.header("Length Converter")

    cols = st.columns(3)
    with cols[0]:
        value = st.number_input("Value", value=1.0)
    with cols[1]:
        from_unit = st.selectbox("From", list(LENGTH_UNITS.keys()))
    with cols[2]:
        to_unit = st.selectbox("To", list(LENGTH_UNITS.keys()))

    if st.button("Convert"):
        out = convert_length(LengthInput(value, from_unit, to_unit))
        st.success(f"{value} {from_unit} = {out:.6g} {to_unit}")
