
USE retaildb;

-- 1: Total Revenue
SELECT SUM(sale_price) AS total_revenue
FROM cleaned_orders1;

-- 2: Total Profit
SELECT SUM(profit) AS total_profit
FROM cleaned_orders1;

-- 3: Total Orders
SELECT COUNT(*) AS total_orders
FROM cleaned_orders1;

-- 4: Revenue by Category
SELECT category,
       SUM(sale_price) AS total_revenue
FROM cleaned_orders1
GROUP BY category
ORDER BY total_revenue DESC;

-- 5: Profit by Category
SELECT category,
       SUM(profit) AS total_profit
FROM cleaned_orders1
GROUP BY category
ORDER BY total_profit DESC;

-- 6: Average Discount by Category
SELECT category,
       AVG(discount_percent) AS avg_discount
FROM cleaned_orders1
GROUP BY category;

-- 7: Revenue by Region
SELECT region,
       SUM(sale_price) AS total_revenue
FROM cleaned_orders1
GROUP BY region
ORDER BY total_revenue DESC;

-- 8: Profit by Region
SELECT region,
       SUM(profit) AS total_profit
FROM cleaned_orders1
GROUP BY region
ORDER BY total_profit DESC;

-- 9: Average Discount by Region
SELECT region,
       AVG(discount_percent) AS avg_discount
FROM cleaned_orders1
GROUP BY region;

-- 10: Top 10 Products by Revenue
SELECT product_id,
       SUM(sale_price) AS total_revenue
FROM cleaned_orders1
GROUP BY product_id
ORDER BY total_revenue DESC
LIMIT 10;

-- 11: Top 5 Products by Profit
SELECT product_id,
       SUM(profit) AS total_profit
FROM cleaned_orders1
GROUP BY product_id
ORDER BY total_profit DESC
LIMIT 5;

-- 12: Products with High Discount (>20%)
SELECT product_id,
       discount_percent
FROM cleaned_orders1
WHERE discount_percent > 0.20;

-- 13: Revenue by Year
SELECT YEAR(order_date) AS year,
       SUM(sale_price) AS total_revenue
FROM cleaned_orders1
GROUP BY year
ORDER BY year;

-- 14: Profit by Year
SELECT YEAR(order_date) AS year,
       SUM(profit) AS total_profit
FROM cleaned_orders1
GROUP BY year
ORDER BY year;

-- 15: Revenue by Month
SELECT MONTH(order_date) AS month,
       SUM(sale_price) AS monthly_revenue
FROM cleaned_orders1
GROUP BY month
ORDER BY month;

-- 16: Profit Margin by Category
SELECT category,
       (SUM(profit) / SUM(sale_price)) * 100 AS profit_margin_percent
FROM cleaned_orders1
GROUP BY category;

-- 17: Segment-wise Quantity Sold
SELECT segment,
       SUM(quantity) AS total_quantity
FROM cleaned_orders1
GROUP BY segment
ORDER BY total_quantity DESC;

-- 18: Most Profitable Month
SELECT MONTH(order_date) AS month,
       SUM(profit) AS total_profit
FROM cleaned_orders1
GROUP BY month
ORDER BY total_profit DESC
LIMIT 1;

-- 19: Region with Highest Average Sale Price
SELECT region,
       AVG(sale_price) AS avg_sale_price
FROM cleaned_orders1
GROUP BY region
ORDER BY avg_sale_price DESC
LIMIT 1;

-- 20: Ranking Products by Revenue
SELECT product_id,
       SUM(sale_price) AS total_revenue,
       RANK() OVER (ORDER BY SUM(sale_price) DESC) AS revenue_rank
FROM cleaned_orders1
GROUP BY product_id;