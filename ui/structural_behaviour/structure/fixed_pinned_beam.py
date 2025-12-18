import streamlit as st
from calculators.structural_behaviour.structure.fixed_pinned_beam import (
    FixedPinnedBeamInput,
    calculate_fixed_pinned_beam,
)

def render():
    st.header("Fixed-Pinned Beam")

    length_ft = st.number_input("Beam Length (ft)", min_value=1.0, value=10.0)
    load_value = st.number_input("Load Magnitude (kN)", min_value=0.0, value=5.0)

    if st.button("Calculate Fixed-Pinned Beam"):
        inp = FixedPinnedBeamInput(length_ft=length_ft, load_value=load_value)
        out = calculate_fixed_pinned_beam(inp)

        st.subheader("Results")
        st.write(f"Reaction A: **{out.reaction_a:.2f} kN**")
        st.write(f"Reaction B: **{out.reaction_b:.2f} kN**")
        st.write(f"Shear Force: **{out.shear_force:.2f} kN**")
        st.write(f"Bending Moment: **{out.bending_moment:.2f} kN·ft**")
