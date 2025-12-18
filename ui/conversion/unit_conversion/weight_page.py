import streamlit as st
from calculators.conversion.unit_conversion.mass import WEIGHT_UNITS, WeightInput, convert_weight

def render():
    st.header("Weight / Mass Converter")

    units = list(WEIGHT_UNITS.keys())

    c = st.columns(3)
    with c[0]:
        value = st.number_input("Value", value=1.0)
    with c[1]:
        from_unit = st.selectbox("From", units, index=units.index("kg"))
    with c[2]:
        to_unit = st.selectbox("To", units, index=units.index("lb") if "lb" in units else 0)

    if st.button("Convert"):
        try:
            out = convert_weight(WeightInput(value=value, from_unit=from_unit, to_unit=to_unit))
            st.success(f"{value:g} {from_unit} = {out.value_out:.6g} {to_unit}")
        except Exception as e:
            st.error(str(e))
