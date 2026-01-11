FT_TO_M = 0.3048
IN_TO_M = 0.0254
CM_TO_M = 0.01
MM_TO_M = 0.001


def to_m(value: float, unit: str) -> float:
    if unit == "m":
        return value
    if unit == "mm":
        return value * MM_TO_M
    if unit == "cm":
        return value * CM_TO_M
    if unit == "in":
        return value * IN_TO_M
    if unit == "ft":
        return value * FT_TO_M
    raise ValueError("Unsupported unit")
