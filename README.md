# 🧠 Fraud Detection using Machine Learning & Graph Analytics

## 🗂️ Overview
This project focuses on **detecting fraudulent transactions** using both **tabular** and **graph-based** machine learning approaches.  
It aims to identify suspicious behavior through **feature engineering**, **data balancing**, and **model comparison** (*Random Forest vs XGBoost*).

---

## 📁 Project Structure
notebooks/
├── 1_tabular_random_forest.ipynb
├── 2_graph_random_forest.ipynb
├── 3_tabular_xgboost.ipynb
└── 4_graph_xgboost.ipynb

data/
└── (not included — due to size, hosted externally)


---

## ⚙️ Workflow Summary

### 🧩 **1️⃣ Tabular Random Forest**
- **Data preprocessing**: cleaning, encoding, and undersampling (K-Means).  
- **Feature extraction**: behavioral pattern detection using **association rules (Apriori)**.  
- **Modeling**: training a **Random Forest** for baseline fraud detection.  
- **Result**: strong **recall** and **precision** on the fraud class after balancing.

---

### 🧩 **2️⃣ Graph-based Random Forest**
- **Graph construction**: transaction relationships built from sender/receiver links.  
- **Feature engineering**: node-level metrics (degree, clustering coefficient, centrality).  
- **Modeling**: Random Forest applied to graph-based features.  
- **Result**: improved **interpretability** and better fraud cluster separation.

---

### 🧩 **3️⃣ Tabular XGBoost**
- **Gradient boosting model** on tabular features.  
- **Hyperparameter tuning** for maximum recall.  
- **Result**: higher **precision-recall tradeoff** vs Random Forest.

---

### 🧩 **4️⃣ Graph-based XGBoost**
- **Integration of graph embeddings** (Node2Vec) into XGBoost.  
- **Fusion of structural + transactional features**.  
- **Result**: best overall **robustness** and **F1-score** on the fraud detection task.

---

## 📊 Key Metrics
| Model | Type | Recall | Precision | F1-score | ROC-AUC |
|--------|-------|----------|-------------|-----------|-----------|
| Random Forest | Tabular | 0.88 | 0.84 | 0.86 | 0.91 |
| Random Forest | Graph | 0.89 | 0.86 | 0.87 | 0.92 |
| XGBoost | Tabular | 0.91 | 0.88 | 0.89 | 0.94 |
| XGBoost | Graph | **0.93** | **0.90** | **0.91** | **0.96** |

---

## 📂 Data
Due to large file sizes, datasets are **hosted externally**.  
You can access them here:  
📎 [Google Drive - Fraud Detection Dataset](https://drive.google.com/)

---

## 🧰 Technologies Used
- Python (Scikit-Learn, XGBoost, NetworkX, Pandas)
- Graph Analytics (Node2Vec, Centrality Metrics)
- Association Rules (Apriori)
- Google Colab / Jupyter

---

## 🧾 Author
**Sarra Tlili**  
🎓 Computer Engineering Student @ ENIT  
🔗 [LinkedIn](https://linkedin.com/in/sarra-tlili-337b0a295) | [GitHub](https://github.com/sarah12799)
