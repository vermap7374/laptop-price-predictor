# Laptop Price Predictor

This is a **Laptop Price Predictor** application built using **Machine Learning**. The model is trained on a dataset of laptop specifications and their prices and predicts the price based on user input.
---
🚀 **Live Demo:** [Deployed Link Here](https://laptop-predict-price-972b96849081.herokuapp.com/)
---

## 🚀 Features
- Predicts laptop prices based on specifications like brand, CPU, GPU, RAM, screen size, etc.
- User-friendly interface using **Streamlit**.
- Uses a **Machine Learning pipeline** for predictions.
- Supports multiple brands, operating systems, and screen resolutions.

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit** (for UI)
- **Scikit-learn** (for Machine Learning model)
- **Pandas & NumPy** (for data processing)
- **Pickle** (for model serialization)

---

## 📊 Data Processing & Model Training
The **laptop-price-predictor.ipynb** notebook contains the following steps:

1. **Data Loading & Cleaning**:
   - Reads `laptop_data.csv` into a DataFrame.
   - Removes duplicates and missing values.
   - Cleans and converts numerical columns (e.g., `Ram`, `Weight`).

2. **Feature Engineering**:
   - Extracts `Cpu Brand`, `Gpu Brand`, `Operating System`.
   - Computes **Pixels Per Inch (PPI)** using screen resolution and size.

3. **Model Training**:
   - Splits data into **training and test sets**.
   - Uses a **machine learning regression models** for price prediction.
   - Saves the trained pipeline as `pipe.pkl` using **Pickle**.

4. **Model Deployment**:
   - Loads the trained model into **Streamlit** (`app.py`).
   - Uses the saved pipeline (`pipe.pkl`) for real-time predictions.
   - Displays predicted price in an interactive UI.

---

## ⚡ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/Laptop-Price-Predictor.git
cd Laptop-Price-Predictor
```

### 2️⃣ Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🏃 Running the Application
```bash
streamlit run app.py
```
