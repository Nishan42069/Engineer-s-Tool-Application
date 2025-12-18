from dataclasses import dataclass
from typing import List


@dataclass
class BoqItemInput:
    description: str
    quantity: float
    rate: float


@dataclass
class BoqItemOutput:
    description: str
    quantity: float
    rate: float
    amount: float


@dataclass
class BoqPadOutput:
    items: List[BoqItemOutput]
    total_amount: float


def calculate_boq(items: List[BoqItemInput]) -> BoqPadOutput:
    outputs = []
    total = 0.0
    for it in items:
        amt = it.quantity * it.rate
        total += amt
        outputs.append(
            BoqItemOutput(
                description=it.description,
                quantity=it.quantity,
                rate=it.rate,
                amount=amt,
            )
        )
    return BoqPadOutput(items=outputs, total_amount=total)
