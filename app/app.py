from pyexpat import features

from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(
    os.path.join(BASE_DIR, "kmeans_vendor_model.pkl")
)

scaler = joblib.load(
    os.path.join(BASE_DIR, "vendor_scaler.pkl")
)

segment_names = {
    0: "Strategic Vendor",
    1: "High-Margin Growth Vendor",
    2: "Underperforming Vendor"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    vendor_number = request.form["vendor_number"]
    vendor_name = request.form["vendor_name"]

    total_sales = float(request.form["total_sales"])
    profit_margin = float(request.form["profit_margin"])
    stock_turnover = float(request.form["stock_turnover"])

    log_sales = np.log1p(total_sales)

    features = pd.DataFrame({
        "LogSales":[log_sales],
        "ProfitMargin_Capped":[profit_margin],
        "StockTurnover_Capped":[stock_turnover]
    })

    scaled = scaler.transform(features)
    scaled_df = pd.DataFrame(
        scaled,
        columns=[
            "LogSales",
            "ProfitMargin_Capped",
            "StockTurnover_Capped"
            ]
        )
    cluster = model.predict(scaled_df)[0]

    segment = segment_names[cluster]

    return render_template(
        "index.html",
        prediction=segment,
        vendor_name=vendor_name,
        vendor_number=vendor_number
    )

if __name__ == "__main__":
    app.run(debug=True)