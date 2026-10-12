def clean_lines(list):
    clean_list = []
    for string in list:
        line = string.strip()
        if line.strip():
            clean_list.append(line)

    return clean_list

def clean_lines_comr(list):
    clean_list = [string.strip() for string in list if string.strip() != ""]

    return clean_list

lines = ["Laptop,1000,3", " ", "Phone,500,5", "\n", "Tablet,700,2"]
print(clean_lines_comr(lines))

def parse_products(lines):
    new_list = []

    for line in lines:
        parts = line.split(",")

        name = parts[0].strip()
        price = float(parts[1])
        quantity = int(parts[2])

        product = (name, price, quantity)
        new_list.append(product)

    return new_list
print(parse_products(clean_lines_comr(lines)))
