# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
df_boston = None

# STEP 2
df_zero_emp = None

# STEP 3
df_employee = None

# STEP 4
df_contacts = None

# STEP 5
df_payment = None

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