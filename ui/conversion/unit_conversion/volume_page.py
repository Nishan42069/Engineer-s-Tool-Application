import streamlit as st
from calculators.conversion.unit_conversion.volume import VOLUME_UNITS, VolumeInput, convert_volume

def render():
    st.header("Volume Converter")

    c = st.columns(3)
    with c[0]:
        value = st.number_input("Value", value=1.0)
    with c[1]:
        from_unit = st.selectbox("From", list(VOLUME_UNITS.keys()))
    with c[2]:
        to_unit = st.selectbox("To", list(VOLUME_UNITS.keys()), index=2 if "m³" in VOLUME_UNITS else 0)

    if st.button("Convert"):
        out = convert_volume(VolumeInput(value=value, from_unit=from_unit, to_unit=to_unit))
        st.success(f"{value:g} {from_unit} = {out:.6g} {to_unit}")
