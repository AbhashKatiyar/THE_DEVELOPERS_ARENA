# ==========================================
# Charts for Sales Data Insights
# ==========================================
# This code creates charts for:
# 1. Product-wise Total Quantity Sold
# 2. Product-wise Total Revenue
# 3. Sales Distribution
#
# Required Libraries:
# pip install pandas matplotlib
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------
# STEP 1: Load Dataset
# ------------------------------------------

file_name = "sales_data.csv"

try:
    df = pd.read_csv(file_name)
    print("✅ Dataset loaded successfully!\n")

except FileNotFoundError:
    print("❌ File not found!")
    print("Please make sure 'sales_data.csv' is in the same folder.")
    exit()

# ------------------------------------------
# STEP 2: Handle Missing Values
# ------------------------------------------

# Fill missing Quantity with 0
df["Quantity"] = df["Quantity"].fillna(0)

# Fill missing Price with average price
df["Price"] = df["Price"].fillna(df["Price"].mean())

# Remove rows where Product is missing
df = df.dropna(subset=["Product"])

# Remove duplicates
df = df.drop_duplicates()

# ------------------------------------------
# STEP 3: Create Revenue Column
# ------------------------------------------

df["Revenue"] = df["Quantity"] * df["Price"]

# ------------------------------------------
# STEP 4: Group Data for Analysis
# ------------------------------------------

# Product-wise total quantity sold
product_quantity = df.groupby("Product")["Quantity"].sum()

# Product-wise total revenue
product_revenue = df.groupby("Product")["Revenue"].sum()

# ------------------------------------------
# CHART 1: Bar Chart - Quantity Sold
# ------------------------------------------

plt.figure(figsize=(8, 5))
product_quantity.plot(kind="bar")

plt.title("Product-wise Total Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Total Quantity")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# ------------------------------------------
# CHART 2: Bar Chart - Revenue Generated
# ------------------------------------------

plt.figure(figsize=(8, 5))
product_revenue.plot(kind="bar")

plt.title("Product-wise Total Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
# plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# ------------------------------------------
# CHART 3: Pie Chart - Revenue Distribution
# ------------------------------------------

plt.figure(figsize=(7, 7))
product_revenue.plot(kind="pie", autopct="%1.1f%%")

plt.title("Revenue Distribution by Product")
plt.ylabel("")

plt.tight_layout()
plt.show()

# ------------------------------------------
# Final Message
# ------------------------------------------

print("📊 Charts generated successfully!")