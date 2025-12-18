from dataclasses import dataclass

@dataclass
class FuelConsumptionInput:
    distance_km: float
    fuel_efficiency_kmpl: float

def calculate_fuel_consumption(i: FuelConsumptionInput) -> float:
    # Fuel consumption = distance / fuel efficiency
    fuel_consumed = i.distance_km / i.fuel_efficiency_kmpl
    return fuel_consumed
