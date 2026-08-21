# Vendor Segmentation and Performance Analysis Using K-Means Clustering

## Project Overview

This project focuses on analyzing vendor performance and segmenting vendors into meaningful business groups using Machine Learning. The objective is to help businesses identify strategic suppliers, uncover growth opportunities, and improve supplier management decisions through data-driven insights.

The project combines **SQL, Python, Machine Learning, Power BI, and Flask** to build an end-to-end analytics solution.

---

## Business Problem

Organizations often work with numerous vendors but lack a structured approach to evaluate their performance.

Key business questions addressed:

* Which vendors contribute the most to revenue?
* Which vendors generate the highest profit margins?
* Which vendors demonstrate efficient inventory movement?
* Which vendors are underperforming and require intervention?

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* SQL
* Power BI
* Flask
* Joblib

---

## Project Workflow

### 1. Data Cleaning & Preparation

* Handled missing values and inconsistencies.
* Performed data transformation and preprocessing.
* Created a vendor-level analytical dataset.

### 2. Exploratory Data Analysis (EDA)

* Vendor sales analysis.
* Profitability analysis.
* Inventory turnover analysis.
* Outlier detection and treatment.

### 3. Feature Engineering

Created key business metrics:

* Total Sales
* Profit Margin
* Stock Turnover
* Log Sales Transformation
* Outlier Capping

### 4. Feature Scaling

Applied **StandardScaler** to normalize features before clustering.

### 5. Vendor Segmentation Using K-Means

* Implemented K-Means Clustering.
* Used Elbow Method and Silhouette Analysis for optimal cluster selection.
* Selected **K = 3** as the final clustering solution.

---

### Segment Characteristics

#### Strategic Vendors

* Highest average sales
* Stable profitability
* Core revenue contributors

#### High-Margin Growth Vendors

* Highest profit margins
* Highest stock turnover
* Strong growth potential

#### Underperforming Vendors

* Low sales volume
* Negative profit margins
* Poor inventory movement

---

## 💡 Key Insights

* The majority of vendors belong to a stable, revenue-generating segment.
* A small group of vendors exhibits exceptional profitability and inventory efficiency.
* Certain vendors consistently underperform and negatively impact business performance.

---

## 📈 Business Recommendations

### Strategic Vendors

* Maintain long-term partnerships.
* Prioritize inventory allocation.
* Monitor performance regularly.

### High-Margin Growth Vendors

* Increase purchasing volume.
* Expand product assortment.
* Invest in growth opportunities.

### Underperforming Vendors

* Review contracts and pricing strategies.
* Reduce inventory exposure.
* Consider vendor replacement if performance does not improve.

---

## 🌐 Vendor Segmentation Predictor

A Flask-based web application was developed to classify vendors into business segments using the trained K-Means model.

### Input Features

* Vendor Number
* Vendor Name
* Total Sales
* Profit Margin
* Stock Turnover

### Predicted Output

* Strategic Vendor
* High-Margin Growth Vendor
* Underperforming Vendor

---

## 📊 Power BI Dashboard

The Power BI dashboard provides:

* Vendor Performance Overview
* Vendor Segment Distribution
* Sales Analysis by Segment
* Profitability Analysis
* Inventory Turnover Analysis
* Interactive Vendor-Level Drill Down

---

## 📂 Project Structure

```text
Vendor-Segmentation-Project/
├── Report
|
├── notebooks/
│   ├── vendor_analysis_cleaning_and_feature_engineering.ipynb
│   ├── vendor_performance_analysis.ipynb
│   └── vendor_segmentation_ml.ipynb
│
├── dashboard/
│   └── Vendor_Segmentation.pbix
│
├── app/
│   ├── app.py
│   ├── kmeans_vendor_model.pkl
│   ├── vendor_scaler.pkl
│   └── templates/
│       └── index.html
│
├── images/
│   ├── dashboard.png
│   ├── predictor_input.png
│   └── predictor_output.png
│
└── README.md
```

---

## Conclusion

This project successfully demonstrates how Machine Learning can be used to segment vendors based on sales, profitability, and inventory performance. The resulting vendor segments provide actionable business insights that support supplier optimization, profitability improvement, and strategic decision-making.

By combining data analysis, machine learning, business intelligence, and deployment, this project delivers an end-to-end analytics solution suitable for real-world business applications.
