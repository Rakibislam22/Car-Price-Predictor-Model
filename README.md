# Car Price Predictor

[![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)](https://www.python.org/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Live Demo](https://img.shields.io/badge/Live-Deployment-brightgreen?style=flat-square)](https://rakibislam22.pythonanywhere.com)

A web-based **Car Price Predictor** built using **Flask**, which estimates the resale price of a car based on user inputs. The prediction is done using a **machine learning model** and displayed in **Bangladeshi Taka (BDT)** with results shown in a **Bootstrap modal popup**.  

---

## **Live Deployment**

Try the app online here: [Car Price Predictor Live](https://rakibislam22.pythonanywhere.com/)  


---

## **Demo Screenshot**

<p align="center">
  <img src="https://raw.githubusercontent.com/Rakibislam22/Car-Price-Predictor-Model/main/screenshoots/home.png" width="350" />
  <img src="https://raw.githubusercontent.com/Rakibislam22/Car-Price-Predictor-Model/main/screenshoots/image.png" width="350" />
</p>
*Example of the prediction modal showing estimated price.*

---

## **Features**

- Predict car price based on:
  - Company
  - Model
  - Year of purchase
  - Fuel type
  - Kilometres driven
- Converts price from **INR → BDT** automatically
- Shows prediction results in a **modal popup**
- Bold numeric price for better visibility
- Responsive UI with **Bootstrap 5**
- Error handling for invalid inputs and server errors
- Friendly 404 and 500 error pages

---

## **Installation**

1. **Clone the repository**

```bash
git clone https://github.com/Rakibislam22/Car-Price-Predictor-Model.git
cd Car-Price-Predictor-Model
````

2. **Create and activate a virtual environment ( If faces any Errors in Global )**

```bash
# Deactivate any current virtual environment
deactivate

# Create a new virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/macOS)
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Flask app**

```bash
python app.py
```

5. Open your browser and visit: `http://127.0.0.1:5000/`

---

## **Usage**

1. Open the app in your browser.
2. Fill in the car details in the form.
3. Click **Predict Price**.
4. View the estimated price in a **modal popup**.
5. Errors (e.g., negative km) are displayed in **red**, while successful predictions are **green/blue**.

---

## **Project Structure**

```
car-price-predictor/
│
├─ app.py                   # Main Flask app
├─ car_price_model.pkl      # Trained ML model
├─ requirements.txt         # Python dependencies
├─ templates/
│   └─ index.html           # HTML template
 other static files
```

---

## **Error Handling**

* Invalid input or server errors are displayed in the modal.
* 404 page → “Page not found!”
* 500 page → “Internal server error!”

---

## **Technologies Used**

* **Backend:** Python, Flask, pandas, scikit-learn
* **Frontend:** HTML, CSS, Bootstrap 5
* **Deployment:** PythonAnywhere, Render, Railway

---

## **How the Prediction Works**

1. User enters car details in the form.
2. Flask app receives data via `POST` request.
3. Data is preprocessed into a format suitable for the ML model.
4. The model predicts car price in INR.
5. Price is converted to BDT and displayed in a **modal popup**.

---

## **Contributing**

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Add feature"`
4. Push to branch: `git push origin feature-name`
5. Open a Pull Request.

---

## **License**

This project is licensed under the **MIT License**.

---

## **Author**

**Md Rakib Ali**
[GitHub Profile](https://github.com/Rakibislam22)


