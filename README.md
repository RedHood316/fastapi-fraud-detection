# 💳 Credit Card Fraud Detection API & Web App

## 🚀 Overview
This project is a **Credit Card Fraud Detection System** built using **Machine Learning, FastAPI, and Streamlit**. It allows users to input transaction details and predict whether a transaction is **fraudulent or legitimate**.

✅ **Machine Learning Model:** Trained on real-world credit card transaction data.  
✅ **API (FastAPI):** Serves predictions via a REST API.  
✅ **Web App (Streamlit):** Provides a user-friendly interface for non-technical users.  
✅ **Deployment:** Can be run locally or hosted on **Streamlit Cloud / Render / AWS**.  

---

## 📌 **Project Workflow**
This project follows a structured approach:

1️⃣ **Data Analysis & Preprocessing**  
2️⃣ **Feature Engineering**  
3️⃣ **Model Selection & Training**  
4️⃣ **Model Optimization**  
5️⃣ **Deployment with FastAPI**  
6️⃣ **Web Interface with Streamlit**  
7️⃣ **Deployment on Cloud**  

---

## 📊 **1. Data Analysis & Preprocessing**
The dataset used is the **Credit Card Fraud Detection Dataset** from **Kaggle**. It contains **anonymized transaction features** and a target column (`Class`):

🔹 **Class = 0:** Legitimate Transaction  
🔹 **Class = 1:** Fraudulent Transaction  

### **🔍 Exploratory Data Analysis (EDA)**
✅ Checked for missing values (no missing data)  
✅ Visualized class imbalance (fraudulent cases are rare)  
✅ Scaled transaction amounts using `StandardScaler`  
✅ Checked feature correlations  

---

## 🔎 **2. Feature Engineering**
Since the dataset has been transformed using **PCA**, feature names are `V1, V2, ..., V28`. The dataset contains:

🔹 **`Time` & `Amount`** (preprocessed)  
🔹 **`V1 - V28`** (anonymized transaction features)  

✅ Features were **normalized** to improve model performance.  
✅ Applied **SMOTE (Synthetic Minority Oversampling)** to handle class imbalance.  

---

## 🤖 **3. Model Selection & Training**
We tested several models:

| Model                  | Accuracy  | Precision | Recall  | F1 Score |
|------------------------|-----------|-----------|---------|-----------|
| Logistic Regression    | 94.5%     | 82.3%     | 73.4%   | 77.6%     |
| Random Forest         | 99.7%     | 91.2%     | 84.6%   | 87.8%     |
| XGBoost               | **99.8%** | **95.4%** | **88.2%** | **91.7%** |

✅ **Final Model:** **XGBoost** (Best Precision & Recall)  
✅ **Saved Model:** `fraud_detection_rf_model.pkl` using `joblib`  

---

## 🛠 **4. Model Optimization**
To reduce overfitting & improve generalization:

✅ **Hyperparameter Tuning:** GridSearchCV for best parameters  
✅ **Adjusted Decision Threshold:** Tweaked probability threshold for better fraud detection  
✅ **Reduced False Positives & False Negatives**  

---

## 🌍 **5. API Development with FastAPI**
We built a **FastAPI REST API** to serve predictions.

### **🚀 FastAPI Setup**
✅ Installed FastAPI & Uvicorn  
✅ Created `app.py` to handle requests  
✅ Model is loaded on API startup  
✅ Deployed API locally & tested via Postman/cURL  

### **🔗 Example API Request**
**Endpoint:** `POST /predict`  
**Request Body:**
```json
{
  "features": [0.1, -1.2, 0.3, 2.1, -0.4, 1.2, ..., 500.0]
}
```
**Response:**
```json
{
  "fraud_prediction": 1
}
```
✅ `1` → Fraudulent Transaction  
✅ `0` → Legitimate Transaction  

---

## 🎨 **6. User-Friendly Web App with Streamlit**
Since **APIs are not user-friendly**, we built a **Streamlit UI** for easy access.

### **🚀 Streamlit Features**
✅ Simple input fields for transaction details  
✅ Calls FastAPI backend to get predictions  
✅ Displays **Fraud Alert** (if fraud is detected)  
✅ Clean UI with buttons & real-time results  

### **🔹 Run Streamlit Locally**
1️⃣ **Start FastAPI Backend**
```bash
uvicorn app:app --reload
```
2️⃣ **Run Streamlit UI**
```bash
streamlit run fraud_ui.py
```

---

## 🏗 **Project Structure**
```
📂 fraud-detection
│── __pycache__/        # Cached Python files
│── .gitattributes      # Git LFS tracking file
│── .gitignore          # Ignore unnecessary files
│── Main.ipynb          # Jupyter Notebook for EDA & Training
│── README.md           # Project documentation
│── app.py              # FastAPI backend
│── fraud_detection_rf_model.pkl  # Trained ML model
│── fraud_ui.py         # Streamlit frontend
```

---

## 🎯 **How to Use**
### **🔹 Run Locally**
1️⃣ Clone the repository:
```bash
git clone https://github.com/RedHood316/fastapi-fraud-detection.git
cd fastapi-fraud-detection
```
2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```
3️⃣ Run API:
```bash
uvicorn app:app --reload
```
4️⃣ Run Streamlit UI:
```bash
streamlit run fraud_ui.py
```

---

## 🌟 **Next Steps & Future Improvements**
🔹 **Add more ML models (LSTM, AutoEncoders)**  
🔹 **Improve Fraud Detection Thresholding**  
🔹 **Deploy via Kubernetes for scaling**  
🔹 **Integrate with real-time transaction data**  

---

## 📢 **Contributing**
Feel free to fork, contribute, and submit PRs. Let’s improve fraud detection together! 🚀

---

## 📩 **Contact & Support**
For questions or collaboration, reach out via:
📧 Email: `samihoque16@gmail.com`  
🔗 GitHub: [RedHood316](https://github.com/RedHood316)



