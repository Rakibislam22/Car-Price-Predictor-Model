from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("car_price_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        company = request.form['company']
        model_name = request.form['model']
        year = int(request.form['year'])
        fuel = request.form['fuel']
        km_driven = int(request.form['km_driven'])

        # Validate input
        if km_driven < 0:
            prediction_text = "Error: Kilometers cannot be negative."
        else:
            # Make dummy DataFrame for prediction
            input_df = pd.DataFrame([[model_name, year, km_driven, fuel, "Individual", "Manual", "First Owner"]],
                                    columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner'])
            
            for col in ['name', 'fuel', 'seller_type', 'transmission', 'owner']:
                input_df[col] = input_df[col].astype('category').cat.codes

            # Predict price in INR
            prediction_inr = model.predict(input_df)[0]

            # Convert INR → BDT
            inr_to_bdt = 1.4
            prediction_bdt = prediction_inr * inr_to_bdt
            prediction_text = f"Estimated Car Price: <strong>৳ {int(prediction_bdt):,}</strong>"

    except Exception as e:
        # Catch any error and show a friendly message
        prediction_text = f"Error: Could not calculate prediction. ({str(e)})"

    # Always return the template with prediction_text
    return render_template('index.html', prediction_text=prediction_text)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html', prediction_text="Page not found!"), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('index.html', prediction_text="Internal server error!"), 500

if __name__ == '__main__':
    app.run(debug=True)
