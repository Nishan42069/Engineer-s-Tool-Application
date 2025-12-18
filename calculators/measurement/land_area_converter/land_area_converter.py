from dataclasses import dataclass

# Base: square meter
SQFT_TO_SQM = 0.09290304
ACRE_TO_SQM = 4046.8564224
HECTARE_TO_SQM = 10000.0

# Nepal (Hilly) standard
ROPANI_TO_SQM = 508.737
ANNA_TO_SQM = ROPANI_TO_SQM / 16.0
PAISA_TO_SQM = ANNA_TO_SQM / 4.0
DAAM_TO_SQM = PAISA_TO_SQM / 4.0

# Pakistan
KANAL_TO_SQM = 505.857  # 1 kanal = 20 marla
MARLA_TO_SQM = KANAL_TO_SQM / 20.0

# India (variable by region)
DEFAULT_BIGHA_TO_SQM = 2500.0
DEFAULT_KATTHA_TO_SQM = 338.63
DEFAULT_DHUR_TO_SQM = DEFAULT_KATTHA_TO_SQM / 20.0


# Display labels used in UI (recommended)
LAND_AREA_UNITS = [
    # Nepal
    "Ropani", "Anna", "Paisa", "Daam",
    # India
    "Bigha", "Kattha", "Dhur",
    # Pakistan
    "Kanal", "Marla",
    # International
    "Sq.m", "Sq.ft", "Acre", "Hectare",
]


def _norm_unit(u: str) -> str:
    """
    Normalize unit strings so UI labels and user-typed variants both work.
    Returns canonical lowercase tokens: ropani, anna, ..., sqm, sqft, acre, hectare
    """
    x = u.strip().lower()

    # allow common variants
    x = x.replace(" ", "")
    x = x.replace(".", "")

    if x in ("sqm", "m2", "sqmeter", "sqmetre", "squaremeter", "squaremetre"):
        return "sqm"
    if x in ("sqft", "ft2", "sqfeet", "squarefeet", "squarefoot"):
        return "sqft"

    # map UI labels too
    if x == "sqm":  # already
        return "sqm"
    if x == "sqft":  # already
        return "sqft"

    return x  # ropani, bigha, acre, hectare, etc.


@dataclass
class LandAreaInput:
    value: float
    from_unit: str
    to_unit: str

    # India customization
    bigha_to_sqm: float = DEFAULT_BIGHA_TO_SQM
    kattha_to_sqm: float = DEFAULT_KATTHA_TO_SQM
    dhur_to_sqm: float = DEFAULT_DHUR_TO_SQM


@dataclass
class LandAreaOutput:
    value_out: float
    sqm: float


def _to_sqm(value: float, unit: str, i: LandAreaInput) -> float:
    u = _norm_unit(unit)

    # Nepal
    if u == "ropani":
        return value * ROPANI_TO_SQM
    if u == "anna":
        return value * ANNA_TO_SQM
    if u == "paisa":
        return value * PAISA_TO_SQM
    if u == "daam":
        return value * DAAM_TO_SQM

    # India
    if u == "bigha":
        return value * i.bigha_to_sqm
    if u == "kattha":
        return value * i.kattha_to_sqm
    if u == "dhur":
        return value * i.dhur_to_sqm

    # Pakistan
    if u == "kanal":
        return value * KANAL_TO_SQM
    if u == "marla":
        return value * MARLA_TO_SQM

    # International
    if u == "sqm":
        return value
    if u == "sqft":
        return value * SQFT_TO_SQM
    if u == "acre":
        return value * ACRE_TO_SQM
    if u == "hectare":
        return value * HECTARE_TO_SQM

    raise ValueError(f"Unknown unit: {unit}")


def _from_sqm(sqm: float, unit: str, i: LandAreaInput) -> float:
    u = _norm_unit(unit)

    # Nepal
    if u == "ropani":
        return sqm / ROPANI_TO_SQM
    if u == "anna":
        return sqm / ANNA_TO_SQM
    if u == "paisa":
        return sqm / PAISA_TO_SQM
    if u == "daam":
        return sqm / DAAM_TO_SQM

    # India
    if u == "bigha":
        return sqm / i.bigha_to_sqm
    if u == "kattha":
        return sqm / i.kattha_to_sqm
    if u == "dhur":
        return sqm / i.dhur_to_sqm

    # Pakistan
    if u == "kanal":
        return sqm / KANAL_TO_SQM
    if u == "marla":
        return sqm / MARLA_TO_SQM

    # International
    if u == "sqm":
        return sqm
    if u == "sqft":
        return sqm / SQFT_TO_SQM
    if u == "acre":
        return sqm / ACRE_TO_SQM
    if u == "hectare":
        return sqm / HECTARE_TO_SQM

    raise ValueError(f"Unknown unit: {unit}")


def convert_land_area(i: LandAreaInput) -> LandAreaOutput:
    if i.value < 0:
        raise ValueError("Value must be non-negative.")

    # sanity checks for India settings
    if i.bigha_to_sqm <= 0 or i.kattha_to_sqm <= 0 or i.dhur_to_sqm <= 0:
        raise ValueError("India unit settings must be positive numbers.")

    sqm = _to_sqm(i.value, i.from_unit, i)
    out = _from_sqm(sqm, i.to_unit, i)
    return LandAreaOutput(value_out=float(out), sqm=float(sqm))
