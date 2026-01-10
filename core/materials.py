from dataclasses import dataclass

@dataclass
class MaterialQuantity:
    quantity: float
    unit: str
    unit_cost: float = 0.0

    @property
    def total_cost(self) -> float:
        return self.quantity * self.unit_cost if self.unit_cost > 0 else 0.0
