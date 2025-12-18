from dataclasses import dataclass

MM_TO_M = 0.001

@dataclass
class ChannelInput:
    depth_mm: float        # h
    flange_width_mm: float # b
    thickness_mm: float    # t (assume uniform)
    length_m: float
    density_kgm3: float = 7850.0

@dataclass
class ChannelOutput:
    area_m2: float
    volume_m3: float
    weight_kg: float

def calculate_channel(i: ChannelInput) -> ChannelOutput:
    h = i.depth_mm * MM_TO_M
    b = i.flange_width_mm * MM_TO_M
    t = i.thickness_mm * MM_TO_M

    # area ≈ web + 2 flanges (uniform thickness)
    web_height = max(h - 2.0 * t, 0.0)
    area = (t * web_height) + 2.0 * (b * t)

    volume = area * i.length_m
    weight = volume * i.density_kgm3
    return ChannelOutput(area_m2=area, volume_m3=volume, weight_kg=weight)
