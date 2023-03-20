import mysql.connector

conn = mysql.connector.connect(
    host="travelclaimdb.mysql.database.azure.com", 
    user='travelclaimdb', 
    password="y2$$6$%A9SL*2w", 
    database='dummy_db')

cursor = conn.cursor()
query = ("SELECT * FROM invoice WHERE invoice_id = 1")
dataName = '1'
cursor.execute(query)
result = cursor.fetchone()
print(result)
if result[0] == 1:
    print("True")
else:
    print("False")

print("connected")