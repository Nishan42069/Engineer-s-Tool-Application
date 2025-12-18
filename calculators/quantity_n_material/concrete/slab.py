# calculators/concrete/slab.py

from dataclasses import dataclass

# 1 ft² = 0.092903 m², 1 ft = 0.3048 m
SQFT_TO_SQM = 0.092903
FT_TO_M = 0.3048


@dataclass
class SlabInput:
    area_sqft: float
    thickness_ft: float
    cement_part: int
    sand_part: int
    aggregate_part: int
    density_kgm3: float = 2400.0       # typical concrete density
    cost_per_m3: float = 0.0           # Rs/m³ (optional)


@dataclass
class SlabOutput:
    volume_m3: float
    cement_weight_kg: float
    sand_weight_kg: float
    aggregate_weight_kg: float
    total_cost: float


def calculate_slab_concrete(i: SlabInput) -> SlabOutput:
    # Convert to metric
    area_m2 = i.area_sqft * SQFT_TO_SQM
    thickness_m = i.thickness_ft * FT_TO_M

    # Slab volume in m³
    volume_m3 = area_m2 * thickness_m

    total_parts = i.cement_part + i.sand_part + i.aggregate_part
    if total_parts <= 0:
        raise ValueError("Mix ratio parts must be greater than zero.")

    cement_vol = volume_m3 * i.cement_part / total_parts
    sand_vol = volume_m3 * i.sand_part / total_parts
    agg_vol = volume_m3 * i.aggregate_part / total_parts

    cement_weight_kg = cement_vol * i.density_kgm3
    sand_weight_kg = sand_vol * i.density_kgm3
    aggregate_weight_kg = agg_vol * i.density_kgm3

    total_cost = volume_m3 * i.cost_per_m3 if i.cost_per_m3 > 0 else 0.0

    return SlabOutput(
        volume_m3=volume_m3,
        cement_weight_kg=cement_weight_kg,
        sand_weight_kg=sand_weight_kg,
        aggregate_weight_kg=aggregate_weight_kg,
        total_cost=total_cost,
    )
