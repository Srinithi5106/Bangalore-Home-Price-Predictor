# Bangalore Home Price Predictor

A Machine Learning-powered web application that accurately estimates house prices in Bangalore based on user inputs such as area (sqft), location, number of bedrooms (BHK), and number of bathrooms.

**Live Demo:** [bangalore-home-price-predictor.onrender.com](https://bangalore-home-price-predictor-59fa.onrender.com)

---

## Features

* **Trained ML Model** using Linear Regression for optimal accuracy
* **Dynamic Location Dropdown** populated from the model's dataset
* **AJAX-enabled Interface** – no page reloads
* **Real-time Price Prediction** based on user inputs
* **Deployed on Render** – accessible from anywhere

---

## ML Model Overview

The core model was selected using cross-validation and grid search:

* **Algorithms Evaluated:**
    * Linear Regression (Best performing model)
    * Lasso Regression
    * Decision Tree Regressor
* **Techniques Used:**
    * `cross_val_score` for model evaluation
    * `GridSearchCV` for hyperparameter tuning
    * Feature encoding for location-based categorical variables

---

## Tech Stack

| Category   | Tools / Libraries                          |
| :--------- | :----------------------------------------- |
| Backend    | Flask                                      |
| ML/DS      | scikit-learn, pandas, numpy, Jupyter Notebook |
| Frontend   | HTML, CSS, JavaScript, jQuery              |
| Deployment | Render                                     |

---

# Bangalore Home Price Predictor

A Machine Learning-powered web application that accurately estimates house prices in Bangalore based on user inputs such as area (sqft), location, number of bedrooms (BHK), and number of bathrooms.

**Live Demo:** [bangalore-home-price-predictor.onrender.com](https://bangalore-home-price-predictor-59fa.onrender.com)

---

## Features

* **Trained ML Model** using Linear Regression for optimal accuracy
* **Dynamic Location Dropdown** populated from the model's dataset
* **AJAX-enabled Interface** – no page reloads
* **Real-time Price Prediction** based on user inputs
* **Deployed on Render** – accessible from anywhere

---

## ML Model Overview

The core model was selected using cross-validation and grid search:

* **Algorithms Evaluated:**
    * Linear Regression (Best performing model)
    * Lasso Regression
    * Decision Tree Regressor
* **Techniques Used:**
    * `cross_val_score` for model evaluation
    * `GridSearchCV` for hyperparameter tuning
    * Feature encoding for location-based categorical variables

---

## Tech Stack

| Category   | Tools / Libraries                          |
| :--------- | :----------------------------------------- |
| Backend    | Flask                                      |
| ML/DS      | scikit-learn, pandas, numpy, Jupyter Notebook |
| Frontend   | HTML, CSS, JavaScript, jQuery              |
| Deployment | Render                                     |

---

## How to Run Locally

1.  **Clone the repo**
    ```bash
    git clone [https://github.com/Srinithi5106/Bangalore-Home-Price-Predictor.git](https://github.com/Srinithi5106/Bangalore-Home-Price-Predictor.git)
    cd Bangalore-Home-Price-Predictor
    ```
2.  **Create virtual environment & activate**
    ```bash
    python -m venv venv
    venv\Scripts\activate    # On Windows
    ```
3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the app**
    ```bash
    python main.py
    ```
5.  **Open in browser**
    ```
    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
    ```

---

## Screenshots

![Bangalore Home Price Predictor UI](project_screenshot.png "The main prediction interface of the Bangalore Home Price Predictor.")

## Contact

Created by [Srinithi Babu](https://github.com/Srinithi5106) <br>
Feel free to star the repo or [open an issue](https://github.com/Srinithi5106/Bangalore-Home-Price-Predictor/issues) for suggestions!
