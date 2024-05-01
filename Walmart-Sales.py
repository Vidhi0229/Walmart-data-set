import pandas as pd

file = "Walmart_Sales.xlsx"
sales_data = pd.read_excel(file)

# A. Analyze the performance of sales and revenue at the city and branch level

sales_data['Total revenue'] = sales_data['Unit price'] * sales_data['Quantity']

total_quantity = sales_data['Quantity'].sum()

performance = sales_data.groupby(['City', 'Branch']).agg({'Quantity': 'sum','Total revenue': 'sum'})
performance.columns = ['Total Quantity', 'Total Revenue']  
print("\nPerformance of sales and revenue at the city and branch level:\n", performance)

# B. What is the average price of an item sold at each branch of the city 
average_price = sales_data.groupby(['City', 'Branch'])['Unit price'].mean()
print("\nAverage Price\n", average_price)


# C. Analyze the performance of sales and revenue, Month over Month across the Product line, Gender, and Payment Method, and identify the focus areas to get better sales for April 2019. 
sales_data['Date'] = pd.to_datetime(sales_data['Date'])

def monthly_performance_analysis(sales_data, year):
    for month in range(1, 4):
        month_data = sales_data[(sales_data['Date'].dt.year == year) & (sales_data['Date'].dt.month == month)]
        monthly_performance = month_data.groupby(['Product line', 'Gender', 'Payment']).agg({'Quantity': 'sum', 'Total revenue': 'sum'})
        print(f"\nPerformance analysis for {month}/{year}:")
        print(monthly_performance)


monthly_performance_analysis(sales_data, 2019)


def overall_performance_analysis(sales_data):
    overall_performance = sales_data.groupby(['Product line', 'Gender', 'Payment']).agg({'Quantity': 'sum', 'Total revenue': 'sum'})
    print("Overall Performance Analysis:")
    print(overall_performance)

    focus_areas = overall_performance[overall_performance['Quantity'] < overall_performance['Quantity'].mean()]
    if not focus_areas.empty:
        print("\nFocus Areas for Improvement:")
        print(focus_areas)


overall_performance_analysis(sales_data)

