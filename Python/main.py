import mysql.connector

conn = mysql.connector.connect(
    user='root', password='arbolesroot123', host='mysql', port=3306, database='arboles')

cursor = conn.cursor()
print("DB connected")

cursor.execute('SHOW TABLES;')
arboles = cursor.fetchall()
conn.close()
print(f'{arboles}')
