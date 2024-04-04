from faker import Faker

faker = Faker('en_US')

product_entries = []

for _ in range(100):
    product_code = faker.unique.bothify(text='PROD-########', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    product_name = faker.catch_phrase()
    category = faker.word()[:50]  # To ensure the generated word fits into the CATEGORY column length
    brand = faker.company()[:50]  # To ensure the generated company name fits into the BRAND column length
    price = round(faker.pydecimal(left_digits=8, right_digits=2, positive=True), 2)

    product_entries.append((product_code, product_name, category, brand, price))

# Starting the SQL insertion script creation with one INSERT statement.
sql_insert_script = "INSERT INTO PRODUCT_DIM (PRODUCT_CODE, PRODUCT_NAME, CATEGORY, BRAND, PRICE) VALUES "

# Adding values for each product
values_list = []
for entry in product_entries:
    values_list.append("('{0}', '{1}' , '{2}' , '{3}' , {4})".format(entry[0].replace("'", "''"), entry[1].replace("'", "''"), entry[2].replace("'", "''"), entry[3].replace("'", "''"), entry[4] ) )


# Joining all the values together separated by commas
sql_insert_script += ',\n'.join(values_list)
sql_insert_script += ';'


with open('insert_products.sql', 'w') as sql_file:
    sql_file.write(sql_insert_script)

print(sql_insert_script)
