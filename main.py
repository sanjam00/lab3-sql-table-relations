# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
df_boston = pd.read_sql("""
                        SELECT firstName, lastName
                        FROM employees
                        JOIN offices USING(officeCode)
                        WHERE officeCode = "2";
                        """, conn)

# print(df_boston)

# STEP 2
df_zero_emp = pd.read_sql("""
                          SELECT COUNT(employeeNumber) AS numEmployees, city, officeCode
                          FROM offices
                          JOIN employees USING(officeCode)
                          GROUP BY city
                          HAVING numEmployees = 0;
                          """, conn)

# print(df_zero_emp)

# STEP 3
df_employee = pd.read_sql("""
                          SELECT firstName, lastName, city, state
                          FROM employees
                          JOIN offices USING(officeCode)
                          ORDER BY firstName, lastName
                          """, conn)

# print(df_employee)

# STEP 4
df_contacts = pd.read_sql("""
                          SELECT c.contactFirstName, c.contactLastName, c.phone, c.salesRepEmployeeNumber
                          FROM customers AS c
                          LEFT JOIN orders AS o 
                          ON c.customerNumber = o.customerNumber
                          WHERE o.customerNumber IS NULL
                          ORDER BY contactLastName;
                          """, conn)

# print(df_contacts)

# STEP 5
df_payment = pd.read_sql("""
                         SELECT c.contactFirstName, c.contactLastName, CAST(p.amount AS FLOAT) AS amount, p.paymentDate
                         FROM customers c
                         JOIN payments p USING(customerNumber)
                         ORDER BY amount DESC
                         """, conn)

# print(df_payment)

# STEP 6
df_credit = pd.read_sql("""
                        SELECT e.employeeNumber, e.firstName, e.lastName, COUNT(c.customerNumber) AS numCustomers
                        FROM employees e
                        JOIN customers C
                          ON e.employeeNumber = c.salesRepEmployeeNumber
                        GROUP BY e.employeeNumber
                        HAVING AVG(creditLimit) > 90000
                        ORDER BY numCustomers DESC;
                        """, conn)

# print(df_credit)

# STEP 7
df_product_sold = pd.read_sql("""
                              SELECT productName, COUNT(od.productCode) AS numOrders, SUM(od.quantityOrdered) AS totalunits
                              FROM products p
                              JOIN orderDetails od USING(productCode)
                              GROUP BY productName
                              ORDER BY totalunits DESC;
                              """, conn)

# print(df_product_sold)

# STEP 8
df_total_customers = pd.read_sql("""
                                 SELECT p.productName, od.productCode, COUNT(DISTINCT o.customerNumber) AS numpurchasers
                                 FROM orderDetails od
                                 JOIN orders o USING(orderNumber)
                                 JOIN products p USING(productCode)
                                 GROUP BY p.productName
                                 ORDER BY numpurchasers DESC;
                                 """, conn)

# print(df_total_customers)

# STEP 9
# customers per office
df_customers = pd.read_sql("""
                           SELECT COUNT(c.customerNumber) AS n_customers, o.officeCode, o.city
                           FROM offices o
                           JOIN employees e USING(officeCode)
                           JOIN customers c
                            ON e.employeeNumber = c.salesRepEmployeeNumber
                           GROUP BY officeCode;
                           """, conn)

# print(df_customers)

# STEP 10
df_under_20 = pd.read_sql("""
                          SELECT DISTINCT e.employeeNumber, e.firstName, e.lastName, of.city, e.officeCode
                          FROM employees e
                          JOIN customers c
                           ON e.employeeNumber = c.salesRepEmployeeNumber
                          JOIN orders o USING(customerNumber)
                          JOIN orderDetails od USING(orderNumber)
                          JOIN offices of USING(officeCode)
                          WHERE od.productCode IN(
                            SELECT od.productCode
                            FROM orderDetails od
                            JOIN orders o USING(orderNumber)
                            GROUP BY od.productCode
                            HAVING COUNT(DISTINCT o.customerNumber) < 20)
                          ORDER BY e.lastName;
                          """, conn)

# print(df_under_20)

conn.close()