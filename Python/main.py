import mysql.connector

connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3300", database='arboles')
print("DB connected")

cursor = connection.cursor()
cursor.execute('')
arboles = cursor.fetchall()
connection.close()
