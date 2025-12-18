from dataclasses import dataclass

@dataclass
class CantileverBeamInput:
    length_ft: float
    load_value: float  # Load magnitude in kN

@dataclass
class CantileverBeamOutput:
    reaction_a: float
    shear_force: float
    bending_moment: float

def calculate_cantilever_beam(i: CantileverBeamInput) -> CantileverBeamOutput:
    reaction_a = i.load_value * i.length_ft
    shear_force = reaction_a
    bending_moment = reaction_a * i.length_ft

    return CantileverBeamOutput(
        reaction_a=reaction_a,
        shear_force=shear_force,
        bending_moment=bending_moment
    )
