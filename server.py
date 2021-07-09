#pip install Flask

from flask import Flask,request,jsonify
import util

app = Flask(__name__)

@app.route('/get_column_names')
def get_column_names():
    response = {'Columns': util.column_names()}
    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    bhk = float(request.form['BHK'])
    sqft = float(request.form['SQFT'])
    bath = float(request.form['BATH'])
    balcony = float(request.form['BALCONY'])
    ar_type = request.form['AREA_TYPE']
    ap_type = request.form['AP_TYPE'] 
    location = request.form['LOCATION'] 
    
    response = jsonify({'estimated_price': util.get_predicted_price(bhk,sqft,bath,balcony,ar_type,ap_type,location)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

app.run()
