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


::contentReference[oaicite:0]{index=0}


---

## 🔹 Gender Distribution


::contentReference[oaicite:1]{index=1}


---

# 📉 Elbow Method


::contentReference[oaicite:2]{index=2}


👉 Optimal clusters: **5**

---

# 🎯 Final Clusters


::contentReference[oaicite:3]{index=3}


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

# 🔄 KNIME Workflow


::contentReference[oaicite:4]{index=4}


Steps:
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

df = pd.read_csv("Mall_Customers.csv")

X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

kmeans = KMeans(n_clusters=5)
df['Cluster'] = kmeans.fit_predict(X)
```

---

# 📂 Project Structure

```
Customer-Segmentation-KMeans/

├── data/
│   ├── Mall_Customers.csv
│
├── images/
│   ├── plots/
│
├── notebooks/
│   └── segmentation.ipynb
│
├── Customer Segmentation.knwf
└── README.md
```

---

# ⚙ Installation

```
pip install pandas matplotlib scikit-learn
```

Run:

```
jupyter notebook
```

---

# 🎮 Usage

- Run notebook  
- Visualize clusters  
- Analyze customer behavior  
- Use insights for business decisions  

---

# 🚀 Future Improvements

- Deploy dashboard  
- Add real-time clustering  
- Use advanced ML models  
- Integrate Streamlit UI  

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,100:2c5364&height=170&section=footer&text=Thanks%20for%20Visiting%20My%20Profile!&fontSize=28&fontColor=ffffff&animation=twinkling&fontAlignY=65"/>
</p>
