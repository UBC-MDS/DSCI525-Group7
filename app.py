from flask import Flask, request, jsonify
import joblib
import numpy as np
## Import any other packages that are needed

app = Flask(__name__)

# 1. Load your model here
model = joblib.load(...)

# 2. Define a prediction function
def return_prediction(...):

    # format input_data here so that you can pass it to model.predict()

    return model.predict(...)

# 3. Set up home page using basic html
@app.route("/")
def index():
    # feel free to customize this if you like
    return """
    <h1>Welcome to our rain prediction service</h1>
    To use this service, make a JSON post request to the /predict url with 25 climate model outputs.
    
    You may use the following curl command:
    curl -X POST http://127.0.0.1:5000/predict -d '{"cm1":"value", "cm2":"value", "cm3":"value", "cm4":"value", "cm5":"value", "cm6":"value", "cm7":"value", "cm8":"value", "cm9":"value", "cm10":"value", "cm11":"value", "cm12":"value", "cm13":"value", "cm14":"value", "cm15":"value", "cm16":"value", "cm17":"value", "cm18":"value", "cm19":"value", "cm20":"value", "cm21":"value", "cm22":"value", "cm23":"value", "cm24":"value", "cm25":"value"
}' -H "Content-Type: application/json"
    """

# 4. define a new route which will accept POST requests and return model predictions
@app.route('/predict', methods=['POST'])
def rainfall_prediction():
    content = request.json  # this extracts the JSON content we sent

    # Capturing the 25 climate model inputs
    cm1 = content[cm1]
    cm2 = content[cm2]
    cm3 = content[cm3]
    cm4 = content[cm4]
    cm5 = content[cm5]
    cm6 = content[cm6]
    cm7 = content[cm7]
    cm8 = content[cm8]
    cm9 = content[cm9]
    cm10 = content[cm10]
    cm11 = content[cm11]
    cm12 = content[cm12]
    cm13 = content[cm13]
    cm14 = content[cm14]
    cm15 = content[cm15]
    cm16 = content[cm16]
    cm17 = content[cm17]
    cm18 = content[cm18]
    cm19 = content[cm19]
    cm20 = content[cm20]
    cm21 = content[cm21]
    cm22 = content[cm22]
    cm23 = content[cm23]
    cm24 = content[cm24]
    cm25 = content[cm25]

    prediction = return_prediction(cm1, cm2, cm3, cm4, cm5, cm6, cm7, cm8, cm9, cm10, cm11, cm12, cm13,
                                   cm14, cm15, cm16, cm17, cm18, cm19, cm20, cm21, cm22, cm23, cm24, cm25)
    results = {"Input Climate Models": name,
               "Output": f"Prediction: {prediction}!"}  # return whatever data you wish, it can be just the prediction
                                                        # or it can be the prediction plus the input data, it's up to you
    return jsonify(results)