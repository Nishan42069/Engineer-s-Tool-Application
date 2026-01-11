# core/unit_system.py

UNIT_TO_M = {
    "Imperial (ft)": 0.3048,
    "Imperial (in)": 0.0254,
    "Metric (m)": 1.0,
    "Metric (cm)": 0.01,
    "Metric (mm)": 0.001,
}

VOLUME_FROM_M3 = {
    "Imperial (ft)": 35.3147,     # m³ → ft³
    "Imperial (in)": 61023.7,     # m³ → in³
    "Metric (m)": 1.0,
    "Metric (cm)": 1_000_000.0,   # m³ → cm³
    "Metric (mm)": 1_000_000_000.0,
}
