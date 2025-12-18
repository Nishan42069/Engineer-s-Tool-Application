from dataclasses import dataclass
import pandas as pd

@dataclass
class PaintMaterial:
    brand_name: str
    material_name: str
    type: str
    unit: str
    price_per_unit_npr: float
    price_last_updated: str


PAINT_MATERIALS = [
    PaintMaterial(brand_name='Asian Paints', material_name='Ace Exterior Emulsion', type='Exterior Economy Emulsion', unit='1 L', price_per_unit_npr=650.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='Ace Exterior Emulsion', type='Exterior Economy Emulsion', unit='5 L', price_per_unit_npr=3020.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='Ace Exterior Emulsion', type='Exterior Economy Emulsion', unit='10 L', price_per_unit_npr=5850.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='Ace Exterior Emulsion', type='Exterior Economy Emulsion', unit='20 L', price_per_unit_npr=11180.0, price_last_updated='2025-10-26'),

    PaintMaterial(brand_name='Asian Paints', material_name='Apcolite Enamel', type='Synthetic Enamel (Solvent-based)', unit='1 L', price_per_unit_npr=950.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='Apcolite Enamel', type='Synthetic Enamel (Solvent-based)', unit='4 L', price_per_unit_npr=4420.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='Apcolite Enamel', type='Synthetic Enamel (Solvent-based)', unit='10 L', price_per_unit_npr=8550.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='Apcolite Enamel', type='Synthetic Enamel (Solvent-based)', unit='20 L', price_per_unit_npr=16340.0, price_last_updated='2025-10-26'),

    PaintMaterial(brand_name='Asian Paints', material_name='Apex Ultima', type='Exterior Premium Emulsion', unit='1 L', price_per_unit_npr=1350.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='Apex Ultima', type='Exterior Premium Emulsion', unit='4 L', price_per_unit_npr=6280.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='Apex Ultima', type='Exterior Premium Emulsion', unit='10 L', price_per_unit_npr=12150.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='Apex Ultima', type='Exterior Premium Emulsion', unit='20 L', price_per_unit_npr=23220.0, price_last_updated='2025-10-26'),

    PaintMaterial(brand_name='Asian Paints', material_name='Royale Luxury Emulsion', type='Interior Premium Emulsion (Low VOC)', unit='1 L', price_per_unit_npr=1100.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='Royale Luxury Emulsion', type='Interior Premium Emulsion (Low VOC)', unit='4 L', price_per_unit_npr=5115.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='Royale Luxury Emulsion', type='Interior Premium Emulsion (Low VOC)', unit='10 L', price_per_unit_npr=9900.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='Royale Luxury Emulsion', type='Interior Premium Emulsion (Low VOC)', unit='20 L', price_per_unit_npr=18980.0, price_last_updated='2025-10-26'),

    PaintMaterial(brand_name='Asian Paints', material_name='SmartCare Damp Proof', type='Waterproofing Coating', unit='1 L', price_per_unit_npr=850.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='SmartCare Damp Proof', type='Waterproofing Coating', unit='4 L', price_per_unit_npr=3920.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='SmartCare Damp Proof', type='Waterproofing Coating', unit='10 L', price_per_unit_npr=7650.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='SmartCare Damp Proof', type='Waterproofing Coating', unit='20 L', price_per_unit_npr=14580.0, price_last_updated='2025-10-26'),

    PaintMaterial(brand_name='Asian Paints', material_name='Tractor Emulsion', type='Interior Acrylic Emulsion', unit='1 L', price_per_unit_npr=550.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='Tractor Emulsion', type='Interior Acrylic Emulsion', unit='4 L', price_per_unit_npr=2510.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='Tractor Emulsion', type='Interior Acrylic Emulsion', unit='10 L', price_per_unit_npr=4800.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='Tractor Emulsion', type='Interior Acrylic Emulsion', unit='20 L', price_per_unit_npr=9150.0, price_last_updated='2025-10-26'),

    PaintMaterial(brand_name='Asian Paints', material_name='TruCare Exterior Wall Primer', type='Exterior Primer', unit='1 L', price_per_unit_npr=500.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='TruCare Exterior Wall Primer', type='Exterior Primer', unit='4 L', price_per_unit_npr=2280.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='TruCare Exterior Wall Primer', type='Exterior Primer', unit='10 L', price_per_unit_npr=4350.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='TruCare Exterior Wall Primer', type='Exterior Primer', unit='20 L', price_per_unit_npr=8290.0, price_last_updated='2025-10-26'),

    PaintMaterial(brand_name='Asian Paints', material_name='TruCare Interior Wall Primer', type='Interior Alkali-resisting Primer', unit='1 L', price_per_unit_npr=450.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='TruCare Interior Wall Primer', type='Interior Alkali-resisting Primer', unit='4 L', price_per_unit_npr=2030.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='TruCare Interior Wall Primer', type='Interior Alkali-resisting Primer', unit='10 L', price_per_unit_npr=3870.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='TruCare Interior Wall Primer', type='Interior Alkali-resisting Primer', unit='20 L', price_per_unit_npr=7370.0, price_last_updated='2025-10-26'),

    PaintMaterial(brand_name='Asian Paints', material_name='BP Exterior Wall Primer', type='Exterior Primer', unit='1 L', price_per_unit_npr=400.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='BP Exterior Wall Primer', type='Exterior Primer', unit='4 L', price_per_unit_npr=1820.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='BP Exterior Wall Primer', type='Exterior Primer', unit='10 L', price_per_unit_npr=3460.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='BP Exterior Wall Primer', type='Exterior Primer', unit='20 L', price_per_unit_npr=6580.0, price_last_updated='2025-10-26'),

    PaintMaterial(brand_name='Asian Paints', material_name='BP Interior Wall Primer', type='Interior Primer', unit='1 L', price_per_unit_npr=350.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='BP Interior Wall Primer', type='Interior Primer', unit='4 L', price_per_unit_npr=1580.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='BP Interior Wall Primer', type='Interior Primer', unit='10 L', price_per_unit_npr=2990.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Asian Paints', material_name='BP Interior Wall Primer', type='Interior Primer', unit='20 L', price_per_unit_npr=5680.0, price_last_updated='2025-10-26'),

    # Berger Paints
    PaintMaterial(brand_name='Berger Paints', material_name='Bison Acrylic Emulsion', type='Interior Acrylic Emulsion', unit='1 L', price_per_unit_npr=500.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='Bison Acrylic Emulsion', type='Interior Acrylic Emulsion', unit='4 L', price_per_unit_npr=2250.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='Bison Acrylic Emulsion', type='Interior Acrylic Emulsion', unit='10 L', price_per_unit_npr=4300.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='Bison Acrylic Emulsion', type='Interior Acrylic Emulsion', unit='20 L', price_per_unit_npr=8200.0, price_last_updated='2025-10-26'),

    PaintMaterial(brand_name='Berger Paints', material_name='Luxol High Gloss Enamel', type='Synthetic Enamel (Solvent-based)', unit='1 L', price_per_unit_npr=900.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='Luxol High Gloss Enamel', type='Synthetic Enamel (Solvent-based)', unit='4 L', price_per_unit_npr=4200.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='Luxol High Gloss Enamel', type='Synthetic Enamel (Solvent-based)', unit='10 L', price_per_unit_npr=8100.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='Luxol High Gloss Enamel', type='Synthetic Enamel (Solvent-based)', unit='20 L', price_per_unit_npr=15400.0, price_last_updated='2025-10-26'),

    PaintMaterial(brand_name='Berger Paints', material_name='Silk Luxury Emulsion', type='Interior Premium Emulsion (Low VOC)', unit='1 L', price_per_unit_npr=1050.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='Silk Luxury Emulsion', type='Interior Premium Emulsion (Low VOC)', unit='4 L', price_per_unit_npr=4950.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='Silk Luxury Emulsion', type='Interior Premium Emulsion (Low VOC)', unit='10 L', price_per_unit_npr=9600.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='Silk Luxury Emulsion', type='Interior Premium Emulsion (Low VOC)', unit='20 L', price_per_unit_npr=18400.0, price_last_updated='2025-10-26'),

    PaintMaterial(brand_name='Berger Paints', material_name='Walmasta', type='Exterior Economy Emulsion', unit='1 L', price_per_unit_npr=650.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='Walmasta', type='Exterior Economy Emulsion', unit='4 L', price_per_unit_npr=3000.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='Walmasta', type='Exterior Economy Emulsion', unit='10 L', price_per_unit_npr=5800.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='Walmasta', type='Exterior Economy Emulsion', unit='20 L', price_per_unit_npr=11200.0, price_last_updated='2025-10-26'),

    PaintMaterial(brand_name='Berger Paints', material_name='WeatherCoat Anti-Dust', type='Exterior Dirt-repellent Emulsion', unit='1 L', price_per_unit_npr=1250.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='WeatherCoat Anti-Dust', type='Exterior Dirt-repellent Emulsion', unit='4 L', price_per_unit_npr=5750.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='WeatherCoat Anti-Dust', type='Exterior Dirt-repellent Emulsion', unit='10 L', price_per_unit_npr=11100.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='WeatherCoat Anti-Dust', type='Exterior Dirt-repellent Emulsion', unit='20 L', price_per_unit_npr=21200.0, price_last_updated='2025-10-26'),

    PaintMaterial(brand_name='Berger Paints', material_name='WeatherCoat Long Life', type='Exterior Premium Emulsion', unit='1 L', price_per_unit_npr=1400.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='WeatherCoat Long Life', type='Exterior Premium Emulsion', unit='4 L', price_per_unit_npr=6400.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='WeatherCoat Long Life', type='Exterior Premium Emulsion', unit='10 L', price_per_unit_npr=12100.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='WeatherCoat Long Life', type='Exterior Premium Emulsion', unit='20 L', price_per_unit_npr=23200.0, price_last_updated='2025-10-26'),

    PaintMaterial(brand_name='Berger Paints', material_name='Beauty Gold Washable', type='Interior Acrylic Emulsion', unit='1 L', price_per_unit_npr=600.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='Beauty Gold Washable', type='Interior Acrylic Emulsion', unit='4 L', price_per_unit_npr=2700.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='Beauty Gold Washable', type='Interior Acrylic Emulsion', unit='10 L', price_per_unit_npr=5200.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='Beauty Gold Washable', type='Interior Acrylic Emulsion', unit='20 L', price_per_unit_npr=9900.0, price_last_updated='2025-10-26'),

    PaintMaterial(brand_name='Berger Paints', material_name='Beauty Smooth Finish', type='Interior Acrylic Emulsion', unit='1 L', price_per_unit_npr=500.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='Beauty Smooth Finish', type='Interior Acrylic Emulsion', unit='4 L', price_per_unit_npr=2300.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='Beauty Smooth Finish', type='Interior Acrylic Emulsion', unit='10 L', price_per_unit_npr=4400.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Berger Paints', material_name='Beauty Smooth Finish', type='Interior Acrylic Emulsion', unit='20 L', price_per_unit_npr=8300.0, price_last_updated='2025-10-26'),

    # Nerolac Paints
    PaintMaterial(brand_name='Nerolac Paints', material_name='Excel Total', type='Exterior Premium Emulsion', unit='1 L', price_per_unit_npr=1300.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Nerolac Paints', material_name='Excel Total', type='Exterior Premium Emulsion', unit='4 L', price_per_unit_npr=6000.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Nerolac Paints', material_name='Excel Total', type='Exterior Premium Emulsion', unit='10 L', price_per_unit_npr=11500.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Nerolac Paints', material_name='Excel Total', type='Exterior Premium Emulsion', unit='20 L', price_per_unit_npr=22000.0, price_last_updated='2025-10-26'),

    PaintMaterial(brand_name='Nerolac Paints', material_name='Beauty Gold Washable', type='Interior Acrylic Emulsion', unit='1 L', price_per_unit_npr=580.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Nerolac Paints', material_name='Beauty Gold Washable', type='Interior Acrylic Emulsion', unit='4 L', price_per_unit_npr=2650.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Nerolac Paints', material_name='Beauty Gold Washable', type='Interior Acrylic Emulsion', unit='10 L', price_per_unit_npr=5100.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Nerolac Paints', material_name='Beauty Gold Washable', type='Interior Acrylic Emulsion', unit='20 L', price_per_unit_npr=9700.0, price_last_updated='2025-10-26'),

    PaintMaterial(brand_name='Nerolac Paints', material_name='Beauty Smooth Finish', type='Interior Acrylic Emulsion', unit='1 L', price_per_unit_npr=500.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Nerolac Paints', material_name='Beauty Smooth Finish', type='Interior Acrylic Emulsion', unit='4 L', price_per_unit_npr=2300.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Nerolac Paints', material_name='Beauty Smooth Finish', type='Interior Acrylic Emulsion', unit='10 L', price_per_unit_npr=4400.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Nerolac Paints', material_name='Beauty Smooth Finish', type='Interior Acrylic Emulsion', unit='20 L', price_per_unit_npr=8300.0, price_last_updated='2025-10-26'),

    PaintMaterial(brand_name='Nerolac Paints', material_name='SurakshaPlus', type='Exterior Economy Emulsion', unit='1 L', price_per_unit_npr=620.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Nerolac Paints', material_name='SurakshaPlus', type='Exterior Economy Emulsion', unit='4 L', price_per_unit_npr=2850.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Nerolac Paints', material_name='SurakshaPlus', type='Exterior Economy Emulsion', unit='10 L', price_per_unit_npr=5500.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Nerolac Paints', material_name='SurakshaPlus', type='Exterior Economy Emulsion', unit='20 L', price_per_unit_npr=10500.0, price_last_updated='2025-10-26'),

    PaintMaterial(brand_name='Nerolac Paints', material_name='Synthetic Enamel', type='Synthetic Enamel (Solvent-based)', unit='1 L', price_per_unit_npr=880.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Nerolac Paints', material_name='Synthetic Enamel', type='Synthetic Enamel (Solvent-based)', unit='4 L', price_per_unit_npr=4090.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Nerolac Paints', material_name='Synthetic Enamel', type='Synthetic Enamel (Solvent-based)', unit='10 L', price_per_unit_npr=7920.0, price_last_updated='2025-10-26'),
    PaintMaterial(brand_name='Nerolac Paints', material_name='Synthetic Enamel', type='Synthetic Enamel (Solvent-based)', unit='20 L', price_per_unit_npr=15135.0, price_last_updated='2025-10-26'),
]


def get_paint_materials_table() -> pd.DataFrame:
    """Return materials as a pandas DataFrame (for debug or UI tables)."""
    return pd.DataFrame([m.__dict__ for m in PAINT_MATERIALS])
