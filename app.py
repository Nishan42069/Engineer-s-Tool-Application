import streamlit as st


hello shreeja 

from ui.quantity_n_material.concrete import (
    concrete_ui, circle_tank_page, concrete_wall_page, dam_body_page, 
    rectangle_tank_page, retaining_wall_page, round_column_page, round_pipe_page, slab_ui, square_column_page
)

from ui.quantity_n_material.brick import (
    brick_wall_support_page, bricks_by_volume_page, circle_wall_bricks_page, full_circle_wall_bricks_page, semi_arch_wall_bricks_page,
    three_room_bricks_page, total_room_bricks_page, two_room_bricks_page, wall_bricks_page, arch_wall_bricks_page
)

from ui.quantity_n_material.block_quantity import blockwork_page

from ui.quantity_n_material.soil_mechanics import (
    bc_circular_page, bc_continuous_page, bc_square_page, dry_unit_weight_page, modulus_elasticity_concrete_page, moisture_unit_weight_page,
    porosity_page,saturated_unit_weight_page, specific_weight_page, submerged_unit_weight_page, thermal_diffusivity_page
)

from ui.quantity_n_material.other_quantities import (
    anti_termite_page, asphalt_page, bed_excavation_page, bed_filling_page, boq_pad_page, concrete_test_page, depth_foundation_page,
    diagonal_page, floor_bricks_page, formwork_slab_page, helix_bar_page, plaster_page, rebar_straight_page, slope_filling_page,
    super_elevation_page, terrazzo_page, tiles_page, water_tank_rect_page, paint_page
)

from ui.rcc.beams import beam_4bar_page, beam_6bar_page

from ui.rcc.columns import column_10bar_page, column_4bar_page, column_6bar_page, column_8bar_page, round_column_rcc_page

from ui.rcc.slabs import one_way_slab_page, simple_slab_page, two_way_slab_page

from ui.structural_behaviour.structure import cantilever_beam, column_buckling, fixed_beam, fixed_pinned_beam, safe_load, simple_supported_beam

from ui.advanced_utilities.roof_calculation import gable_roof, hip_roof, shade_roof

from ui.advanced_utilities.hydraulics import pump_flow_rate, pump_horsepower, total_head

from ui.advanced_utilities.others import cube_test, fuel_consumption

from ui.advanced_utilities.road_drainage import box_culvert, curve_asphalt, gabion, pipe_culvert

from ui.advanced_utilities.stair_foundation import plumb_concrete, stair_geometry

from ui.metal.steel_weights import (
    angle_page, beam_bar_page, channel_page, flat_page, hex_bar_page, round_bar_page, round_pipe_page, sheet_page,
    square_bar_page, square_tubing_page, tee_bar_page
)

from ui.volume.solid_geometrys import (
    cone_page, cube_page, cylinder_page, frustum_page, half_sphere_page, parabolic_cone_page, prism_page, rectangle_tank_page,
    rectangular_prism_page, sphere_page, trapezoid_dumper_page, triangle_dumper_page
)

from ui.area.basic_shape import circle_page, ellipse_page, rectangle_page, square_page, trapezoid_page, triangle_page

from ui.area.composite_shape import shape1_page, shape2_page, shape3_page, shape4_page, shape5_page

from ui.conversion.unit_conversion import (
    angle_page, area_page, data_page, force_page, fuel_page, length_page, power_page, pressure_page, speed_page,
    temperature_page, time_page, voltage_page, volume_page, weight_page, work_page
)

from ui.measurement.land_area_converter import land_area_converter_page

from ui.measurement.perimter import perimeter_page

from ui.measurement. shuttering_area_tools import shuttering_page

from ui.boq import boq_page

MENUS = {
    "Quantity & Material": {
        "Block Quantity": {
            "Block Work": blockwork_page 
        },
        
        "Brick": {
            "Bricks by Volume": bricks_by_volume_page,
            "Wall Bricks": wall_bricks_page,
            "Circle Wall Bricks": circle_wall_bricks_page,
            "Total Room Bricks": total_room_bricks_page,
            "Arch Wall Bricks": arch_wall_bricks_page,
            "Semi Arch Wall Bricks": semi_arch_wall_bricks_page,
            "Full Circle Wall Bricks": full_circle_wall_bricks_page,
            "Two Room Bricks": two_room_bricks_page,
            "Three Room Bricks": three_room_bricks_page,
            "Brick Wall Support": brick_wall_support_page
        },
        
        "Concrete": {
            "Concrete by Volume": concrete_ui,
            "Slab Concrete": slab_ui,
            "Square Column Concrete": square_column_page,
            "Round Column Concrete": round_column_page,
            "Circle Tank Concrete": circle_tank_page,
            "Dam Body Concrete": dam_body_page,
            "Retaining Wall Concrete": retaining_wall_page,
            "Round Pipe Concrete": round_pipe_page,
            "Rectangle Tank Concrete": rectangle_tank_page,
            "Concrete Wall": concrete_wall_page
        },
        
        "Other Quantities": {
            "Super Elevation": super_elevation_page,
            "Helix Bar": helix_bar_page,
            "Plaster": plaster_page,
            "Bed Filling": bed_filling_page,
            "Bed Excavation": bed_excavation_page,
            "Paint": paint_page,
            "Slope Filling": slope_filling_page,
            "Asphalt Calculation": asphalt_page,
            "Tile Calculation": tiles_page,
            "Terrazzo/Chips": terrazzo_page,
            "Floor Bricks": floor_bricks_page,
            "Anti-Termite": anti_termite_page,
            "Reinforcement Steel Calculation": rebar_straight_page,
            "Formwork": formwork_slab_page,
            "Water Tank Calculation": water_tank_rect_page,
            "BOQ Pad": boq_pad_page,
            "Diagonal": diagonal_page,
            "Depth of Foundation": depth_foundation_page,
            "Concrete Test (Cube Test)": concrete_test_page
 
        },
        
        "Soil Mechanics": {
            "Dry Unit Weight": dry_unit_weight_page,
            "Moisture Unit Weight": modulus_elasticity_concrete_page,
            "Saturated Unit Weight": saturated_unit_weight_page,
            "Bearing Capacity (Circular)": bc_circular_page,
            "Bearing Capacity (Continuous)": bc_continuous_page,
            "Bearing Capacity (Square)": bc_square_page,
            "Modulus of Elasticity of Concrete": modulus_elasticity_concrete_page,
            "Porosity": porosity_page,
            "Specific Weight": specific_weight_page,
            "Submerged Unit Weight": submerged_unit_weight_page,
            "Thermal Diffusivity": thermal_diffusivity_page
        }
    },
    
    "RCC - Structure": {
        "Beams": {
            "4 Bar": beam_4bar_page,
            "6 Bar": beam_6bar_page
        },
        
        "Columns": {
            "4 Bar": column_4bar_page,
            "6 Bar": column_6bar_page,
            "8 Bar": column_8bar_page,
            "10 Bar": column_10bar_page,
            "Round Column": round_column_rcc_page
        },
        
        "Slabs": {
            "Simple Slab": simple_slab_page,
            "One-way Slab": one_way_slab_page,
            "Two-way Slab": two_way_slab_page
        }
    },
    
    "Structural Behaviour": {
        "Structure": {
            "Simple Supported Beam": simple_supported_beam,
            "Cantilever Beam": cantilever_beam,
            "Fixed Beam": fixed_beam,
            "Fixed-Pinned Beam": fixed_pinned_beam,
            "Column Buckling": column_buckling,
            "Safe Load": safe_load
        }
    },
    
    "Advanced Utilities": {
        "Hydraulics": {
            "Pump Flow Rate": pump_flow_rate,
            "Pump Horsepower": pump_horsepower,
            "Total Head": total_head
        },
        
        "Others": {
            "Fuel Consumption": fuel_consumption,
            "Cube Test": cube_test
        },
        
        "Road/Drainage": {
            "Curve Asphalt": curve_asphalt,
            "Gabion": gabion,
            "Box Culvert": box_culvert,
            "Pipe Culvert": pipe_culvert
        },
        
        "Roof Calculation": {
            "Shade Roof": shade_roof,
            "Gable Roof": gable_roof,
            "Hip Roof": hip_roof
        },
        
        "Stair Foundation": {
            "Stair Geometry": stair_geometry,
            "Plumb Concrete": plumb_concrete
        }
    },
    
    "Metal": {
        "Steel Weights": {
            "Round Bar": round_bar_page,
            "Square Bar": square_bar_page,
            "Round Pipe": round_pipe_page,
            "Hexagonal Bar": hex_bar_page,
            "Square Tubing": square_tubing_page,
            "Tee Bar": tee_bar_page,
            "Beam Bar": beam_bar_page,
            "Channel": channel_page,
            "Angle": angle_page,
            "Flat": flat_page,
            "Sheet": sheet_page
        }
    },
    
    "Volume": {
        "Solid Geometrys": {
            "Rectangular Prism": rectangular_prism_page,
            "Cylinder": cylinder_page,
            "Rectangle Tank": rectangle_tank_page,
            "Triangle Dumper": triangle_dumper_page,
            "Trapezoid Dumper": trapezoid_dumper_page,
            "Sphere":sphere_page,
            "Cone": cone_page,
            "Frustum": frustum_page,
            "Parabolic Cone": parabolic_cone_page,
            "Cube": cube_page,
            "Half Sphere": half_sphere_page,
            "Prism": prism_page
        }
    },
    
    "Area": {
        "Basic Shape": {
            "Circle": circle_page,
            "Ellipse": ellipse_page,
            "Rectangle": rectangle_page,
            "Square": square_page,
            "Trapezoid": trapezoid_page,
            "Triangle": triangle_page
        },
        
        "Composite Shape": {
            "Shape 1 → rectangle + extended triangle head": shape1_page,
            "Shape 2 → rectangle + half circle": shape2_page,
            "Shape 3 → rectangle + two semicircles": shape3_page,
            "Shape 4 → rectangle tapering": shape4_page,
            "Shape 5 → rectangle + triangle": shape5_page
        }
    },
    
    "Conversion": {
        "Unit Conversion": {
            "Angle": angle_page,
            "Area": area_page,
            "Data": data_page,
            "Force": force_page,
            "Fuel": fuel_page,
            "Length": length_page,
            "Power": power_page,
            "Pressure": pressure_page,
            "Speed": speed_page,
            "Temperature": temperature_page,
            "Time": time_page,
            "Voltage": voltage_page,
            "Volume": volume_page,
            "Weight/Mass": weight_page,
            "Work/Energy": work_page, 
        }
    },
    
    "Measurement Tools": {
        "Land Area Converter": {
            "Land Area Converter": land_area_converter_page
        },
        
        "Perimeter": {
            "Perimeter": perimeter_page
        },
        
        "Shuttering Area Tools": {
            "Shuttering Area": shuttering_page
        }
    }
}

TOP_PAGES = {
    "BOQ": boq_page,
}

def main():
    st.set_page_config(page_title="Engineer's Toolbox", layout="wide")

    st.sidebar.title("Engineer's Toolbox")

    # -----------------------------
    # ✅ BOQ button under title
    # -----------------------------
    if "quick_page" not in st.session_state:
        st.session_state["quick_page"] = None

    boq_clicked = st.sidebar.button("📋 BOQ", use_container_width=True)
    if boq_clicked:
        st.session_state["quick_page"] = "BOQ"

    # If BOQ (or any top page) is selected, render it and stop normal menu
    if st.session_state["quick_page"] in TOP_PAGES:
        st.caption(f"BOQ")
        TOP_PAGES[st.session_state["quick_page"]].render()

        # Optional: back button to go to normal calculators
        if st.sidebar.button("⬅ Back to Calculators", use_container_width=True):
            st.session_state["quick_page"] = None
            st.rerun()
        return

    st.sidebar.divider()


    # 1️⃣ Main menu
    main_menu = st.sidebar.selectbox(
        "Main menu",
        options=list(MENUS.keys()),
    )

    # 2️⃣ Sub menu (category)
    sub_categories = MENUS[main_menu]
    sub_menu = st.sidebar.selectbox(
        "Category",
        options=list(sub_categories.keys()),
    )

    # 3️⃣ Sub-sub menu (specific calculator)
    calculators = sub_categories[sub_menu]
    calculator_name = st.sidebar.radio(
        "Calculator",
        options=list(calculators.keys()),
    )

    # Get the selected page module
    page_module = calculators[calculator_name]

    # Optional breadcrumb at top of main area
    st.caption(f"{main_menu} › {sub_menu} › {calculator_name}")

    # Call the page's render() function
    page_module.render()


if __name__ == "__main__":
    main()
