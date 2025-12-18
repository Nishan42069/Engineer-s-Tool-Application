from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple, Optional
import pandas as pd


# -----------------------------
# Unit system (simple but solid)
# -----------------------------
# We keep a "base quantity" per row, so if user changes unit, we can convert
# while preserving the physical quantity.
#
# category: length / area / volume / mass / count / time / lump
# base units:
# length -> m
# area   -> m2
# volume -> m3
# mass   -> kg
# count  -> no
# time   -> hr
# lump   -> ls (lumpsum)
#
# factor is "how many base units in 1 unit".
UNITS: Dict[str, Tuple[str, float]] = {
    # COUNT / NOS
    "No.": ("count", 1.0),
    "Nos": ("count", 1.0),
    "Each": ("count", 1.0),
    "Set": ("count", 1.0),
    "Lot": ("lump", 1.0),
    "L.S.": ("lump", 1.0),
    "Item": ("count", 1.0),

    # LENGTH
    "m": ("length", 1.0),
    "cm": ("length", 0.01),
    "mm": ("length", 0.001),
    "km": ("length", 1000.0),
    "ft": ("length", 0.3048),
    "in": ("length", 0.0254),
    "Rft": ("length", 0.3048),   # running feet
    "Running ft": ("length", 0.3048),

    # AREA
    "m²": ("area", 1.0),
    "sqm": ("area", 1.0),
    "sq.m": ("area", 1.0),
    "cm²": ("area", 0.0001),
    "mm²": ("area", 0.000001),
    "ft²": ("area", 0.09290304),
    "sq.ft": ("area", 0.09290304),
    "in²": ("area", 0.00064516),
    "acre": ("area", 4046.8564224),
    "hectare": ("area", 10000.0),

    # VOLUME
    "m³": ("volume", 1.0),
    "cum": ("volume", 1.0),
    "cu.m": ("volume", 1.0),
    "ft³": ("volume", 0.028316846592),
    "cft": ("volume", 0.028316846592),
    "L": ("volume", 0.001),
    "liter": ("volume", 0.001),
    "ml": ("volume", 0.000001),
    "gal (US)": ("volume", 0.003785411784),

    # MASS
    "kg": ("mass", 1.0),
    "g": ("mass", 0.001),
    "tonne": ("mass", 1000.0),
    "lb": ("mass", 0.45359237),

    # TIME
    "hr": ("time", 1.0),
    "day": ("time", 24.0),
}


DEFAULT_UNIT = "m³"


def list_units() -> list[str]:
    return list(UNITS.keys())


def unit_category(unit: str) -> str:
    if unit not in UNITS:
        return "count"
    return UNITS[unit][0]


def unit_factor(unit: str) -> float:
    if unit not in UNITS:
        return 1.0
    return UNITS[unit][1]


def can_convert(u_from: str, u_to: str) -> bool:
    return unit_category(u_from) == unit_category(u_to)


def convert_value(value: float, u_from: str, u_to: str) -> float:
    """
    Convert value from u_from to u_to within same category using base unit.
    """
    if value is None:
        return 0.0
    if u_from == u_to:
        return float(value)
    if not can_convert(u_from, u_to):
        # different categories => do not auto convert, keep same number
        return float(value)

    # value_in_base = value * factor_from
    base = float(value) * unit_factor(u_from)
    # value_in_to = base / factor_to
    return base / unit_factor(u_to)


# -----------------------------
# BOQ row model
# -----------------------------
@dataclass
class BOQMeta:
    project_name: str
    writer_name: str
    date_str: str  # keep as string to avoid timezone issues


def new_boq_df(n_rows: int = 40) -> pd.DataFrame:
    """
    Creates a BOQ table with internal columns for unit conversion.
    - sn: display only (not editable)
    - qty: user-facing quantity in current unit
    - qty_base: internal physical quantity in base unit
    - unit: current unit
    - unit_base: the unit used as base representation per category
    """
    rows = []
    for i in range(n_rows):
        rows.append(
            {
                "S.N.": i + 1,
                "Description": "",
                "Unit": DEFAULT_UNIT,
                "Qty": 0.0,
                "Rate": 0.0,
                "Amount": 0.0,      # Qty * Rate
                "_QtyBase": 0.0,    # internal base quantity
                "_UnitPrev": DEFAULT_UNIT,  # internal for diff tracking
                "_QtyPrev": 0.0,
            }
        )
    return pd.DataFrame(rows)


def recalc_amounts(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # Make sure numeric
    df["Qty"] = pd.to_numeric(df["Qty"], errors="coerce").fillna(0.0)
    df["Rate"] = pd.to_numeric(df["Rate"], errors="coerce").fillna(0.0)
    df["Amount"] = (df["Qty"] * df["Rate"]).round(3)
    return df


def apply_unit_qty_rules(df: pd.DataFrame) -> pd.DataFrame:
    """
    Keeps _QtyBase consistent with user edits.

    Rules:
    - If Unit changed (Unit != _UnitPrev): convert displayed Qty from old unit to new unit
      while preserving _QtyBase (physical amount).
      If we have _QtyBase already, we recompute Qty from _QtyBase into new unit.
    - If Qty changed (Qty != _QtyPrev): update _QtyBase from current Qty and Unit.
    """
    df = df.copy()

    for idx, row in df.iterrows():
        unit_now = str(row.get("Unit", DEFAULT_UNIT))
        unit_prev = str(row.get("_UnitPrev", unit_now))
        qty_now = float(row.get("Qty", 0.0) or 0.0)
        qty_prev = float(row.get("_QtyPrev", qty_now) or 0.0)
        qty_base = float(row.get("_QtyBase", 0.0) or 0.0)

        unit_changed = unit_now != unit_prev
        qty_changed = abs(qty_now - qty_prev) > 1e-12

        # If unit changed: preserve physical quantity using _QtyBase
        if unit_changed:
            # If convertible category, compute Qty from base
            if can_convert(unit_prev, unit_now) and unit_now in UNITS:
                # If we never had base, derive base using previous unit & previous qty
                if qty_base == 0.0 and qty_prev != 0.0:
                    qty_base = qty_prev * unit_factor(unit_prev)

                # Convert base -> new unit
                qty_now = qty_base / unit_factor(unit_now) if unit_factor(unit_now) != 0 else qty_now
                df.at[idx, "Qty"] = qty_now
                df.at[idx, "_QtyBase"] = qty_base
            else:
                # Not convertible category: keep numeric qty as-is, reset base using new unit
                df.at[idx, "_QtyBase"] = qty_now * unit_factor(unit_now) if unit_now in UNITS else qty_now

        # If qty changed (and unit did not change or user edited after unit conversion)
        elif qty_changed:
            df.at[idx, "_QtyBase"] = qty_now * unit_factor(unit_now) if unit_now in UNITS else qty_now

        # Update prev trackers
        df.at[idx, "_UnitPrev"] = unit_now
        df.at[idx, "_QtyPrev"] = float(df.at[idx, "Qty"])

    return df


def total_amount(df: pd.DataFrame) -> float:
    if "Amount" not in df.columns:
        return 0.0
    s = pd.to_numeric(df["Amount"], errors="coerce").fillna(0.0).sum()
    return float(s)
