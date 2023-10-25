-- SQL-команды для создания таблиц
CREATE TABLE customers
(
	customer_id varchar(10) PRIMARY KEY,
	company_name varchar(60) NOT NULL,
	contact_name varchar(60) NOT NULL
);

CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(20) NOT NULL,
	last_name varchar(20) NOT NULL,
	title varchar (50) NOT NULL,
	birth_date date,
	notes text
);

CREATE TABLE orders
(
	order_id serial PRIMARY KEY,
	customer_id varchar(10) NOT NULL,
	employee_id int NOT NULL,
	order_date date NOT NULL,
	ship_city varchar(25) NOT NULL,
	FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
	FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

SELECT * FROM customers;
SELECT * FROM employees;
SELECT * FROM orders;