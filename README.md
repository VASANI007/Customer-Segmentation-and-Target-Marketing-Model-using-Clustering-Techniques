<!-- 🌌 Header -->
<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,100:2c5364&height=220&section=header&text=Customer%20Segmentation%20(K-Means)&fontSize=45&fontColor=ffffff&animation=fadeIn"/>
</p>

<!-- Typing Animation -->
<p align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&duration=3000&pause=1000&color=00F7FF&center=true&vCenter=true&width=800&lines=Customer+Segmentation+Project;K-Means+Clustering+%7C+KNIME+%2B+Python;EDA+%2B+Visualization+%2B+Insights"/>
</p>

---

# 🏆 Tech Stack

![Python](https://img.shields.io/badge/Python-3670A0?logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-ffffff?logo=plotly&logoColor=black)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white)
![KNIME](https://img.shields.io/badge/KNIME-FDD800?logo=data&logoColor=black)
![Excel](https://img.shields.io/badge/Excel-217346?logo=microsoft-excel&logoColor=white)

---

# 📌 Project Overview

This project performs **Customer Segmentation using K-Means Clustering**.

It analyzes customer data based on:
- Age  
- Annual Income  
- Spending Score  

and groups customers into meaningful segments.

---

# 📊 Dataset

Dataset Source: Kaggle (Mall Customer Segmentation)

🔗 https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python

### Features:

- CustomerID  
- Gender  
- Age  
- Annual Income (k$)  
- Spending Score (1–100)  

---

# 🧠 How It Works

1. Load dataset using Pandas  
2. Perform Exploratory Data Analysis (EDA)  
3. Visualize data (scatter plots, distributions)  
4. Use **Elbow Method** to find optimal clusters  
5. Apply **K-Means Clustering**  
6. Analyze clusters for business insights  

---


# 📈 EDA (Exploratory Data Analysis)

## 🔹 Customer Distribution

![Customer Distribution](https://raw.githubusercontent.com/VASANI007/Customer-Segmentation-and-Target-Marketing-Model-using-Clustering-Techniques/main/Customer-Segmentation/images/custumer_dis.png)

👉 This scatter plot shows the relationship between **Annual Income** and **Spending Score**.  
👉 Customers are naturally distributed into different regions, indicating potential clusters.

---

## 🔹 Gender Distribution

![Gender Distribution](https://raw.githubusercontent.com/VASANI007/Customer-Segmentation-and-Target-Marketing-Model-using-Clustering-Techniques/main/Customer-Segmentation/images/Ex/Ex_01.png)

👉 Displays the count of male and female customers.  
👉 Helps in understanding demographic balance in the dataset.

---

# 📉 Elbow Method

![Elbow Method](https://raw.githubusercontent.com/VASANI007/Customer-Segmentation-and-Target-Marketing-Model-using-Clustering-Techniques/main/Customer-Segmentation/images/wcss.png)

👉 Used to determine the optimal number of clusters.  
👉 The “elbow point” is observed at **K = 5**, which is selected for clustering.

---

# 🎯 Final Clusters

![Cluster Plot](https://raw.githubusercontent.com/VASANI007/Customer-Segmentation-and-Target-Marketing-Model-using-Clustering-Techniques/main/Customer-Segmentation/images/cluster.png)

👉 Customers are grouped into **5 distinct clusters** based on behavior.  
👉 Each color represents a different customer segment.

### Cluster Types:

- High Income / High Spending (Premium Customers)  
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
# 📸 App Preview

## 🔹 Single Prediction
<p align="left">
<img src="https://raw.githubusercontent.com/VASANI007/Customer-Segmentation-and-Target-Marketing-Model-using-Clustering-Techniques/main/Customer-Segmentation/images/app.png" width="700"/>
</p>

---

## 🔹 Dataset Prediction
<p align="left">
<img src="https://raw.githubusercontent.com/VASANI007/Customer-Segmentation-and-Target-Marketing-Model-using-Clustering-Techniques/main/Customer-Segmentation/images/app1.png" width="700"/>
</p>

---

## 🔹 Cluster Visualization
<p align="left">
<img src="https://raw.githubusercontent.com/VASANI007/Customer-Segmentation-and-Target-Marketing-Model-using-Clustering-Techniques/main/Customer-Segmentation/images/app2.png" width="700"/>
</p>

---

## 🔹 Interactive Dashboard
<p align="left">
<img src="https://raw.githubusercontent.com/VASANI007/Customer-Segmentation-and-Target-Marketing-Model-using-Clustering-Techniques/main/Customer-Segmentation/images/app3.png" width="700"/>
</p>

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

# 🔄 KNIME Workflow

![KNIME Workflow](https://raw.githubusercontent.com/VASANI007/Customer-Segmentation-and-Target-Marketing-Model-using-Clustering-Techniques/main/Customer-Segmentation/images/KNIME/Flow.png)

👉 Workflow used for clustering:
- CSV Reader  
- Column Filter  
- K-Means  
- Color Manager  
- Scatter Plot  

---

# 🐍 Python Implementation

```python
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("../data/Mall_Customers.csv")

X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

kmeans = KMeans(n_clusters=5)
df['Cluster'] = kmeans.fit_predict(X)
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

# ⚙ Installation

```
pip install pandas matplotlib scikit-learn
```

Run:

```
jupyter notebook
```
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

# 🎮 Usage

- Run notebook  
- Visualize clusters  
- Analyze customer behavior  
- Use insights for business decisions  

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
