from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Tuple
import pandas as pd

# -----------------------------
# UNIT SYSTEM
# -----------------------------
UNITS: Dict[str, Tuple[str, float]] = {
    "No.": ("count", 1.0),
    "Nos": ("count", 1.0),
    "Each": ("count", 1.0),
    "Set": ("count", 1.0),

    "m": ("length", 1.0),
    "cm": ("length", 0.01),
    "mm": ("length", 0.001),
    "ft": ("length", 0.3048),
    "in": ("length", 0.0254),

    "m²": ("area", 1.0),
    "ft²": ("area", 0.09290304),

    "m³": ("volume", 1.0),
    "ft³": ("volume", 0.028316846592),
}

DEFAULT_UNIT = "m³"


def list_units() -> list[str]:
    return list(UNITS.keys())


def unit_category(unit: str) -> str:
    return UNITS.get(unit, ("count", 1.0))[0]


def unit_factor(unit: str) -> float:
    return UNITS.get(unit, ("count", 1.0))[1]


def can_convert(u_from: str, u_to: str) -> bool:
    return unit_category(u_from) == unit_category(u_to)


# -----------------------------
# META
# -----------------------------
@dataclass
class BOQMeta:
    project_name: str
    writer_name: str
    date_str: str
    company_name: str


# -----------------------------
# DATAFRAME
# -----------------------------
def new_boq_df(n_rows: int = 40) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "S.N.": "",
                "Description": "",
                "Unit": DEFAULT_UNIT,
                "Qty": 0.0,
                "Rate": 0.0,
                "Amount": 0.0,
                "Remarks": "",
                "_QtyBase": 0.0,
                "_UnitPrev": DEFAULT_UNIT,
                "_QtyPrev": 0.0,
            }
            for _ in range(n_rows)
        ]
    )


def apply_unit_qty_rules(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for i, r in df.iterrows():
        u_now, u_prev = r["Unit"], r["_UnitPrev"]
        q_now, q_prev = float(r["Qty"]), float(r["_QtyPrev"])
        q_base = float(r["_QtyBase"])

        if u_now != u_prev and can_convert(u_prev, u_now):
            if q_base == 0 and q_prev != 0:
                q_base = q_prev * unit_factor(u_prev)
            df.at[i, "Qty"] = q_base / unit_factor(u_now)
            df.at[i, "_QtyBase"] = q_base
        elif abs(q_now - q_prev) > 1e-12:
            df.at[i, "_QtyBase"] = q_now * unit_factor(u_now)

        df.at[i, "_UnitPrev"] = u_now
        df.at[i, "_QtyPrev"] = df.at[i, "Qty"]

    return df


def recalc_amounts(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Qty"] = pd.to_numeric(df["Qty"], errors="coerce").fillna(0.0)
    df["Rate"] = pd.to_numeric(df["Rate"], errors="coerce").fillna(0.0)
    df["Amount"] = (df["Qty"] * df["Rate"]).round(3)
    return df


def total_amount(df: pd.DataFrame) -> float:
    return float(df[df["Description"].str.strip() != ""]["Amount"].sum())
