
# 🌱 OptiCrop
# Smart Agricultural Production Optimization Engine

OptiCrop is a Machine Learning-powered web application that recommends the most suitable crop based on soil nutrients and environmental conditions. The application helps farmers, students, and agricultural enthusiasts make informed crop selection decisions using predictive analytics and an interactive web interface.

---

# 📖 Project Overview

Agriculture is one of the most important sectors for food production, and selecting the right crop is essential for achieving higher productivity and better profitability.

OptiCrop uses a trained Machine Learning model to analyze soil nutrients and environmental conditions, including Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Soil pH, and Rainfall, to recommend the most suitable crop.

The application features a clean, responsive, and user-friendly interface that allows users to enter soil parameters and instantly receive crop recommendations along with detailed crop information.

---

# ✨ Features

- 🌾 AI-based Crop Recommendation
- 🤖 Machine Learning Prediction Model
- 📊 Interactive Dashboard with Charts
- 🌱 Detailed Information for 22 Crops
- 🖼️ Crop Images for Every Prediction
- 🌡️ Temperature Recommendation
- 💧 Rainfall Information
- 🌱 Soil pH Details
- 📅 Growing Season Information
- 🧪 Fertilizer Recommendation
- 💡 Farmer Tips
- 📱 Responsive Modern User Interface
- ⚡ Real-time Crop Prediction
- ✅ Input Validation
- 🌍 Flask-based Web Application

---

# 📊 Input Parameters

The Machine Learning model accepts the following parameters:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature (°C)
- Humidity (%)
- Soil pH
- Rainfall (mm)

---

# 🌾 Supported Crops

The system recommends any of the following 22 crops:

- Rice
- Maize
- Chickpea
- Kidney Beans
- Pigeon Peas
- Moth Beans
- Mung Bean
- Black Gram
- Lentil
- Pomegranate
- Banana
- Mango
- Grapes
- Watermelon
- Muskmelon
- Apple
- Orange
- Papaya
- Coconut
- Cotton
- Jute
- Coffee

---

# 🛠️ Technologies Used

## Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap

## Backend

- Python
- Flask

## Machine Learning

- Scikit-learn
- Pandas
- NumPy
- Joblib

## Data Visualization

- Chart.js

## Development Tools

- Visual Studio Code
- Git
- GitHub

---

# 📁 Project Structure

```
OptiCrop/
│
├── app.py
├── crop_data.py
├── model.pkl
├── requirements.txt
├── README.md
├── Crop_recommendation.csv
├── train_model.py
│
├── static/
│   ├── style.css
│   └── images/
│       ├── hero.png
│       ├── logo.png
│       ├── rice.jpg
│       ├── maize.jpg
│       ├── banana.jpg
│       └── ... (22 crop images)
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── dashboard.html
│   ├── predict.html
│   └── result.html
```

---

# ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/tejo798/OptiCrop.git
```

### Navigate to the Project Folder

```bash
cd OptiCrop
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

### Open in Browser

```
http://127.0.0.1:5000
```

---

# 🧠 Machine Learning Workflow

1. Dataset Collection
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Model Training
6. Model Evaluation
7. Model Serialization using Joblib
8. Flask Backend Integration
9. Frontend Development
10. Crop Prediction

---

# 🎯 Objectives

- Recommend the most suitable crop based on soil nutrients and environmental conditions.
- Help farmers make better agricultural decisions.
- Improve crop productivity using Machine Learning.
- Provide a simple and interactive web application.
- Promote smart and data-driven farming practices.

---

# 📊 Dashboard

The dashboard provides visual insights into the crop recommendation dataset using interactive charts:

- 🌾 Crop Distribution (Pie Chart)
- 🌱 Average Soil Nutrients (Bar Chart)
- 🌡️ Temperature Analysis (Line Chart)
- 🌧️ Rainfall Analysis (Bar Chart)

---

# 🌾 Crop Information

For every predicted crop, OptiCrop displays:

- Crop Image
- Crop Name
- Description
- Ideal Temperature
- Rainfall Requirement
- Soil pH Range
- Growing Season
- Recommended Fertilizer
- Farmer Tip

---

# 📌 Future Enhancements

- 🌦️ Weather API Integration
- 🧪 Advanced Fertilizer Recommendation
- 🌿 Crop Disease Detection
- 📈 Crop Yield Prediction
- 🌍 Multi-language Support
- 📱 Android Mobile Application
- ☁️ Cloud Deployment
- 📍 GPS-based Soil Recommendation

---
