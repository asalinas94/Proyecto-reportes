import time
import os
import re
#import mysql.connector as mariadb

#mariadb_connection = mariadb.connect(user='root', password='RealNet2019', database='pruebapy')  # Conexion con MariaDB
#cursor = mariadb_connection.cursor()  # Se crea un cursor, que sera el encargado de la interaccion con la base de datos

f = open('log.txt', 'r')  # Carga del archivo


def follow(f):  # Funcion que lee el ultimo renglon del archivo, si detecta cambios espera 0.3 segundos para volver a correr
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.3)
            continue
        yield line
loglines = follow(f)
for line in loglines:
    a = ""
    b = ""
    i = 0
    s = re.findall('"(.*?)"', line)  # Busca todo lo que este dentro de " " del archivo

    for i in range(len(s)):
        texto = s[i].replace(" ","_")  # De la busqueda anterior, dentro del texto remplaza los espacios por guiones bajos
        line = line.replace(s[i], texto)  # Remplaza el texto corregido con guion bajo en el texto con espacios
    print(line)
    for i in range(2):  # Arreglo para separar el texto, primero separa por espacios, y luego separa por el signo de igual
        x = line.split(' ')[i].split('=')[0]  # El corte se hace en la posicion 0 que seria el valor de la columna
        y = line.split(' ')[i].split('=')[1]  # El corte se hace en la posicion 1 que seria el valor de la fila
        b = b + "'" + y + "'" + ","  # Se agrega el valor del corte en la posicion 1

    x = line.split(' ')[2].split('=')[0]
    y = line.split(' ')[2].split('=')[1]
    b = b + "'" + y + "'"

    z = ("Insert into amenazas values(" + b + ");")  # Se construye el script de insercion con los valores de b
    print(z)
    #cursor.execute(z)  # Se ejecuta el script en la base de datos mediante el cursor
    #mariadb_connection.commit()  # Se hace el commit de la informacion para que se guarde

#mariadb_connection.close()