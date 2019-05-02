import time
import os
import re
from dateutil.parser import parse
f = open('log.txt', 'r')  # Carga del archivo
nt = 0
tabla3 = [' ']
tablaf = []
def follow(f):  # Funcion que lee el ultimo renglon del archivo, si detecta cambios espera 0.3 segundos para volver a correr
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.3)
            continue
        yield line
loglines = (f)

for line in loglines:
    a = ""
    b = ""
    x = []
    y = []
    i = 0
    s = re.findall('"(.*?)"', line)  # Busca todo lo que este dentro de " " del archivo

    for i in range(len(s)):
        texto = s[i].replace(" ","_")  # De la busqueda anterior, dentro del texto remplaza los espacios por guiones bajos
        line = line.replace(s[i], texto)  # Remplaza el texto corregido con guion bajo en el texto con espacios
    espacios = line.count(' ')
    for i in range(espacios):  # Arreglo para separar el texto, primero separa por espacios, y luego separa por el signo de igual
        x.append(line.split(' ')[i].split('=')[0])
        y.append(line.split(' ')[i].split('=')[1])

    x.append(line.split(' ')[2].split('=')[0])
    y.append(line.split(' ')[2].split('=')[1])

    tabla1 = 'Create table '
    ntabla = "tabla"
    valores = "("
    tabla2 = tabla1 + ntabla + str(nt)+'('

    for e in range(len(x)-1):
        campo = str(x[e])
        valor = str(y[e])
        if valor.isdigit() == True:
            valores = valores + ' '+campo+' int,'
        else:
            valores = valores + ' '+campo+' varchar,'
    campo = str(x[len(x)-1])
    valor = str(y[len(y)-1])

    if valor.isdigit() == True:
        valores = valores + ' '+campo+' int );'
    else:
        valores = valores + ' '+campo+' varchar );'

    if valores not in tabla3:
        rtabla = tabla1+ntabla+str(nt)+valores
        print rtabla
        tablaf.append(rtabla)
        tabla3.append(valores)
        nt += 1


print(tablaf)
print(len(tabla3))
