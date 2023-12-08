import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('banhang.xlsx')
product_data = pd.read_excel('CSDL_MON.xlsx')

# -------------------------------------------------------------------------------------
# total_sold_by_product_df = df.drop(columns=[
#                                    'Thành tiền', 'Thời gian', 'Khách hàng', 'SĐT']).sort_values('Số lượng', ascending=False)
# total_sold_by_product_df = total_sold_by_product_df.groupby(
#     'Tên sản phẩm')['Số lượng'].sum().sort_values(ascending=False).head(10).reset_index()
# print(total_sold_by_product_df)
# # Create a bar chart
# plt.figure(figsize=(12, 6))
# plt.bar(total_sold_by_product_df['Tên sản phẩm'],
#         total_sold_by_product_df['Số lượng'])

# # Add titles and labels
# plt.title('Top 10 sản phẩm bán chạy nhất')
# plt.xlabel('Tên sản phảm')
# plt.ylabel('Tổng số lượng bán được')
# plt.xticks(rotation=45)

# # Show the plot
# plt.show()
# plt.savefig('chart1.png', bbox_inches='tight')
# total_sold_by_product_df.to_excel('chart1.xlsx', index=False)

# -------------------------------------------------------------------------------------

# product_revenue = df.groupby('Tên sản phẩm')['Thành tiền'].sum()

# # Sorting the products by total revenue in descending order
# product_revenue_sorted = product_revenue.sort_values(ascending=False)

# # Selecting the product with the highest total sales value
# top_product_revenue = product_revenue_sorted.head(1)

# # Plotting the bar chart for the product with the highest total sales value
# plt.figure(figsize=(6, 4))
# plt.bar(top_product_revenue.index, top_product_revenue, color='blue')
# plt.xlabel('Tên sản phẩm')
# plt.ylabel('Tổng giá trị bán hàng (VND)')
# plt.title('Sản phẩm có tổng giá trị bán hàng cao nhất')
# plt.grid(axis='y')

# # Formatting the y-axis to display full revenue values
# plt.gca().get_yaxis().set_major_formatter(
#     plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

# # Display the plot
# plt.show()
# product_revenue_df = product_revenue_sorted.reset_index()
# product_revenue_df.columns = ['Tên sản phẩm', 'Tổng giá trị bán hàng']
# product_revenue_df.to_excel('chart2.xlsx', index=False)
# -------------------------------------------------------------------------------------

# Grouping by customer's phone number and summing their total purchase value
# customer_purchase = df.groupby('SĐT')['Thành tiền'].sum()

# # Sorting the customers by total purchase value in descending order
# customer_purchase_sorted = customer_purchase.sort_values(ascending=False)

# # Creating a new DataFrame with phone numbers and their total purchase value
# customer_purchase_df = customer_purchase_sorted.reset_index()
# customer_purchase_df.columns = ['SĐT', 'Tổng giá trị mua hàng']

# # Displaying the new DataFrame
# customer_purchase_df.head()
# customer_purchase_df.to_excel('chart2.xlsx', index=False)

# -------------------------------------------------------------------------------------

df['Thời gian'] = pd.to_datetime(df['Thời gian'])
df['Giờ'] = df['Thời gian'].dt.hour

# data_hours = df[(df['Giờ'] >= 6) & (df['Giờ'] <= 22)]

# # Grouping by hour and summing the total sales value
# hourly_sales = data_hours.groupby('Giờ')['Thành tiền'].sum()

# # Sorting the hourly sales in descending order
# hourly_sales_sorted = hourly_sales.sort_values(ascending=False)

# # Plotting the bar chart for sales revenue by hour from 6 AM to 10 PM
# plt.figure(figsize=(12, 6))
# plt.bar(hourly_sales.index, hourly_sales, color='orange')
# plt.xlabel('Giờ trong ngày')
# plt.ylabel('Doanh thu (VND)')
# plt.title('Doanh thu theo giờ từ 6h sáng đến 10h tối')
# # Setting x-ticks for every hour from 6 AM to 10 PM
# plt.xticks(np.arange(6, 23, 1))
# plt.grid(axis='y')

# # Formatting the y-axis to display full revenue values
# plt.gca().get_yaxis().set_major_formatter(
#     plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

# # Display the plot
# plt.show()
# hourly_sales_sorted_df = hourly_sales_sorted.reset_index()
# # hourly_sales_sorted_df.columns = ['SĐT', 'Tổng giá trị mua hàng']
# hourly_sales_sorted_df.to_excel('chart2.xlsx', index=False)

# print(hourly_sales_sorted_df.head())

# -------------------------------------------------------------------------------------

# df['Thời gian'] = pd.to_datetime(df['Thời gian'])
# df['Giờ'] = df['Thời gian'].dt.hour
# data_morning = df[(df['Giờ'] >= 6) & (df['Giờ'] < 8)]

# morning_product_sales = data_morning.groupby('Tên sản phẩm')['Số lượng'].sum()

# morning_product_sales_sorted = morning_product_sales.sort_values(
#     ascending=False)
# morning_product_sales_sorted_df = morning_product_sales_sorted.reset_index()
# morning_product_sales_sorted_df.to_excel('chart2.xlsx', index=False)

# -------------------------------------------------------------------------------------

# df['Thời gian'] = pd.to_datetime(df['Thời gian'])
# df['Giờ'] = df['Thời gian'].dt.hour
# data_evening = df[(df['Giờ'] >= 16) & (df['Giờ'] < 19)]

# evening_product_sales = data_evening.groupby('Tên sản phẩm')['Số lượng'].sum()
# evening_product_sales_sorted = evening_product_sales.sort_values(
#     ascending=False)

# evening_product_sales_sorted = evening_product_sales.reset_index()
# evening_product_sales_sorted.to_excel('chart2.xlsx', index=False)
# print(evening_product_sales_sorted.head())

# -------------------------------------------------------------------------------------

# product_name_to_code = {
#     'Donut': 'DN001',
#     'Cupcake': 'CCK001',
#     'Macaron': 'MCR001',
#     'Crepe': 'CR001',
#     'Su Kem': 'SK001',
#     'Red Velvet': 'RV001',
#     'Panna Cotta': 'PNCT001',
#     'Cookies': 'CK001',
#     'Tiramisu': 'TRMS001'
# }

# # Mapping product names in the sales data to their product codes
# df['Mã SP'] = df['Tên sản phẩm'].map(product_name_to_code)

# # Extracting the product group code from the sales data
# df['Nhóm sản phẩm'] = df['Mã SP'].str[:2]

# # Grouping by product group and summing the total sales value
# group_sales = df.groupby('Nhóm sản phẩm')['Thành tiền'].sum()

# # Sorting the group sales in alphabetical order of the product group code
# group_sales_sorted = group_sales.sort_index()

# # Plotting the bar chart for sales revenue by product group
# plt.figure(figsize=(10, 6))
# plt.bar(group_sales_sorted.index, group_sales_sorted, color='cyan')
# plt.xlabel('Nhóm sản phẩm')
# plt.ylabel('Doanh thu (VND)')
# plt.title('Doanh thu theo nhóm sản phẩm')
# plt.grid(axis='y')

# # Formatting the y-axis to display full revenue values
# plt.gca().get_yaxis().set_major_formatter(
#     plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

# # Display the plot
# plt.show()
# group_sales_sorted.reset_index().to_excel('chart2.xlsx', index=False)


# -------------------------------------------------------------------------------------

# product_name_to_code = {
#     'Donut': 'DN001',
#     'Cupcake': 'CCK001',
#     'Macaron': 'MCR001',
#     'Crepe': 'CR001',
#     'Su Kem': 'SK001',
#     'Red Velvet': 'RV001',
#     'Panna Cotta': 'PNCT001',
#     'Cookies': 'CK001',
#     'Tiramisu': 'TRMS001'
# }

# df['Mã SP'] = df['Tên sản phẩm'].map(product_name_to_code)
# df['Nhóm sản phẩm'] = df['Mã SP'].str[:2]
# # Grouping data by product group and product name, then summing the total sales value
# group_product_sales = df.groupby(['Nhóm sản phẩm', 'Tên sản phẩm'])[
#     'Thành tiền'].sum()

# # Getting unique product groups
# unique_product_groups = group_product_sales.index.get_level_values(0).unique()

# # Plotting pie charts for each product group
# fig, axes = plt.subplots(len(unique_product_groups), 1,
#                          figsize=(10, 6 * len(unique_product_groups)))
# fig.tight_layout(pad=6.0)

# for i, group in enumerate(unique_product_groups):
#     # Selecting data for the specific product group
#     group_data = group_product_sales[group].sort_values(ascending=False)

#     # Plotting the pie chart
#     axes[i].pie(group_data, labels=group_data.index,
#                 autopct='%1.1f%%', startangle=140)
#     axes[i].set_title(f'Doanh thu của các sản phẩm trong nhóm {group}')

# # Show the plot
# plt.show()
# group_sales_sorted.reset_index().to_excel('chart2.xlsx', index=False)

# -------------------------------------------------------------------------------------

# Re-extracting the hour from the 'Thời gian' column
df['Thời gian'] = pd.to_datetime(df['Thời gian'])
df['Giờ'] = df['Thời gian'].dt.hour

# Grouping by product name and hour, then summing the quantity sold
product_hourly_sales = df.groupby(['Tên sản phẩm', 'Giờ'])[
    'Số lượng'].sum().unstack(fill_value=0)

# Plotting the bar chart for hourly sales of each product
product_hourly_sales.plot(kind='bar', figsize=(15, 8), stacked=True)

plt.xlabel('Tên sản phẩm')
plt.ylabel('Số lượng bán ra')
plt.title('Doanh số theo giờ của từng sản phẩm')
plt.legend(title='Giờ trong ngày', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Display the plot
plt.show()
product_hourly_sales.reset_index().to_excel('chart2.xlsx', index=False)
