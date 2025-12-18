import streamlit as st
from calculators.conversion.unit_conversion.angle import (
    ANGLE_UNITS,
    AngleInput,
    convert_angle,
)


def render():
    st.header("Angle Converter")

    units = list(ANGLE_UNITS.keys())

    row = st.columns(3)
    with row[0]:
        value = st.number_input("Value", value=1.0)
    with row[1]:
        from_unit = st.selectbox("From", units, index=units.index("degree") if "degree" in units else 0)
    with row[2]:
        to_unit = st.selectbox("To", units, index=units.index("radian") if "radian" in units else 0)

    if st.button("Convert"):
        try:
            out = convert_angle(
                AngleInput(value=value, from_unit=from_unit, to_unit=to_unit)
            )
            st.success(f"{value:g} {from_unit} = {out.value_out:.6g} {to_unit}")
        except Exception as e:
            st.error(str(e))
