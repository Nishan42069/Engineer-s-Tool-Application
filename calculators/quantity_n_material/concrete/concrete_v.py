# calculators/concrete.py

from dataclasses import dataclass

@dataclass
class ConcreteInput:
    volume_m3: float
    cement: int       # part
    sand: int         # part
    aggregate: int    # part
    dry_factor: float = 1.54
    cement_bag_weight: float = 50.0

@dataclass
class ConcreteOutput:
    dry_volume: float
    cement_bags: float
    sand_m3: float
    aggregate_m3: float

def calculate_concrete(i: ConcreteInput) -> ConcreteOutput:
    dry_volume = i.volume_m3 * i.dry_factor
    total_parts = i.cement + i.sand + i.aggregate

    cement_vol = dry_volume * i.cement / total_parts
    sand_vol   = dry_volume * i.sand / total_parts
    agg_vol    = dry_volume * i.aggregate / total_parts

    # approximate density 1440 kg/m3
    cement_kg = cement_vol * 1440
    cement_bags = cement_kg / i.cement_bag_weight

    return ConcreteOutput(
        dry_volume=dry_volume,
        cement_bags=cement_bags,
        sand_m3=sand_vol,
        aggregate_m3=agg_vol,
    )
