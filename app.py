from flask import Flask 
from flask import request
from flask import jsonify
from modules.insurance_predict import InsurancePredict
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return "API Modeling"

@app.route("/predict", methods=['POST'])
def predict ():
    data = request.get_json()
    df = pd.DataFrame(data, index=[0])
    result_predict = InsurancePredict().runModel(
        df, typed='single')
    
    result_predict = 'interested'
    
    return jsonify({
        "status": "Predicted",
        "predict_result": result_predict
    })