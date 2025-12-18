import streamlit as st
from calculators.advanced_utilities.others.fuel_consumption import (
    FuelConsumptionInput,
    calculate_fuel_consumption,
)

def render():
    st.header("Fuel Consumption Calculation")

    distance_km = st.number_input("Distance (km)", min_value=0.0, value=100.0)
    fuel_efficiency_kmpl = st.number_input("Fuel Efficiency (km/l)", min_value=0.0, value=15.0)

    if st.button("Calculate Fuel Consumption"):
        inp = FuelConsumptionInput(distance_km=distance_km, fuel_efficiency_kmpl=fuel_efficiency_kmpl)
        fuel_consumed = calculate_fuel_consumption(inp)

        st.subheader("Results")
        st.write(f"Fuel Consumed: **{fuel_consumed:.2f} liters**")
