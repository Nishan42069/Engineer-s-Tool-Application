from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple
import pandas as pd


# -----------------------------
# Unit system (simple but solid)
# -----------------------------
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
# factor = how many base units in 1 unit
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
    "Rft": ("length", 0.3048),
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
        return float(value)

    base = float(value) * unit_factor(u_from)
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
    - S.N.: display only (not editable)
    - Description / Remarks: user text
    - Unit / Qty / Rate: user-facing
    - Amount: auto Qty * Rate
    - _QtyBase / _UnitPrev / _QtyPrev: internal trackers
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
                "Amount": 0.0,
                "Remarks": "",  # ✅ included in logic (order in UI handled separately)
                "_QtyBase": 0.0,
                "_UnitPrev": DEFAULT_UNIT,
                "_QtyPrev": 0.0,
            }
        )
    return pd.DataFrame(rows)


def recalc_amounts(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Qty"] = pd.to_numeric(df["Qty"], errors="coerce").fillna(0.0)
    df["Rate"] = pd.to_numeric(df["Rate"], errors="coerce").fillna(0.0)
    df["Amount"] = (df["Qty"] * df["Rate"]).round(3)
    return df


def apply_unit_qty_rules(df: pd.DataFrame) -> pd.DataFrame:
    """
    Keeps _QtyBase consistent with user edits.

    Rules:
    - If Unit changed (Unit != _UnitPrev): preserve physical quantity using _QtyBase
      and recompute displayed Qty in new unit where convertible.
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

        if unit_changed:
            if can_convert(unit_prev, unit_now) and unit_now in UNITS:
                if qty_base == 0.0 and qty_prev != 0.0:
                    qty_base = qty_prev * unit_factor(unit_prev)

                denom = unit_factor(unit_now)
                if denom != 0:
                    qty_now = qty_base / denom
                    df.at[idx, "Qty"] = qty_now
                df.at[idx, "_QtyBase"] = qty_base
            else:
                df.at[idx, "_QtyBase"] = qty_now * unit_factor(unit_now) if unit_now in UNITS else qty_now

        elif qty_changed:
            df.at[idx, "_QtyBase"] = qty_now * unit_factor(unit_now) if unit_now in UNITS else qty_now

        df.at[idx, "_UnitPrev"] = unit_now
        df.at[idx, "_QtyPrev"] = float(df.at[idx, "Qty"])

    return df


def total_amount(df: pd.DataFrame) -> float:
    if "Amount" not in df.columns:
        return 0.0
    s = pd.to_numeric(df["Amount"], errors="coerce").fillna(0.0).sum()
    return float(s)
