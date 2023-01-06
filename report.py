from plugins.send_to_slack import send_to_slack
from plugins.transform.read_transform import append_all_files
import matplotlib.pyplot as plt

file_bytes = '/mnt/f/DigitalSkola/2.Project_1/automate_report/output/sales_per_month.png'

# analyze and create graph
data_product = append_all_files(
    '/mnt/f/DigitalSkola/2.Project_1/automate_report/data/sales_product_data/Sales_December_2019.csv')

# transform

data_product.drop(
    data_product[data_product['Quantity Ordered'] == "Quantity Ordered"].index, inplace=True)


data_product['total_price'] = data_product['Quantity Ordered'].astype(
    float) * data_product['Price Each'].astype(float)/1000

data_transformed = data_product.groupby('Product').agg({'total_price':'sum'}).reset_index().nlargest(3,'total_price')
data_transformed1 = data_product.groupby('Product').agg({'total_price':'sum'}).reset_index().nsmallest(3,'total_price')


print(data_transformed)

fig, ax = plt.subplots(2)

ax[0].bar(data_transformed ['Product'], data_transformed['total_price'])
ax[0].set_xlabel('Product',loc=('right'))
ax[0].set_ylabel('Total Sales (USD)',loc=('top'))

ax[0].set_title('Top 3 Penjualan')

ax[1].bar(data_transformed1 ['Product'], data_transformed1['total_price'])
ax[1].set_xlabel('Product',loc=('right'))
ax[1].set_ylabel('Total Sales (USD)',loc=('top'))
ax[1].set_title('Bottom 3 Penjualan')



fig.set_size_inches(8,8)

fig.savefig(file_bytes,dpi=220)

send_to_slack.execute('Report Hari Ini', '#automate_report', file_bytes)
