import streamlit as st

from calculators.measurement.perimeter.perimeter_rectangle import (
    RectanglePerimeterInput,
    calculate_rectangle_perimeter,
)
from calculators.measurement.perimeter.perimeter_circle import (
    CirclePerimeterInput,
    calculate_circle_perimeter,
)
from calculators.measurement.perimeter.perimeter_polygon import (
    PolygonPerimeterInput,
    calculate_polygon_perimeter,
)


def render():
    st.header("Perimeter Tools")

    tab1, tab2, tab3 = st.tabs(["Rectangle", "Circle", "Irregular Polygon"])

    # -------------------------
    # Rectangle
    # -------------------------
    with tab1:
        st.subheader("Rectangle Perimeter")
        cols = st.columns(2)
        with cols[0]:
            L = st.number_input("Length (ft)", min_value=0.0, value=10.0)
        with cols[1]:
            W = st.number_input("Width (ft)", min_value=0.0, value=8.0)

        if st.button("Calculate Rectangle Perimeter"):
            out = calculate_rectangle_perimeter(RectanglePerimeterInput(length_ft=L, width_ft=W))
            r = st.columns(2)
            r[0].metric("Perimeter (ft)", f"{out.perimeter_ft:.3f}")
            r[1].metric("Perimeter (m)", f"{out.perimeter_m:.3f}")

    # -------------------------
    # Circle
    # -------------------------
    with tab2:
        st.subheader("Circle Perimeter (Circumference)")
        mode = st.radio("Input mode", ["Diameter", "Radius"], horizontal=True)

        if mode == "Diameter":
            d = st.number_input("Diameter (ft)", min_value=0.0, value=10.0)
            inp = CirclePerimeterInput(diameter_ft=d, use_diameter=True)
        else:
            r = st.number_input("Radius (ft)", min_value=0.0, value=5.0)
            inp = CirclePerimeterInput(radius_ft=r, use_diameter=False)

        if st.button("Calculate Circle Perimeter"):
            out = calculate_circle_perimeter(inp)
            c = st.columns(2)
            c[0].metric("Circumference (ft)", f"{out.circumference_ft:.3f}")
            c[1].metric("Circumference (m)", f"{out.circumference_m:.3f}")

    # -------------------------
    # Polygon
    # -------------------------
    with tab3:
        st.subheader("Irregular Polygon Perimeter")
        st.caption("Enter side lengths in feet separated by commas. Example: 10, 8.5, 12, 9")

        s = st.text_input("Side lengths (ft)", value="10, 8, 12, 9")

        if st.button("Calculate Polygon Perimeter"):
            try:
                sides = [float(x.strip()) for x in s.split(",") if x.strip() != ""]
                out = calculate_polygon_perimeter(PolygonPerimeterInput(side_lengths_ft=sides))
                c = st.columns(3)
                c[0].metric("Sides", f"{out.sides_count}")
                c[1].metric("Perimeter (ft)", f"{out.perimeter_ft:.3f}")
                c[2].metric("Perimeter (m)", f"{out.perimeter_m:.3f}")
            except Exception as e:
                st.error(str(e))
