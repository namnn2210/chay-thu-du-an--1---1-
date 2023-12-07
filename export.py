import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('a.xlsx')

total_sold_by_product_df = df.drop(columns=['Thành tiền', 'Thời gian', 'Khách hàng', 'SĐT']).sort_values('Số lượng', ascending=False)
total_sold_by_product_df = total_sold_by_product_df.groupby('Tên sản phẩm')['Số lượng'].sum().sort_values(ascending=False).head(10).reset_index()
print(total_sold_by_product_df)
# Create a bar chart
plt.figure(figsize=(12, 6))
plt.bar(total_sold_by_product_df['Tên sản phẩm'], total_sold_by_product_df['Số lượng'])

# Add titles and labels
plt.title('Top 10 Best Selling Products')
plt.xlabel('Product Name')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=45)

# Show the plot
plt.show()