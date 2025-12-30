import streamlit as st
from calculators.structural_behaviour.structure.safe_load import (
    SafeLoadInput,
    calculate_safe_load,
)

def render():
    st.title("Safe Load Calculator (Euler Buckling)")

    length_ft = st.number_input("Column length (ft)", min_value=0.0, value=10.0, step=0.5)
    diameter_ft = st.number_input("Column diameter (ft)", min_value=0.0, value=1.0, step=0.1)
    E_gpa = st.number_input("Elastic modulus E (GPa)", min_value=0.0, value=200.0, step=1.0)

    st.caption("K examples: 1.0 pinned–pinned, 0.5 fixed–fixed, 2.0 cantilever, 0.7 fixed–pinned")
    k_factor = st.number_input("Effective length factor K", min_value=0.01, value=1.0, step=0.1)

    safety_factor = st.number_input("Safety factor", min_value=0.01, value=1.5, step=0.1)

    if st.button("Calculate"):
        try:
            out = calculate_safe_load(
                SafeLoadInput(
                    length_ft=length_ft,
                    diameter_ft=diameter_ft,
                    E_gpa=E_gpa,
                    k_factor=k_factor,
                    safety_factor=safety_factor,
                )
            )

            st.success("Results")
            st.write(f"Critical buckling load (Pcr): **{out.Pcr_kN:.3f} kN**")
            st.write(f"Safe load (Psafe = Pcr / SF): **{out.Psafe_kN:.3f} kN**")
            st.write(f"Safety factor used: **{out.safety_factor:.2f}**")

        except Exception as e:
            st.error(str(e))
