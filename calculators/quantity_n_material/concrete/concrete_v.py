from dataclasses import dataclass


@dataclass
class ConcreteInput:
    volume_m3: float
    cement: int
    sand: int
    aggregate: int
    dry_factor: float = 1.54
    cement_bag_weight: float = 50.0


@dataclass
class ConcreteOutput:
    dry_volume_m3: float
    cement_bags: float
    sand_m3: float
    aggregate_m3: float


def calculate_concrete(i: ConcreteInput) -> ConcreteOutput:
    dry_volume = i.volume_m3 * i.dry_factor

    total_parts = i.cement + i.sand + i.aggregate
    if total_parts <= 0:
        raise ValueError("Mix ratio parts must be greater than zero.")

    cement_vol = dry_volume * i.cement / total_parts
    sand_vol = dry_volume * i.sand / total_parts
    agg_vol = dry_volume * i.aggregate / total_parts

    # Cement density ≈ 1440 kg/m³
    cement_kg = cement_vol * 1440
    cement_bags = cement_kg / i.cement_bag_weight

    return ConcreteOutput(
        dry_volume_m3=dry_volume,
        cement_bags=cement_bags,
        sand_m3=sand_vol,
        aggregate_m3=agg_vol,
    )
