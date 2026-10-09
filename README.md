# ecommerce-data-cleaning
E-commerce data cleaning and preprocessing using Python and Pandas
# E-Commerce Data Cleaning Project

## Project Overview

This project demonstrates data cleaning and preprocessing using Python and Pandas.

The goal is to clean raw e-commerce order data and prepare it for further analysis.

## Dataset

The dataset contains information about:

- Order ID
- Customer Name
- Age
- City
- Product
- Price
- Quantity
- Order Date

## Data Cleaning Performed

The following cleaning steps were performed:

1. Loaded the raw CSV dataset.
2. Inspected the dataset structure.
3. Identified missing values.
4. Handled missing Age values using the median.
5. Identified duplicate records.
6. Removed duplicate records.
7. Standardized city names.
8. Converted Order Date into datetime format.
9. Created a Total Amount column.
10. Validated the cleaned dataset.
11. Exported the cleaned dataset.

## Technologies Used

- Python
- Pandas
- GitHub Codespaces

## Project Structure

```text
ecommerce-data-cleaning/
│
├── data/
│   ├── ecommerce_data.csv
│   └── cleaned_ecommerce_data.csv
│
├── src/
│   └── data_cleaning.py
│
├── README.md
└── requirements.txt