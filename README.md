# Heart Disease Prediction

This project aims to predict the presence of heart disease in patients using machine learning algorithms. By analyzing various medical attributes, the model determines the likelihood of a patient having heart disease.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Web Application](#web-application)

## Introduction

Heart disease is a leading cause of mortality worldwide. Early detection can significantly improve treatment outcomes and patient quality of life. This project leverages machine learning techniques to assist in the early detection of heart disease, potentially aiding healthcare professionals in making informed decisions.

## Dataset

The dataset used in this project contains 303 instances with 14 attributes. Each attribute provides specific medical information about the patients. The dataset is included in this repository as `heart_disease.csv`.



## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/AlaMosleh/Heart-Disease-prediction.git
   cd Heart-Disease-prediction
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use 'env\Scripts\activate'
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Data Preprocessing**:

   The dataset undergoes preprocessing steps such as feature scaling. These steps are implemented in the `Heart_disease.ipynb` notebook.

2. **Model Training**:

   Various machine learning algorithms, including Decision Trees, XGBoost, Random Forests, and Support Vector Machines, are trained and evaluated. The training process is detailed in the `Heart_disease.ipynb` notebook.

3. **Model Evaluation**:

   The models are evaluated using metrics like accuracy, precision, recall, and F1-score. The Random Forest classifier achieved the highest accuracy of 85%.

## Web Application

A Streamlit web application is developed to provide an interactive interface for users to input medical attributes and receive heart disease predictions. To run the app:

```bash
streamlit run streamlit.py
```

This will launch the web application in your default web browser.
