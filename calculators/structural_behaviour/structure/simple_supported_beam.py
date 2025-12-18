from dataclasses import dataclass

@dataclass
class SimpleBeamInput:
    length_ft: float
    load_value: float  # Load magnitude in kN

@dataclass
class SimpleBeamOutput:
    reaction_a: float
    reaction_b: float
    shear_force: float
    bending_moment: float

def calculate_simple_supported_beam(i: SimpleBeamInput) -> SimpleBeamOutput:
    reaction_a = i.load_value * i.length_ft / 2
    reaction_b = reaction_a
    shear_force = reaction_a
    bending_moment = reaction_a * i.length_ft / 2

    return SimpleBeamOutput(
        reaction_a=reaction_a,
        reaction_b=reaction_b,
        shear_force=shear_force,
        bending_moment=bending_moment
    )
