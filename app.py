import streamlit as st
import time
from backend import latest, model

st.title("🌱 Smart Irrigation Dashboard")

while True:

    if latest:

        st.subheader("📊 Live Data")

        st.write("Moisture A:", latest["mA"])
        st.write("Moisture B:", latest["mB"])
        st.write("Moisture C:", latest["mC"])

        st.write("Pump:", "ON" if latest["pump"] else "OFF")

        st.write("Valve A:", latest["vA"])
        st.write("Valve B:", latest["vB"])
        st.write("Valve C:", latest["vC"])

        # ML Prediction
        X = [[latest["mA"], latest["temp"], latest["hum"]]]
        pred = model.predict(X)

        st.subheader("🌾 Yield Prediction")
        st.write(pred[0])

        # Crop suggestion
        if latest["mA"] > 70:
            crop = "Rice"
        elif latest["mA"] > 50:
            crop = "Wheat"
        else:
            crop = "Millets"

        st.subheader("🌱 Suggested Crop")
        st.write(crop)

    time.sleep(2)
