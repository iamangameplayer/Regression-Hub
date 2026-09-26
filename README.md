# Regression Hub

## Comparative Analysis of Regression Algorithms for House Price Prediction

**Regression Hub** is a Django-based machine learning web application that compares multiple regression algorithms for house price prediction.

The application provides separate interfaces for different regression models, allows users to enter housing-related features and obtain predictions, and provides a dedicated metrics section for comparing model performance.

The project was developed to demonstrate a complete machine learning workflow, from trained regression models to an interactive web-based prediction system.

---

## 📌 Features

* Interactive web-based house price prediction
* Six different regression algorithms
* Separate prediction interface for each model
* Model performance comparison
* Regression evaluation metrics
* Pre-trained machine learning models stored using Joblib
* Django-based backend
* HTML/CSS-based frontend
* Dedicated pages for individual regression algorithms
* Centralized metrics and model comparison section

---

## 🤖 Machine Learning Models

Regression Hub implements and compares the following regression algorithms:

1. **Linear Regression**
2. **Ridge Regression**
3. **Random Forest Regression**
4. **K-Nearest Neighbors (KNN) Regression**
5. **Gradient Boosting Regression**
6. **XGBoost Regression**

Each model is integrated into the Django application through its own Django app and prediction interface.

---

## 📊 Model Evaluation

The models are evaluated using commonly used regression metrics:

| Metric       | Description                                                                  |
| ------------ | ---------------------------------------------------------------------------- |
| **R² Score** | Measures how well the model explains the variance in the target variable     |
| **MAE**      | Measures the average absolute difference between predicted and actual values |
| **MSE**      | Measures the average squared prediction error                                |
| **RMSE**     | Measures the square root of the mean squared error                           |

The **Metrics** section of the application provides a centralized view for examining model performance and comparing the implemented algorithms.

---

## 🌐 Web Application

The application is built using **Django** and is organized into separate components for different parts of the system.

### Main Page

Provides the entry point to Regression Hub and navigation to the different regression models and application sections.

### Regression Model Pages

Each regression algorithm has its own Django application and prediction page.

| Django App   | Model                        |
| ------------ | ---------------------------- |
| `linear`     | Linear Regression            |
| `ridge`      | Ridge Regression             |
| `regression` | Random Forest Regression     |
| `knnreg`     | KNN Regression               |
| `gradient`   | Gradient Boosting Regression |
| `xgbst`      | XGBoost Regression           |
| `metrics`    | Metrics & Model Comparison   |
| `mainpage`   | Main Application Page        |

---

## 🏗️ System Architecture

```text
                         Regression Hub
                              │
                              ▼
                       Django Web App
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
        Main Page       Model Prediction    Metrics
                              │                │
              ┌───────────────┼────────────┐   │
              │       │       │      │     │   │
              ▼       ▼       ▼      ▼     ▼   ▼
           Linear   Ridge    RF     KNN   GB   XGBoost
              │       │       │      │     │     │
              └───────┴───────┴──────┴─────┴─────┘
                              │
                              ▼
                       House Price
                        Prediction
```

---

## 🔄 Machine Learning Workflow

```text
Housing Dataset
      ↓
Data Preprocessing
      ↓
Feature Engineering
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Model Selection / Comparison
      ↓
Model Serialization
      ↓
Django Integration
      ↓
User Input
      ↓
House Price Prediction
```

The trained models are serialized using **Joblib** and loaded by the Django application when predictions are requested.

---

## 💻 Technologies Used

### Backend

* Python
* Django

### Machine Learning

* Scikit-learn
* XGBoost
* Joblib

### Data Processing

* Pandas
* NumPy

### Frontend

* HTML
* CSS

### Database

* SQLite

### Development & Version Control

* Git
* GitHub

---

## 📁 Project Structure

```text
Regression-Hub/
│
└── machine/
    │
    ├── manage.py
    ├── db.sqlite3
    │
    ├── adaboost_regressor.joblib
    ├── gradient_boosting_regressor.joblib
    │
    ├── machine/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    │
    ├── mainpage/
    │   ├── views.py
    │   ├── urls.py
    │   ├── templates/
    │   └── static/
    │
    ├── linear/
    │   ├── views.py
    │   ├── urls.py
    │   ├── templates/
    │   └── static/
    │
    ├── ridge/
    │   ├── views.py
    │   ├── urls.py
    │   ├── templates/
    │   └── static/
    │
    ├── regression/
    │   ├── views.py
    │   ├── urls.py
    │   ├── templates/
    │   └── static/
    │
    ├── knnreg/
    │   ├── views.py
    │   ├── urls.py
    │   ├── templates/
    │   └── static/
    │
    ├── gradient/
    │   ├── views.py
    │   ├── urls.py
    │   ├── templates/
    │   └── static/
    │
    ├── xgbst/
    │   ├── views.py
    │   ├── urls.py
    │   ├── templates/
    │   └── static/
    │
    └── metrics/
        ├── views.py
        ├── urls.py
        ├── templates/
        └── static/


⚙️ Installation
1. Clone the repository

```bash
git clone https://github.com/iamangameplayer/Regression-Hub.git
```

2. Navigate to the project

```bash
cd Regression-Hub/machine
```

3. Create a virtual environment

```bash
python -m venv venv
```

 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

 5. Install dependencies

```bash
pip install django pandas numpy scikit-learn xgboost joblib
```
 6. Run database migrations

```bash
python manage.py migrate
```

 7. Start the development server

```bash
python manage.py runserver
```

Open the local application at:

```text
http://127.0.0.1:8000/
```

---

📈 Results

Regression Hub provides a dedicated model comparison section where the implemented algorithms can be evaluated using:

 R² Score
MAE
MSE
RMSE

This allows the performance of different regression approaches to be examined under the same prediction task.



🎯 Project Objective

The objective of Regression Hub is to develop an interactive machine learning application that demonstrates and compares different regression techniques for house price prediction.

The project combines machine learning with web development by integrating trained regression models into a Django application, allowing users to interact with the models through a browser rather than executing prediction code manually.

---
🔮 Future Scope

Potential improvements include:

Adding more regression algorithms
Improving feature engineering and selection
Adding interactive data visualizations
Adding model explainability
Improving prediction accuracy through further hyperparameter optimization
Adding user authentication
Storing prediction history
Deploying the application to a cloud platform
Adding support for additional datasets



📸 Application Screenshots

Screenshots of the Regression Hub interface can be added here to demonstrate:

* Main page
* Linear Regression prediction page
* Ridge Regression prediction page
* Random Forest prediction page
* KNN prediction page
* Gradient Boosting prediction page
* XGBoost prediction page
* Model metrics and comparison page

👨‍💻 Author

**iamangameplayer**

GitHub:
https://github.com/iamangameplayer


📜 License

This project was developed for educational and academic purposes.
