-- Use the appropriate database, or uncomment the next line to create one
CREATE DATABASE IF NOT EXISTS order_entry_db;

-- Switching context to the newly created database 
USE DATABASE order_entry_db;

-- Creating Date Dimension Table
CREATE TABLE date_dim (
    date_id INT IDENTITY(1, 1) PRIMARY KEY,
    date_actual DATE NOT NULL,
    year SMALLINT NOT NULL,
    quarter SMALLINT NOT NULL,
    month SMALLINT NOT NULL,
    day_of_month SMALLINT NOT NULL,
    day_of_week SMALLINT NOT NULL,
    week_of_year SMALLINT NOT NULL,
    is_weekend BOOLEAN NOT NULL,
    is_holiday BOOLEAN NOT NULL,
    holiday_name VARCHAR(100)
);

-- Creating Product Dimension Table
CREATE TABLE product_dim (
    product_id INT IDENTITY(1, 1) PRIMARY KEY,
    product_code VARCHAR(50) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    brand VARCHAR(50),
    price DECIMAL(10,2)
);

-- Creating Customer Dimension Table
CREATE TABLE customer_dim (
    customer_id INT IDENTITY(1, 1) PRIMARY KEY,
    customer_code VARCHAR(50) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20),
    address_line1 VARCHAR(255),
    address_line2 VARCHAR(255),
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(10),
    country VARCHAR(50),
    loyalty_points INT
);

-- Creating Employee Dimension Table
CREATE TABLE employee_dim (
    employee_id INT IDENTITY(1, 1) PRIMARY KEY,
    employee_code VARCHAR(50) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20),
    hire_date DATE,
    department VARCHAR(50)
);

-- Creating Order Fact Table
CREATE TABLE order_fact (
    order_id INT IDENTITY(1, 1) PRIMARY KEY,
    date_id INT NOT NULL,
    product_id INT NOT NULL,
    customer_id INT NOT NULL,
    employee_id INT NOT NULL,
    quantity_ordered INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    discount_rate DECIMAL(5,2),
    total_amount DECIMAL(10,2) AS (quantity_ordered * unit_price * (1 - IFNULL(discount_rate, 0))),
    FOREIGN KEY (date_id) REFERENCES date_dim(date_id),
    FOREIGN KEY (product_id) REFERENCES product_dim(product_id),
    FOREIGN KEY (customer_id) REFERENCES customer_dim(customer_id),
    FOREIGN KEY (employee_id) REFERENCES employee_dim(employee_id)
);
