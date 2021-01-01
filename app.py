#Flask File : For Main Application (BackEnd)
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math

#render_template: Attach HTML


app   = Flask(__name__)                   #FLASK APP
model = pickle.load(open('taxi.pkl','rb'))#LOAD MODEL

@app.route('/') #Add Decorator
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features  = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0],2)
    return render_template('index.html',prediction_text="Number of Weekly Rides Should be {}".format(math.floor(output)))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
