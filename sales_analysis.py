# =================================================
# Sales Data Analysis Project in 5 Days Roadmap
# =================================================

# Import pandas library
import pandas as pd

# ------------------------------------------
# DAY 1 PROGRESS: Loading CSV File
# ------------------------------------------

file_name = "sales_data.csv"

try:
    # Load dataset
    df = pd.read_csv(file_name)

    print("✅ Dataset loaded successfully!\n")

except FileNotFoundError:
    print("❌ File not found!")
    print("Please make sure 'sales_data.csv' is in the same folder.\n")
    exit()

# ------------------------------------------
# DAY 2 PROGRESS: Exploring The Sales Dataset
# ------------------------------------------

print("📊 FIRST 5 ROWS OF DATA USING DEFAULT HEAD() FUNCTION:\n")
print(df.head())

print("📊 FIRST CUSTOM ROWS OF DATA USING HEAD(NO. OF ROWS) FUNCTION:\n")
print(df.head(25))

print("📊 LAST CUSTOM ROWS OF DATA USING TAIL(NO. OF ROWS) FUNCTION:\n")
print(df.tail(25))

# CHECKING THE SHAPE (ROWS, COLUMNS) OF THE DATASET
print("\n📏 Dataset Shape:")
print(df.shape)

# CHECKING THE COLUMN NAMES IN THE DATASET
print("\n📌 Column Names:")
print(df.columns)

# CHECKING THE DATA TYPES OF EACH COLUMN
print("\n🔍 Data Types:")
print(df.dtypes)

# ------------------------------------------
# DAY 3 PROGRESS: Handling Missing Values
# ------------------------------------------

# CHECKING FOR MISSING VALUES IN EACH COLUMN
print("\n🧹 Checking Missing Values:\n")
print(df.isnull().sum())

# Filling missing quantity with 0
df["Quantity"] = df["Quantity"].fillna(0)

# Filling missing price with average price
df["Price"] = df["Price"].fillna(df["Price"].mean())

# Removing rows where Product Name is missing
df = df.dropna(subset=["Product"])

# Removing duplicate rows
df = df.drop_duplicates()

# Final check for missing values and duplicates
print("\n🧹 Final Check After Handling Missing Values and Duplicates:\n")
print(df.isnull().sum())
print(f"\n✅ Missing values handled and duplicates removed.\n")

# ------------------------------------------
# DAY 4 PROGRESS: Sales Analysis
# ------------------------------------------

# Creating new column: Revenue = Quantity × Price
df["Revenue"] = df["Quantity"] * df["Price"]

# Metric 1: Total Sales Revenue
total_sales = df["Revenue"].sum()

# Metric 2: Total Quantity Sold
total_quantity = df["Quantity"].sum()

# Metric 3: Average Sales Revenue
average_sales = df["Revenue"].mean()

# Metric 4: Best-Selling Product (highest quantity sold)
best_selling_product = (
    df.groupby("Product")["Quantity"]
    .sum()
    .idxmax()
)

# Metric 5: Highest Revenue Product
highest_revenue_product = (
    df.groupby("Product")["Revenue"]
    .sum()
    .idxmax()
)

# ------------------------------------------
# DAY 5 PROGRESS: Generating Final Clean Report
# ------------------------------------------

print("=" * 60)
print("\t\t📈 SALES ANALYSIS REPORT")
print("=" * 60)

print(f"💰 Total Sales Revenue      : ₹{total_sales:.2f}")
print(f"📦 Total Quantity Sold      : {total_quantity}")
print(f"📊 Average Sales Revenue    : ₹{average_sales:.2f}")
print(f"🏆 Best-Selling Product     : {best_selling_product}")
print(f"🔥 Highest Revenue Product  : {highest_revenue_product}")

print("=" * 60)

print("\n✅ Report Generated Successfully!")
print("Insights:")
print(f"1. The total sales revenue is ₹{total_sales:.2f}, indicating the overall performance of the sales.")
print(f"2. A total of {total_quantity} units were sold, showing the demand for the products.")
print(f"3. The average sales revenue per transaction is ₹{average_sales:.2f}, which can help in understanding the typical sale value.")
print(f"4. The best-selling product is '{best_selling_product}', which is the most popular item among customers.")
print(f"5. The highest revenue product is '{highest_revenue_product}', which contributes the most to total sales.")

print("\n✅ Analysis Complete!")
