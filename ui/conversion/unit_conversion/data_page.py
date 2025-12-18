import streamlit as st
from calculators.conversion.unit_conversion.data import (
    DATA_UNITS,
    DataInput,
    convert_data,
)


def render():
    st.header("Data Converter")

    units = list(DATA_UNITS.keys())

    row = st.columns(3)
    with row[0]:
        value = st.number_input("Value", value=1024.0)
    with row[1]:
        from_unit = st.selectbox("From", units, index=units.index("byte"))
    with row[2]:
        to_unit = st.selectbox("To", units, index=units.index("MB") if "MB" in units else 0)

    if st.button("Convert"):
        try:
            out = convert_data(
                DataInput(
                    value=value,
                    from_unit=from_unit,
                    to_unit=to_unit,
                )
            )
            st.success(f"{value:g} {from_unit} = {out.value_out:.6g} {to_unit}")
        except Exception as e:
            st.error(str(e))
