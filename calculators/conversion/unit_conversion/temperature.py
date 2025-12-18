from dataclasses import dataclass

TEMP_UNITS = ["C", "F", "K"]

@dataclass
class TemperatureInput:
    value: float
    from_unit: str
    to_unit: str

@dataclass
class TemperatureOutput:
    value_out: float

def convert_temperature(i: TemperatureInput) -> TemperatureOutput:
    fu = i.from_unit.strip().upper()
    tu = i.to_unit.strip().upper()

    if fu not in TEMP_UNITS:
        raise ValueError(f"Unsupported temperature unit: {fu}")
    if tu not in TEMP_UNITS:
        raise ValueError(f"Unsupported temperature unit: {tu}")

    # to Celsius
    if fu == "C":
        c = i.value
    elif fu == "F":
        c = (i.value - 32.0) * 5.0 / 9.0
    else:  # K
        c = i.value - 273.15

    # from Celsius
    if tu == "C":
        out = c
    elif tu == "F":
        out = c * 9.0 / 5.0 + 32.0
    else:  # K
        out = c + 273.15

    return TemperatureOutput(value_out=out)
