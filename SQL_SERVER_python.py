# importing libs
import pyodbc
import pandas as pd

# sql file path
sql_file = open("E:\\Projects\\SQL-SERVER-Connection-with-Python\\SQL_query.sql")

# converting query in string
sql_as_string = sql_file.read().replace('\n',' ')

# connecting in SQL SERVER
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-1LCCVB\\SQLEXPRESS;'
                      'Database=Youtube;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

# inputing query in SQL SERVER and reading query
sql_query = pd.read_sql_query(sql_as_string , conn)
print(sql_query)