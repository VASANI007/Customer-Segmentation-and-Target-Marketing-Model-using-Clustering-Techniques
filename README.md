<!-- 🌌 Header -->
<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,100:2c5364&height=220&section=header&text=Customer%20Segmentation%20AI%20App&fontSize=45&fontColor=ffffff&animation=fadeIn"/>
</p>

<!-- Typing -->
<p align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&duration=3000&pause=1000&color=00F7FF&center=true&vCenter=true&width=900&lines=Customer+Segmentation+using+K-Means;Streamlit+Interactive+App;Python+%7C+ML+%7C+Data+Visualization"/>
</p>

---

# 🏆 Tech Stack

![Python](https://img.shields.io/badge/Python-3670A0?logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white)
![KNIME](https://img.shields.io/badge/KNIME-FDD800?logo=data&logoColor=black)

---

# 📌 Project Overview

This project performs **Customer Segmentation using K-Means Clustering** and provides a **Streamlit-based interactive web application**.

It allows:
- Customer clustering  
- Real-time predictions  
- Interactive visualization  
- Dataset-level analysis  

---

# 📊 Dataset

Dataset Source: Kaggle  
https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python

### Features:

- CustomerID  
- Gender  
- Age  
- Annual Income (k$)  
- Spending Score (1–100)  

---

# 🧠 How It Works

1. Load dataset using Pandas  
2. Select key features (Income & Spending Score)  
3. Apply Standard Scaling  
4. Train K-Means model  
5. Save model files  
6. Use Streamlit app for predictions & visualization  

---

# 🎯 Final Clusters

![Clusters](https://raw.githubusercontent.com/VASANI007/Customer-Segmentation-and-Target-Marketing-Model-using-Clustering-Techniques/main/Customer-Segmentation/images/cluster.png)

### Cluster Types:

- High Income / High Spending  
- High Income / Low Spending  
- Low Income / High Spending  
- Low Income / Low Spending  
- Average Customers  

---

# 📊 Cluster Analysis

| Cluster | Description |
|--------|------------|
| 0 | Average Customers |
| 1 | High Income - High Spending |
| 2 | Young High Spenders |
| 3 | Rich but Low Spenders |
| 4 | Low Income Customers |

---

# 🖥️ Streamlit Application

## 🔹 App Features

From your `app.py` :contentReference[oaicite:0]{index=0}:

### 🧩 3 Powerful Tabs

### 1️⃣ Single Prediction
- Input Income & Spending Score  
- Predict cluster instantly  
- Shows visualization with your input point  

### 2️⃣ Dataset Prediction
- Loads full dataset  
- Applies clustering  
- Displays table + chart  
- Download result CSV  

### 3️⃣ Visualization
- Interactive Plotly scatter plot  
- Real-time cluster visualization  

---

## 📸 App Preview

<p align="center">
<img src="https://raw.githubusercontent.com/VASANI007/Customer-Segmentation-and-Target-Marketing-Model-using-Clustering-Techniques/main/Customer-Segmentation/images/app.png" width="250"/>
<img src="https://raw.githubusercontent.com/VASANI007/Customer-Segmentation-and-Target-Marketing-Model-using-Clustering-Techniques/main/Customer-Segmentation/images/app1.png" width="250"/>
<img src="https://raw.githubusercontent.com/VASANI007/Customer-Segmentation-and-Target-Marketing-Model-using-Clustering-Techniques/main/Customer-Segmentation/images/app2.png" width="250"/>
<img src="https://raw.githubusercontent.com/VASANI007/Customer-Segmentation-and-Target-Marketing-Model-using-Clustering-Techniques/main/Customer-Segmentation/images/app3.png" width="250"/>
</p>

---

# ⚙️ How to Run (IMPORTANT)

### 1️⃣ Install Dependencies

```
pip install pandas numpy scikit-learn streamlit plotly
```

---

### 2️⃣ Train Model (First Time Only)

Run:

```
python train_model.py
```

👉 This will:
- Train KMeans model  
- Save model.pkl, scaler.pkl, features.pkl  
- Generate output dataset  

(From your script) :contentReference[oaicite:1]{index=1}

---

### 3️⃣ Run App

```
streamlit run app.py
```

---

# 🤖 Model Details

Inside `/models`:

- `model.pkl` → KMeans clustering model  
- `scaler.pkl` → StandardScaler  
- `features.pkl` → Selected features  

---

# 🧠 Model Training Pipeline

From `train_model.py`:

```
1. Load dataset
2. Select features
3. Apply StandardScaler
4. Train KMeans (k=5)
5. Save model & scaler
6. Generate clustered dataset
```

---

# 📂 Project Structure

```
Customer-Segmentation/

├── data/
│   ├── Mall_Customers.csv
│   ├── output_with_clusters.csv
│
├── images/
│
├── models/
│   ├── model.pkl
│   ├── scaler.pkl
│   ├── features.pkl
│
├── notebooks/
│
├── app.py
├── train_model.py
├── Customer Segmentation.knwf
```

---

# 🎯 Use Cases

- Customer targeting  
- Marketing segmentation  
- Business analytics  
- Recommendation systems  

---

# 🚀 Future Improvements

- Deploy online (Streamlit Cloud)  
- Add user authentication  
- Add ML explainability  
- Real-time data pipeline  

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,100:2c5364&height=170&section=footer&text=Thanks%20for%20Visiting%20My%20Profile!&fontSize=28&fontColor=ffffff&animation=twinkling&fontAlignY=65"/>
</p>
