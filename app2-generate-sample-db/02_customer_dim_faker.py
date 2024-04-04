import random
from faker import Faker

# Initialize the Faker library with US locale for realistic data
fake = Faker('en_US')

def create_fake_customer():
    # Note: CUSTOMER_CODE is limited to 50 characters, adjust the pattern accordingly if needed
    customer_code = fake.bothify(text='CUST-########', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    first_name = fake.first_name().replace("'", "''")[:50]  # Limited to 50 characters
    last_name = fake.last_name().replace("'", "''")[:50]  # Limited to 50 characters
    email = fake.email()[:100]  # Limited to 100 characters
    phone = fake.phone_number()[:20]  # Limited to 20 characters
    address_line1 = fake.street_address().replace("'", "''")[:255]  # Limited to 255 characters
    address_line2 = fake.secondary_address().replace("'", "''")[:255]  # Limited to 255 characters
    city = fake.city().replace("'", "''")[:50]  # Limited to 50 characters
    state = fake.state_abbr()
    zip_code = fake.zipcode()
    country = 'USA'
    loyalty_points = random.randint(0, 10000)
    
    return f"('{customer_code}', '{first_name}', '{last_name}', '{email}', '{phone}', '{address_line1}', '{address_line2}', '{city}', '{state}', '{zip_code}', '{country}', {loyalty_points}),"

# Generate fake customer records
customer_records = [create_fake_customer() for _ in range(100)]
last_element = customer_records[-1]
last_element = last_element[:-1]
customer_records[-1] = last_element

# Prepare a single SQL insert query
newline = "\n"
sql_insert_statement = f"""
INSERT INTO CUSTOMER_DIM (CUSTOMER_CODE, FIRST_NAME, LAST_NAME, EMAIL, PHONE, ADDRESS_LINE1, ADDRESS_LINE2, CITY, STATE, ZIP_CODE, COUNTRY, LOYALTY_POINTS)
VALUES{newline.join(customer_records)};
"""

# Print or save the SQL insert statement
print(sql_insert_statement)

# Optionally write the SQL script to a file
with open('insert_customers.sql', 'w') as sql_file:
    sql_file.write(sql_insert_statement)
