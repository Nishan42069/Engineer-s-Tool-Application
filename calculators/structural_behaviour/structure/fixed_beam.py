from dataclasses import dataclass

@dataclass
class FixedBeamInput:
    length_ft: float
    load_value: float  # Load magnitude in kN

@dataclass
class FixedBeamOutput:
    reaction_a: float
    reaction_b: float
    shear_force: float
    bending_moment: float

def calculate_fixed_beam(i: FixedBeamInput) -> FixedBeamOutput:
    reaction_a = i.load_value * i.length_ft / 2
    reaction_b = reaction_a
    shear_force = reaction_a
    bending_moment = reaction_a * i.length_ft / 2

    return FixedBeamOutput(
        reaction_a=reaction_a,
        reaction_b=reaction_b,
        shear_force=shear_force,
        bending_moment=bending_moment
    )
