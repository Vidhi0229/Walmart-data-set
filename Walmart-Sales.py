import pandas as pd

file = "Walmart_Sales.xlsx"
sales_data = pd.read_excel(file)

csv_file = "Walmart_Sales.csv"
sales_data.to_csv(csv_file, index=False)


sales_csv = pd.read_csv(csv_file)

# A. Analyze the performance of sales and revenue at the city and branch level
sales_data['Total'] = sales_data['Unit price'] * sales_data['Quantity']
performance = sales_data.groupby(['City', 'Branch']).agg({'Total': 'sum'})
print(performance)

# B. What is the average price of an item sold at each branch of the city (10 marks)
average_price = sales_data.groupby(['City', 'Branch'])['Unit price'].mean()
print("\nAverage Data\n", average_price)

# C. Analyze the performance of sales and revenue, Month over Month across the Product line, Gender, and Payment Method, and identify the focus areas to get better sales for April 2019. 
sales_data['Date'] = pd.to_datetime(sales_data['Date'])

april_data = sales_data[(sales_data['Date'].dt.month == 4) & (sales_data['Date'].dt.year == 2019)]

ap_data = april_data.groupby(['Product line', 'Gender', 'Payment']).agg({'Total': 'sum'}).reset_index()

ap_data['Revenue'] = ap_data['Total'] * 0.1  # Assuming a revenue rate of 10% for simplicity

print("\nApril Data\n", ap_data)