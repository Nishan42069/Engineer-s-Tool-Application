from dataclasses import dataclass

@dataclass
class FixedPinnedBeamInput:
    length_ft: float
    load_value: float  # Load magnitude in kN

@dataclass
class FixedPinnedBeamOutput:
    reaction_a: float
    reaction_b: float
    shear_force: float
    bending_moment: float

def calculate_fixed_pinned_beam(i: FixedPinnedBeamInput) -> FixedPinnedBeamOutput:
    reaction_a = i.load_value * i.length_ft / 3
    reaction_b = reaction_a * 2
    shear_force = reaction_a
    bending_moment = reaction_a * i.length_ft / 3

    return FixedPinnedBeamOutput(
        reaction_a=reaction_a,
        reaction_b=reaction_b,
        shear_force=shear_force,
        bending_moment=bending_moment
    )
