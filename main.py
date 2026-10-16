# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# Replace None with your code
df_boston = pd.read_sql("""
SELECT e.firstName, e.lastName
FROM employees e
JOIN offices o USING (officeCode)
WHERE o.city = 'Boston'
""", conn)

# STEP 2
# Replace None with your code
df_zero_emp = pd.read_sql("""
SELECT o.officeCode, o.city
FROM offices o
LEFT JOIN employees e USING (officeCode)
GROUP BY o.officeCode
HAVING COUNT(e.employeeNumber) = 0
""", conn)

# STEP 3
# Replace None with your code
df_employee = pd.read_sql("""
SELECT e.firstName, e.lastName, o.city, o.state
FROM employees e
LEFT JOIN offices o USING (officeCode)
ORDER BY e.firstName, e.lastName
""", conn)

# STEP 4
# Replace None with your code
df_contacts = pd.read_sql("""
SELECT c.contactFirstName, c.contactLastName, c.phone, c.salesRepEmployeeNumber
FROM customers c
LEFT JOIN orders o USING (customerNumber)
WHERE o.orderNumber IS NULL
ORDER BY c.contactLastName
""", conn)

# STEP 5
# Replace None with your code
df_payment = pd.read_sql("""
SELECT c.contactFirstName, c.contactLastName, p.paymentDate, p.amount
FROM customers c
JOIN payments p USING (customerNumber)
ORDER BY CAST(p.amount AS REAL) DESC
""", conn)

# STEP 6
# Replace None with your code
df_credit = pd.read_sql("""
SELECT e.employeeNumber, e.firstName, e.lastName,
       COUNT(c.customerNumber) AS n_customers
FROM employees e
JOIN customers c ON c.salesRepEmployeeNumber = e.employeeNumber
GROUP BY e.employeeNumber
HAVING AVG(c.creditLimit) > 90000
ORDER BY n_customers DESC
""", conn)

# STEP 7
# Replace None with your code
df_product_sold = pd.read_sql("""
SELECT p.productName,
       COUNT(od.orderNumber) AS numorders,
       SUM(od.quantityOrdered) AS totalunits
FROM products p
JOIN orderdetails od USING (productCode)
GROUP BY p.productCode
ORDER BY totalunits DESC
""", conn)

# STEP 8
# Replace None with your code
df_total_customers = pd.read_sql("""
SELECT p.productName, p.productCode,
       COUNT(DISTINCT o.customerNumber) AS numpurchasers
FROM products p
JOIN orderdetails od USING (productCode)
JOIN orders o USING (orderNumber)
GROUP BY p.productCode
ORDER BY numpurchasers DESC
""", conn)

# STEP 9
# Replace None with your code
df_customers = pd.read_sql("""
SELECT COUNT(c.customerNumber) AS n_customers, o.officeCode, o.city
FROM offices o
JOIN employees e USING (officeCode)
JOIN customers c ON c.salesRepEmployeeNumber = e.employeeNumber
GROUP BY o.officeCode
ORDER BY o.officeCode
""", conn)

# STEP 10
# Replace None with your code
df_under_20 = pd.read_sql("""
SELECT DISTINCT e.employeeNumber, e.firstName, e.lastName, o.city, o.officeCode
FROM employees e
JOIN offices o USING (officeCode)
JOIN customers c ON c.salesRepEmployeeNumber = e.employeeNumber
JOIN orders ord ON ord.customerNumber = c.customerNumber
JOIN orderdetails od USING (orderNumber)
WHERE od.productCode IN (
    SELECT od2.productCode
    FROM orderdetails od2
    JOIN orders o2 USING (orderNumber)
    GROUP BY od2.productCode
    HAVING COUNT(DISTINCT o2.customerNumber) < 20
)
ORDER BY e.lastName
""", conn)

conn.close()