from dataclasses import dataclass

MM_TO_M = 0.001

@dataclass
class TeeBarInput:
    depth_mm: float              # overall depth (h)
    flange_width_mm: float       # flange width (bf)
    flange_thickness_mm: float   # tf
    web_thickness_mm: float      # tw
    length_m: float
    density_kgm3: float = 7850.0

@dataclass
class TeeBarOutput:
    area_m2: float
    volume_m3: float
    weight_kg: float

def calculate_tee_bar(i: TeeBarInput) -> TeeBarOutput:
    h  = i.depth_mm * MM_TO_M
    bf = i.flange_width_mm * MM_TO_M
    tf = i.flange_thickness_mm * MM_TO_M
    tw = i.web_thickness_mm * MM_TO_M

    web_height = max(h - tf, 0.0)

    area = (bf * tf) + (tw * web_height)
    volume = area * i.length_m
    weight = volume * i.density_kgm3

    return TeeBarOutput(area_m2=area, volume_m3=volume, weight_kg=weight)
