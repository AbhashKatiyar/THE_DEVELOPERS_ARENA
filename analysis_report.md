# Sales Data Analysis Report

## Project Title
Sales Data Analysis using Python and Pandas

## Project Overview

This project is designed to analyze a simple sales dataset using Python and the pandas library. The main goal is to calculate important sales metrics such as total sales revenue, total quantity sold, average sales revenue, best-selling product, and highest revenue-generating product.

The project also includes data cleaning techniques like handling missing values and removing duplicate entries to ensure accurate analysis.

This project helps in understanding how real-world sales data can be processed and analyzed efficiently using Python.

## Objectives

- Load and analyze sales data using pandas
- Handle missing values appropriately
- Remove duplicate records
- Calculate multiple sales performance metrics
- Identify the best-selling product
- Generate a clean and formatted report
- Improve understanding of data analysis using Python

## Technologies Used

- Python
- Pandas Library
- CSV File Handling
- Visual Studio Code

## Project Files

SalesDataAnalysis/
│
├── main.py
├── sales_data.csv
├── requirements.txt
├── README.md
└── analysis_report.md

## Dataset Description

The dataset contains the following columns:

| Column Name | Description |
|---|---|
|Date|Stores the date of sale of the product|,
|Product|Contains the Product Type|,
|Quantity|Specifies the Quantity Sold|,
|Price|Displays the Price per unit Item|,
|Customer_ID|Shows the CustomerID for each Sale Made|,
|Region|Depicts the Region of Sale|,
|Total_Sales|Totalvalue of the entire sale|

## Setup Instructions
### Step 1: Install Python
Download and install Python from the official website.
Make sure to enable:
Add Python to PATH

### Step 2: Install pandas
Open terminal where the files are stored and run:
pip install pandas
Then run in the same Terminal window:
python main.py

### Working of the main.py file
It performs the following tasks:

1. Loads CSV file using pandas
2. Displays dataset preview
3. Checks shape and columns
4. Handles missing values
5. Removes duplicate records
6. Calculates sales metrics
7. Generates final report along with project insights

### Metrics Calculated
1. Total Sales Revenue
2. Total Quantity Sold
3. Average Sales Revenue
4. Best-Selling Product
5. Highest Revenue Product

### Final Report Generated

============================================================
                📈 SALES ANALYSIS REPORT
============================================================
💰 Total Sales Revenue      : ₹12365048.00
📦 Total Quantity Sold      : 478
📊 Average Sales Revenue    : ₹123650.48
🏆 Best-Selling Product     : Laptop
🔥 Highest Revenue Product  : Laptop
============================================================
