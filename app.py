import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Retail Order BI Dashboard",
    layout="wide"
)

# ================= DARK THEME STYLE =================
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ================= CONNECT TO MYSQL =================
@st.cache_data
def load_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="retaildb"
    )
    query = "SELECT * FROM cleaned_orders1"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

df = load_data()

df["order_date"] = pd.to_datetime(df["order_date"])
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month

# ================= SIDEBAR =================
st.sidebar.title("📊 Filters")

selected_region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + sorted(df["region"].unique())
)

selected_year = st.sidebar.selectbox(
    "Select Year",
    ["All"] + sorted(df["year"].unique())
)

filtered_df = df.copy()

if selected_region != "All":
    filtered_df = filtered_df[filtered_df["region"] == selected_region]

if selected_year != "All":
    filtered_df = filtered_df[filtered_df["year"] == selected_year]

# ================= SIDEBAR KPIs =================
st.sidebar.markdown("### 🔎 Quick KPIs")

total_revenue = filtered_df["sale_price"].sum()
total_profit = filtered_df["profit"].sum()
profit_margin = (total_profit / total_revenue) * 100 if total_revenue != 0 else 0

st.sidebar.metric("Revenue", f"${total_revenue:,.0f}")
st.sidebar.metric("Profit", f"${total_profit:,.0f}")
st.sidebar.metric("Profit %", f"{profit_margin:.2f}%")

# ================= TITLE =================
st.title("📊 Retail Business Intelligence Dashboard")

# ================= MAIN KPIs =================
col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Profit Margin %", f"{profit_margin:.2f}%")

st.divider()

# ================= CATEGORY ANALYSIS =================
st.subheader("📦 Category Performance")

category_data = filtered_df.groupby("category").agg({
    "sale_price": "sum",
    "profit": "sum"
}).reset_index()

category_data["profit_margin"] = (
    category_data["profit"] / category_data["sale_price"]
) * 100

col1, col2 = st.columns(2)

# Pie Chart - Revenue Share
with col1:
    fig1 = px.pie(
        category_data,
        values="sale_price",
        names="category",
        title="Revenue Share by Category"
    )
    st.plotly_chart(fig1, use_container_width=True)

# Profit Margin Bar with Conditional Coloring
with col2:
    fig2 = px.bar(
        category_data,
        x="category",
        y="profit_margin",
        title="Profit Margin by Category",
        color="profit_margin",
        color_continuous_scale="RdYlGn"
    )
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ================= REGION ANALYSIS =================
st.subheader("🌍 Region Performance")

region_data = filtered_df.groupby("region")["sale_price"].sum().reset_index()

fig3 = px.bar(
    region_data,
    x="region",
    y="sale_price",
    title="Revenue by Region",
    color="sale_price",
    color_continuous_scale="Blues"
)

st.plotly_chart(fig3, use_container_width=True)

st.divider()

# ================= PRODUCT ANALYSIS =================
st.subheader("🏆 Top 10 Products by Revenue")

top_products = (
    filtered_df.groupby("product_id")["sale_price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig4 = px.bar(
    top_products,
    x="product_id",
    y="sale_price",
    title="Top 10 Revenue Products",
    color="sale_price",
    color_continuous_scale="Viridis"
)

st.plotly_chart(fig4, use_container_width=True)

st.divider()

# ================= TIME ANALYSIS =================
st.subheader("📅 Revenue Trend")

yearly_data = filtered_df.groupby("year")["sale_price"].sum().reset_index()

fig5 = px.line(
    yearly_data,
    x="year",
    y="sale_price",
    markers=True,
    title="Year-wise Revenue Trend"
)

st.plotly_chart(fig5, use_container_width=True)

st.divider()

# ================= DOWNLOAD BUTTON =================
st.subheader("⬇ Download Filtered Data")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="filtered_retail_data.csv",
    mime="text/csv",
)

st.success("Dashboard Loaded Successfully 🚀")