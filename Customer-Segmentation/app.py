import streamlit as st
import pickle
import numpy as np
import os
import pandas as pd
import plotly.express as px


# PAGE CONFIG

st.set_page_config(
    page_title="Customer Segmentation Ultra",
    page_icon="🛍️",
    layout="wide"
)


# LOAD MODEL

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@st.cache_resource
def load_model():
    try:
        model = pickle.load(open(os.path.join(BASE_DIR, "models", "model.pkl"), "rb"))
        scaler = pickle.load(open(os.path.join(BASE_DIR, "models", "scaler.pkl"), "rb"))
        return model, scaler
    except:
        st.error("Model files not found")
        st.stop()

model, scaler = load_model()


# SAFE PREDICTION

def safe_predict(income, score):
    try:
        income = float(income)
        score = float(score)

        if income > 200:
            income = income / 1000

        income = max(0, min(income, 150))
        score = max(1, min(score, 100))

        data = np.array([[income, score]])
        data_scaled = scaler.transform(data)

        cluster = model.predict(data_scaled)[0]
        return cluster, income, score

    except:
        return None, None, None


# HEADER

st.title("Customer Segmentation Ultra App")
st.markdown("### AI-powered smart clustering system")


# TABS

tab1, tab2, tab3 = st.tabs(["🔍 Single Prediction", "📊 Dataset Prediction", "📈 Visualization"])


# TAB 1: SINGLE
with tab1:
    st.subheader("Enter Customer Data")

    col1, col2 = st.columns(2)

    with col1:
        income = st.number_input("Annual Income (k$)", 0.0, 100000.0, 50.0)

    with col2:
        score = st.number_input("Spending Score (1-100)", 0.0, 100.0, 50.0)

    if st.button("Predict"):
        cluster, income, score = safe_predict(income, score)

        if cluster is None:
            st.error("Invalid input")
        else:
            st.success(f"Cluster: {cluster}")

            try:
                df = pd.read_csv(os.path.join(BASE_DIR, "data", "Mall_Customers.csv"))

                X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
                X_scaled = scaler.transform(X)
                df["Cluster"] = model.predict(X_scaled)

                fig = px.scatter(
                    df,
                    x="Annual Income (k$)",
                    y="Spending Score (1-100)",
                    color=df["Cluster"].astype(str),
                    title="Customer Segments"
                )

                fig.add_scatter(
                    x=[income],
                    y=[score],
                    mode="markers",
                    marker=dict(size=15, symbol="x"),
                    name="Your Input"
                )

                st.plotly_chart(fig, use_container_width=True)

            except:
                st.warning("Dataset not found")


# TAB 2: DATASET PREDICTION

with tab2:
    st.subheader("Mall Customers Dataset")

    try:
        df = pd.read_csv(os.path.join(BASE_DIR, "data", "Mall_Customers.csv"))

        # Predict
        X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
        X_scaled = scaler.transform(X)
        df["Cluster"] = model.predict(X_scaled)

        st.success("Dataset Loaded & Predicted ")

        st.dataframe(df)

        # Visualization
        fig = px.scatter(
            df,
            x="Annual Income (k$)",
            y="Spending Score (1-100)",
            color=df["Cluster"].astype(str),
            title="Dataset Customer Segmentation"
        )

        st.plotly_chart(fig, use_container_width=True)

        # Download
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Dataset with Clusters", csv, "dataset_result.csv", "text/csv")

    except:
        st.error("Dataset not found in /data folder")


# TAB 3: VISUALIZATION
with tab3:
    st.subheader("Interactive Visualization")

    try:
        df = pd.read_csv(os.path.join(BASE_DIR, "data", "Mall_Customers.csv"))

        X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
        X_scaled = scaler.transform(X)
        df["Cluster"] = model.predict(X_scaled)

        fig = px.scatter(
            df,
            x="Annual Income (k$)",
            y="Spending Score (1-100)",
            color=df["Cluster"].astype(str),
            title="Customer Segmentation (Interactive)"
        )

        st.plotly_chart(fig, use_container_width=True)

    except:
        st.error("Dataset not found")


# FOOTER
st.markdown("---")
st.caption(" Developed by Daksh Vasani | Customer Segmentation ML Project | Python • Streamlit • Plotly")