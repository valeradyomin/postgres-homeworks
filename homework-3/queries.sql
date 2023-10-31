-- Напишите запросы, которые выводят следующую информацию:
-- 1. Название компании заказчика (company_name из табл. customers) и ФИО сотрудника, работающего над заказом этой компании (см таблицу employees),
-- когда и заказчик и сотрудник зарегистрированы в городе London, а доставку заказа ведет компания United Package (company_name в табл shippers)
SELECT customers.company_name, CONCAT(employees.last_name, ' ', employees.first_name) AS employee
FROM orders
JOIN customers USING(customer_id)
JOIN employees USING(employee_id)
JOIN shippers ON shippers.shipper_id = orders.ship_via
WHERE shippers.company_name = 'United Package' AND employees.city = 'London' AND customers.city = 'London'

-- 2. Наименование продукта, количество товара (product_name и units_in_stock в табл products),
-- имя поставщика и его телефон (contact_name и phone в табл suppliers) для таких продуктов,
-- которые не сняты с продажи (поле discontinued) и которых меньше 25 и которые в категориях Dairy Products и Condiments.
-- Отсортировать результат по возрастанию количества оставшегося товара.
SELECT product_name, units_in_stock, contact_name, phone
FROM products
JOIN suppliers ON suppliers.supplier_id = products.supplier_id
JOIN categories ON categories.category_id = products.category_id
WHERE products.discontinued = 0 AND products.units_in_stock < 25 AND categories.category_name IN ('Condiments', 'Dairy Products')
ORDER BY products.units_in_stock

-- 3. Список компаний заказчиков (company_name из табл customers), не сделавших ни одного заказа
SELECT customers.company_name
FROM customers
LEFT JOIN orders ON orders.customer_id = customers.customer_id
WHERE orders.customer_id IS NULL

-- 4. уникальные названия продуктов, которых заказано ровно 10 единиц (количество заказанных единиц см в колонке quantity табл order_details)
-- Этот запрос написать именно с использованием подзапроса.
SELECT products.product_name
FROM products
WHERE products.product_id IN (SELECT order_details.product_id FROM order_details WHERE order_details.quantity = 10)