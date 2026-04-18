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

print(df_boston)

# STEP 2
df_zero_emp = pd.read_sql("""
                          SELECT COUNT(employeeNumber) AS numEmployees, city, officeCode
                          FROM offices
                          JOIN employees USING(officeCode)
                          GROUP BY city
                          HAVING numEmployees = 0;
                          """, conn)

print(df_zero_emp)

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
df_credit = None

# STEP 7
df_product_sold = None

# STEP 8
df_total_customers = None

# STEP 9
df_customers = None

# STEP 10
df_under_20 = None

conn.close()