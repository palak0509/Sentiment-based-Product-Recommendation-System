from __future__ import division, print_function

import numpy as np
import pandas as pd

# Flask utils
from flask import Flask, redirect, url_for, request, render_template, jsonify

app = Flask(__name__)

#ratingsMatrix = joblib.load('user_Rating.pkl')
#productClass = joblib.load('product_sentiment.pkl')

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000)
    app.debug=True
    app.run()
