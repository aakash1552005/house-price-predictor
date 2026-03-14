import streamlit as st
import joblib
import numpy as np
import os
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

@st.cache_resource
def load_model():
    if os.path.exists("rf_model.pkl"):
        model = joblib.load("rf_model.pkl")
        feature_names = joblib.load("feature_names.pkl")
    else:
        with st.spinner("Training model for first time... (30 seconds)"):
            housing = fetch_california_housing()
            X = housing.data
            y = housing.target
            feature_names = list(housing.feature_names)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            model = RandomForestRegressor(
                n_estimators=100,
                random_state=42,
                n_jobs=-1
            )
            model.fit(X_train, y_train)
            joblib.dump(model, "rf_model.pkl")
            joblib.dump(feature_names, "feature_names.pkl")
    return model, feature_names

model, feature_names = load_model()

st.title("House Price Predictor")
st.write("Enter the details below to predict the house price!")
st.write("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Area Details")
    MedInc = st.slider(
        "Median Income (in $10,000s)",
        min_value=0.5,
        max_value=15.0,
        value=3.0,
        step=0.1
    )
    HouseAge = st.slider(
        "House Age (years)",
        min_value=1,
        max_value=52,
        value=20,
        step=1
    )
    AveRooms = st.slider(
        "Average Rooms",
        min_value=1.0,
        max_value=20.0,
        value=5.0,
        step=0.1
    )
    AveBedrms = st.slider(
        "Average Bedrooms",
        min_value=0.5,
        max_value=10.0,
        value=1.0,
        step=0.1
    )

with col2:
    st.subheader("Location Details")
    Population = st.slider(
        "Population",
        min_value=3,
        max_value=10000,
        value=1000,
        step=10
    )
    AveOccup = st.slider(
        "Average Occupants",
        min_value=1.0,
        max_value=10.0,
        value=3.0,
        step=0.1
    )
    Latitude = st.slider(
        "Latitude",
        min_value=32.5,
        max_value=42.0,
        value=35.0,
        step=0.1
    )
    Longitude = st.slider(
        "Longitude",
        min_value=-124.0,
        max_value=-114.0,
        value=-119.0,
        step=0.1
    )

st.write("---")

if st.button("Predict House Price", use_container_width=True):
    input_data = np.array([[
        MedInc, HouseAge, AveRooms, AveBedrms,
        Population, AveOccup, Latitude, Longitude
    ]])
    prediction = model.predict(input_data)[0]
    price_dollars = prediction * 100000
    st.success(f"Predicted House Price: ${price_dollars:,.0f}")
    st.write("---")
    st.subheader("Your Input Summary")
    col3, col4 = st.columns(2)
    with col3:
        st.metric("Median Income", f"${MedInc*10000:,.0f}/yr")
        st.metric("House Age", f"{HouseAge} years")
        st.metric("Avg Rooms", f"{AveRooms}")
        st.metric("Avg Bedrooms", f"{AveBedrms}")
    with col4:
        st.metric("Population", f"{Population:,}")
        st.metric("Avg Occupants", f"{AveOccup}")
        st.metric("Latitude", f"{Latitude}")
        st.metric("Longitude", f"{Longitude}")