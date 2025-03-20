import streamlit as st  # Streamlit for interactive UI
import pickle  # Pickle for loading saved ML models
import numpy as np  # NumPy for numerical operations

# Set up the Streamlit app title with a stylish heading
st.title("💻 Laptop Price Predictor (₹)")

# Load the trained machine learning pipeline and dataset
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Brand selection
company = st.selectbox('🏷️ Select Brand:', df['Company'].unique())

# Laptop Type selection
type = st.selectbox('🖥️ Select Laptop Type:', df['TypeName'].unique())

# RAM selection
ram = st.selectbox('💾 Select RAM (GB):', [2, 4, 6, 8, 12, 16, 24, 32, 64])

# Weight input
weight = st.number_input("⚖️ Enter Laptop Weight (kg):", min_value=0.5, max_value=5.0, step=0.1)

# Touchscreen selection
touchscreen = st.selectbox('📱 Touchscreen:', ['No', 'Yes'])

# IPS Display selection
ips = st.selectbox('🔲 IPS Display:', ['No', 'Yes'])

# Screen size selection
screen_size = st.slider('📏 Screen Size (in inches):', 10.0, 18.0, 13.0)

# Screen resolution selection
resolution = st.selectbox('🔳 Screen Resolution:', [
    '1920x1080', '1366x768', '1600x900', '3840x2160',
    '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'
])

# CPU selection
cpu = st.selectbox('⚡ Select CPU:', df['Cpu Brand'].unique())

# HDD selection
hdd = st.selectbox('🛢️ Select HDD (in GB):', [0, 128, 256, 512, 1024, 2048])

# SSD selection
ssd = st.selectbox('🚀 Select SSD (in GB):', [0, 8, 128, 256, 512, 1024])

# GPU selection
gpu = st.selectbox('🎮 Select GPU Brand:', df['Gpu Brand'].unique())

# Operating System selection
os = st.selectbox('🖥️ Select Operating System:', df['os'].unique())

# Button to predict price
if st.button('🔮 Predict Price'):
    
    # Convert categorical inputs to numerical format
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0
    
    # Extract screen resolution width and height
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    
    # Calculate Pixels Per Inch (PPI)
    ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size
    
    # Create a query array for prediction
    query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])

    # Reshape the query to match model input format
    query = query.reshape(1, 12)
    
    # Make prediction and convert from log scale to actual price
    predicted_price = int(np.exp(pipe.predict(query)[0]))
    
    # Display the predicted price in INR with better formatting
    st.success(f"💰 The predicted price of this laptop configuration is **₹{predicted_price:,}**")
