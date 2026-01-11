from dataclasses import dataclass

@dataclass
class BlockSize:
    """
    Block size INCLUDING mortar joint.
    All dimensions are stored internally in meters.
    """
    length_m: float
    height_m: float
    thickness_m: float

    @property
    def volume_m3(self) -> float:
        return self.length_m * self.height_m * self.thickness_m
