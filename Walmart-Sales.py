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
