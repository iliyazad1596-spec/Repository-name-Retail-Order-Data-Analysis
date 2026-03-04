# 📊 Retail Order Data Analysis Dashboard

## Project Overview
This project performs an end-to-end analysis of retail order data to extract business insights related to revenue generation, product performance, profitability, and regional sales distribution.

The project includes data cleaning using Python, SQL-based analytical queries, and an interactive business intelligence dashboard built using Streamlit.

---

## Tools & Technologies Used
- Python (Pandas)
- MySQL
- Streamlit
- Plotly
- Kaggle Dataset

---

## Project Workflow

### 1. Data Collection
The dataset was obtained from Kaggle containing retail order transactions including product category, pricing details, discounts, and order dates.

### 2. Data Cleaning (Python)
The dataset was cleaned using Pandas by:
- Standardizing column names
- Converting discount percentages
- Creating `sale_price` column
- Calculating `profit`
- Formatting date columns

### 3. SQL Data Analysis
20 SQL queries were written to analyze:

- Total Revenue
- Total Profit
- Revenue by Category
- Profit by Category
- Revenue by Region
- Top Performing Products
- Profit Margin Analysis
- Monthly and Yearly Revenue Trends

### 4. Dashboard Development
An interactive **Streamlit dashboard** was developed to visualize the results.

Dashboard Features:
- Region filter
- Year filter
- KPI metrics (Revenue, Profit, Profit Margin)
- Category revenue distribution
- Region sales performance
- Top product analysis
- Revenue trend visualization

---

## Key Insights
- Technology category generates the highest revenue.
- West region contributes the most to total sales.
- Certain products significantly dominate total revenue.
- Revenue trend shows steady growth between 2022 and 2023.

---
## Project Structure

```
Retail_Order_Data_Analysis/
│
├── app.py
├── cleaned_orders.csv
├── SQL_Queries.sql
├── Retail_Order_Data_Analysis_GUVI_Report_Compact.pdf
├── requirements.txt
└── README.md
```

## Author
**Iliyaz Ahamed**  
Data Science Batch: MDTM38[DS-S-WD-T-B33]

---
## Future Improvements

- Deploy the Streamlit dashboard online.
- Add machine learning models for sales prediction.
- Implement automated ETL pipeline for real-time data updates.
- Create customer segmentation analysis.
- Add more advanced business KPI visualizations.
