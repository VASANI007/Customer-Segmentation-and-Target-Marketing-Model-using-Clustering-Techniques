<!-- 🌌 Header -->
<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,100:2c5364&height=220&section=header&text=Customer%20Segmentation%20(K-Means)&fontSize=45&fontColor=ffffff&animation=fadeIn"/>
</p>

<!-- Typing Animation -->
<p align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=00F7FF&center=true&vCenter=true&width=800&lines=Customer+Segmentation+Project;K-Means+Clustering+using+Python+%2B+KNIME;Data+Analysis+%7C+Visualization+%7C+Business+Insights"/>
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

This project focuses on **Customer Segmentation using K-Means Clustering**.

The goal is to analyze customer behavior and divide customers into different groups based on:

- Annual Income  
- Spending Score  

This helps businesses apply **targeted marketing strategies**.

---

# 📊 Dataset

Dataset Source: Kaggle (Mall Customers Dataset)

🔗 https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python

### Features:

- CustomerID  
- Gender  
- Age  
- Annual Income (k$)  
- Spending Score (1–100)  

---

# 🧠 Project Workflow

### 🔹 Step 1: Data Loading
- Dataset loaded using Python (Pandas)

### 🔹 Step 2: Data Analysis (EDA)
- Scatter plot visualization  
- Customer behavior analysis  

### 🔹 Step 3: Elbow Method
- Optimal number of clusters found: **K = 5**

### 🔹 Step 4: K-Means Clustering
- Applied clustering algorithm  
- Customers grouped into segments  

### 🔹 Step 5: Visualization
- Cluster visualization using Python & KNIME  

---

# 📈 EDA (Exploratory Data Analysis)

## 🔹 Customer Distribution
- Scatter plot between Income & Spending  
- Shows natural grouping of customers  

---

# 📉 Elbow Method

- Used to determine optimal clusters  
- Elbow point found at: **K = 5**

---

# 🎯 Final Clusters (Results)

Customers are divided into 5 segments:

- 💎 High Income – High Spending (Premium Customers)  
- 💰 High Income – Low Spending  
- 🛍 Low Income – High Spending  
- 📉 Low Income – Low Spending  
- ⚖ Average Customers  

---

# 📊 Cluster Analysis (Business View)

| Cluster | Type | Strategy |
|--------|------|---------|
| 0 | Average Customers | General marketing |
| 1 | Premium Customers | VIP offers, luxury ads |
| 2 | High Spenders | Discounts & combos |
| 3 | Rich but Low Spend | Targeted ads |
| 4 | Budget Customers | Low-cost deals |

---

# 🔄 KNIME Implementation

Workflow Used:

- CSV Reader  
- Column Filter  
- K-Means  
- Color Manager  
- Scatter Plot  

✔ Clusters visualized using different colors  
✔ Workflow-based implementation (no coding)

---

# 🐍 Python Implementation

```python
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("Mall_Customers.csv")

X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

print(df.head())
