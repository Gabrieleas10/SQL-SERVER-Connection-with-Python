import pyodbc
import pandas as pd
            
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-1LCCVB\SQLEXPRESS;'
                      'Database=Youtube;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

query = 'SELECT * FROM CLIENTES'

sql_query = pd.read_sql_query(query , conn)
print(sql_query)