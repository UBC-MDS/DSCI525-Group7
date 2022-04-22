from flask import Flask, request, jsonify
import joblib
import numpy as np
## Import any other packages that are needed

app = Flask(__name__)

# 1. Load your model here
# model url: 'https://mds-s3-group7.s3.us-west-2.amazonaws.com/model.joblib'
model = joblib.load('model.joblib')

# 2. Define a prediction function
def return_prediction(content):
    # format input_data here so that you can pass it to model.predict()
    
    return model.predict(np.array(content).reshape(1, -1))

# 3. Set up home page using basic html
@app.route("/")
def index():
    # feel free to customize this if you like
    return """
    <h1>Welcome to our rain prediction service</h1>
    To use this service, make a JSON post request to the /predict url with 25 climate model outputs.
    
    You may use the following curl command:
    curl -X POST http://54.202.154.96:8080/predict -d '{"data":[1,2,3,4,53,11,22,37,41,53,11,24,31,44,53,11,22,35,42,53,12,23,31,42,53]}' -H "Content-Type: application/json"
    """

# 4. define a new route which will accept POST requests and return model predictions
@app.route('/predict', methods=['POST'])
def rainfall_prediction():
    content = request.json  # this extracts the JSON content we sent

    prediction = round(return_prediction(content['data'])[0],2)
    results = {"Output": f"Prediction: {prediction} mm of rainfall!"}  # return predictions
        
    rtn = jsonify(results)
    return rtn