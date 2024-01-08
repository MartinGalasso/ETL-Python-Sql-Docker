import mysql.connector
import csv

with open("/usr/src/app/dataset/caracteristicas.csv",'r+', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    conn = mysql.connector.connect(
           user='', password='arbolesroot123', host='mysql', port=3306, database='arboles')
    
    print('Connection successful')
    
    cursor = conn.cursor()

    for row in reader:
        cursor.execute('INSERT INTO Caracteristicas(tipo_folla) VALUES(%s)',row)
    
    conn.commit()

    cursor.close()

    conn.close()
 

