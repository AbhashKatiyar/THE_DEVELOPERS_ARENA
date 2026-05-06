# =========================================================
# E-COMMERCE SALES DATA ANALYSIS & VISUALIZATION PROJECT
# =========================================================

# FEATURES INCLUDED:
# ✔ Complete Data Analysis Pipeline
# ✔ Load Dataset using pandas
# ✔ Data Cleaning & Validation
# ✔ Missing Value Handling
# ✔ Duplicate Removal
# ✔ Revenue Calculation
# ✔ Sales Analysis Metrics
# ✔ 3 Different Chart Types (Bar chart, Pie chart, Line chart)
# ✔ Error Handling
# ✔ Professional Report Formatting
# ✔ Business Insights

# REQUIRED LIBRARIES:
# pip install pandas matplotlib

# ---------------------------------------------------------
# IMPORTING REQUIRED LIBRARIES
# ---------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# FILE CONFIGURATION
# ---------------------------------------------------------

FILE_NAME = "sales_data.csv"

# ---------------------------------------------------------
# LOAD DATASET WITH ERROR HANDLING
# ---------------------------------------------------------

try:
    # Loading the existing CSV file
    df = pd.read_csv(FILE_NAME)

    print("✅ Dataset loaded successfully!\n")

except FileNotFoundError:
    print("❌ ERROR: Dataset file not found.")
    print(f"Please make sure '{FILE_NAME}' exists.")
    exit()

except Exception as e:
    print("❌ Unexpected Error:", e)
    exit()

# ---------------------------------------------------------
# DATA EXPLORATION
# ---------------------------------------------------------

print("=" * 60)
print("📊 DATASET OVERVIEW")
print(df)
print("=" * 60)

# Display first 10 rows
print("\n🔹 FIRST 10 ROWS:\n")
print(df.head(10))

# Dataset shape
print("\n🔹 DATASET SHAPE:")
print(df.shape)

# Column names
print("\n🔹 COLUMN NAMES:")
print(df.columns.tolist())

# Data types
print("\n🔹 DATA TYPES:\n")
print(df.dtypes)

# Missing values
print("\n🔹 MISSING VALUES:\n")
print(df.isnull().sum())

# ---------------------------------------------------------
# DATA CLEANING
# ---------------------------------------------------------

print("\n🧹 CLEANING DATA...\n")

# Removing duplicate rows
df = df.drop_duplicates()

# Handling missing Quantity values
if "Quantity" in df.columns:
    df["Quantity"] = df["Quantity"].fillna(0)

# Handling missing Price values
if "Price" in df.columns:
    df["Price"] = df["Price"].fillna(df["Price"].mean())

# Removing rows where Product is missing
if "Product" in df.columns:
    df = df.dropna(subset=["Product"])

# Handling missing Category values
if "Category" in df.columns:
    df["Category"] = df["Category"].fillna("Unknown")

# Converting OrderDate column to datetime
if "OrderDate" in df.columns:
    df["OrderDate"] = pd.to_datetime(
        df["OrderDate"],
        errors="coerce"
    )

print("✅ Data cleaning completed successfully!\n")

# ---------------------------------------------------------
# CREATE REVENUE COLUMN
# ---------------------------------------------------------

try:
    df["Revenue"] = (df["Quantity"] * df["Price"]).astype(int)

except Exception as e:
    print("❌ Error while calculating Revenue:", e)
    exit()

# ---------------------------------------------------------
# SALES ANALYSIS REPORT
# ---------------------------------------------------------

print("=" * 60)
print("📈 SALES ANALYSIS REPORT")
print("=" * 60)

# Total Revenue
total_revenue = df["Revenue"].sum()

# Total Orders
total_orders = len(df)

# Total Quantity Sold
total_quantity = df["Quantity"].sum()

# Average Order Value
average_order_value = df["Revenue"].mean()

# Best-Selling Product
best_selling_product = (
    df.groupby("Product")["Quantity"]
    .sum()
    .idxmax()
)

# Highest Revenue Product
highest_revenue_product = (
    df.groupby("Product")["Revenue"]
    .sum()
    .idxmax()
)

# Safe Category Analysis
if "Category" in df.columns:

    category_revenue = (
        df.groupby("Category")["Revenue"]
        .sum()
    )

    top_category = category_revenue.idxmax()

else:
    top_category = "{best_selling_product}"

# Display Results
print(f"\n💰 TOTAL REVENUE           : ₹{total_revenue:,.0f}")
print(f"📦 TOTAL ORDERS            : {total_orders}")
print(f"🛒 TOTAL QUANTITY SOLD     : {total_quantity}")
print(f"📊 AVERAGE ORDER VALUE     : ₹{average_order_value:.2f}")
print(f"🏆 BEST-SELLING PRODUCT    : {best_selling_product}")
print(f"🔥 HIGHEST REVENUE PRODUCT : {highest_revenue_product}")
print(f"📂 TOP CATEGORY            : {best_selling_product}")

# ---------------------------------------------------------
# VISUALIZATIONS using CHARTS
# ---------------------------------------------------------

print("\n📊 GENERATING VISUALIZATIONS...\n")

# =========================================================
# CHART 1: BAR CHART
# Product-wise Revenue
# =========================================================

try:

    product_revenue = (
        df.groupby("Product")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 6))

    product_revenue.plot(kind="bar")

    plt.title("Product-wise Revenue")
    plt.xlabel("Products")
    plt.ylabel("Revenue")
    plt.ticklabel_format(style='plain', axis='y')

    plt.xticks(rotation=360)

    for i, value in enumerate(product_revenue):
        plt.text(i, value, f'₹{value:,.0f}', ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

    print("✅ Bar Chart generated successfully!\n")

except Exception as e:
    print("❌ Error generating Bar Chart:", e)

# =========================================================
# CHART 2: PIE CHART
# Product-wise Revenue Distribution
# =========================================================

try:

    product_revenue = (
        df.groupby("Product")["Revenue"].sum())

    # Create labels with revenue values
    labels = [
        f"{product} (₹{revenue:,.0f})"
        for product, revenue in product_revenue.items()]

    # Create Pie Chart
    plt.figure(figsize=(9, 9))

    plt.pie(
        product_revenue,
        labels=labels,
        autopct="%1.1f%%"
    )

    plt.title("Product-wise Revenue Distribution")

    plt.tight_layout()
    plt.show()

    print("✅ Pie Chart generated successfully!\n")

except Exception as e:
    print("❌ Error generating Pie Chart:", e)

# =========================================================
# CHART 3: LINE CHART: Revenue Trend by Product
# =========================================================

try:

    revenue_trend = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values())

    # Create Line Chart
    plt.figure(figsize=(10, 5))

    ax = revenue_trend.plot(kind="line", marker="o")

    plt.title("Revenue Trend by Product")

    plt.xlabel("Product")
    plt.ylabel("Revenue")

    # Show full revenue values on Y-axis
    plt.ticklabel_format(style='plain', axis='y')

    plt.xticks(rotation=45)

    plt.grid(True)

# ---------------------------------------------------------
# DISPLAYING REVENUE VALUES ABOVE DIRECTLY POINTERS
# ---------------------------------------------------------

    for i, value in enumerate(revenue_trend):
        ax.text(i, value, f'₹{value:,.0f}', ha='center', va='bottom')

    plt.tight_layout()
    plt.show()
    print("✅ Line Chart generated successfully!\n")

except Exception as e:
    print("❌ Error generating Line Chart:", e)

# ---------------------------------------------------------
# BUSINESS INSIGHTS
# ---------------------------------------------------------

print("=" * 60)
print("📌 BUSINESS INSIGHTS")
print("=" * 60)

print(f"""
1. The total revenue generated from the dataset is ₹{total_revenue:.2f}.

2. '{best_selling_product}' is the best-selling product based on quantity sold.

3. '{highest_revenue_product}' generates the highest revenue for the business.

4. The average order value is ₹{average_order_value:.2f}, indicating customer spending behavior.

5. '{best_selling_product}' is the highest-performing category based on revenue analysis.

6. The bar chart helps compare revenue generated by different products.

7. The pie chart clearly shows the revenue contribution of each product.

8. The line chart helps identify product revenue trends and performance patterns.

9. These insights can help businesses improve marketing, inventory management, and sales strategies.
""")

# ---------------------------------------------------------
# FINAL MESSAGE
# ---------------------------------------------------------

print("=" * 60)
print("✅ E-COMMERCE SALES ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)
