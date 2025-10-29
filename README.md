🧠 Fraud Detection using Machine Learning & Graph Analytics
📋 Overview

This project focuses on detecting fraudulent transactions using both tabular and graph-based machine learning approaches.
It aims to identify suspicious behavior through feature engineering, data balancing, and model comparison (Random Forest vs XGBoost).

⚙️ Project Structure
notebooks/
 ├── 1_tabular_random_forest.ipynb
 ├── 2_graph_random_forest.ipynb
 ├── 3_tabular_xgboost.ipynb
 └── 4_graph_xgboost.ipynb
data/
 └── (not included — due to size, hosted externally)

🚀 Workflow Summary
1️⃣ Tabular Random Forest

Data cleaning, encoding, and undersampling (KMeans).

Behavioral pattern extraction with association rules (Apriori).

Training a Random Forest for baseline fraud detection.

📈 Result: Good recall and precision on the fraud class after balancing.

2️⃣ Graph Random Forest

Construction of a directed transaction graph using NetworkX.

Computation of centrality measures (degree, betweenness, closeness, eigenvector).

Random Forest trained on enriched graph features.

📈 Result: Excellent ROC-AUC (~0.996). Graph features improved fraud interpretability.

3️⃣ Tabular XGBoost

Same tabular preprocessing pipeline as notebook 1.

XGBoost model applied for better robustness and feature interaction handling.

📈 Result: Higher recall and ROC-AUC compared to Random Forest.

4️⃣ Graph XGBoost

Integration of graph features + XGBoost classifier.

Combined effect of relational data and gradient boosting for enhanced detection.

📈 Result: Strong predictive power with high AUC and improved detection of subtle frauds.

🧩 Key Insights

Data preprocessing & balancing (SMOTE, undersampling) are crucial for performance.

Graph features significantly improve model understanding of relationships.

XGBoost proved more robust and adaptable than Random Forest.

🛠️ Tech Stack

Python, Pandas, Scikit-learn, XGBoost, NetworkX, Matplotlib, Imbalanced-learn, MLxtend

👩‍💻 Author

Sarra Tlili
Élève ingénieure en Informatique — ENIT