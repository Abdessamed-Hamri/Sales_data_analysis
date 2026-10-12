from utils.helpers import clean_lines, parse_products
from utils.product import Product
with open("../data/raw/data.txt", "r") as file:
     lines = file.readlines()

lines = clean_lines(lines)
products_data = parse_products(lines)

products = []
for item in products_data:
    product = Product(item[0], item[1], item[2])
    products.append(product)

total_sales = 0

for product in products:
    value = product.total_value()
    print(product.name, value)
    total_sales += value

print("total sales:", total_sales)




