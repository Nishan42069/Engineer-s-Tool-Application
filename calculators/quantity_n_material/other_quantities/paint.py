# calculators/paint.py

import math
from dataclasses import dataclass

@dataclass
class PaintInput:
    wall_area_sqft: float
    ceiling_area_sqft: float
    include_ceiling: bool
    openings_area_sqft: float
    coverage_sqft_per_litre: float
    coats: int
    labour_rate_sqft: float
    margin_percent: float

@dataclass
class PaintOutput:
    total_area_sqft: float
    paintable_area_sqft: float
    litres_needed: float
    base_labour_cost: float
    margin_amount: float
    total_labour_cost: float

def calculate_paint(i: PaintInput) -> PaintOutput:
    # Total area
    total_area = i.wall_area_sqft + (i.ceiling_area_sqft if i.include_ceiling else 0.0)

    # Paintable area
    paintable_area = max(total_area - i.openings_area_sqft, 0.0)

    # Paint required
    if i.coverage_sqft_per_litre > 0:
        litres_needed = (paintable_area * i.coats) / i.coverage_sqft_per_litre
    else:
        litres_needed = 0.0

    # Labour cost calculations
    base_labour_cost = paintable_area * i.labour_rate_sqft
    margin_amount = base_labour_cost * (i.margin_percent / 100.0)
    total_labour_cost = base_labour_cost + margin_amount

    return PaintOutput(
        total_area_sqft=total_area,
        paintable_area_sqft=paintable_area,
        litres_needed=litres_needed,
        base_labour_cost=base_labour_cost,
        margin_amount=margin_amount,
        total_labour_cost=total_labour_cost
    )
