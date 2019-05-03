import io
import time
import os
import re


columnas = []
columnasInsert = []
columna = ""
aColumnas = open('archivos_tablas/columnas.txt','r')
loglines = (aColumnas)
for line in loglines:
    columnas.append(line)
aColumnas.close()

loglines = open('log.txt','r')

for line in loglines:
    a = ""
    b = ""
    x = []
    y = []
    i = 0
    s = re.findall('url=(.*?) service=', line)
    for i in range(len(s)):
        texto = s[i].replace(" ","_")
        line = line.replace(s[i], texto)

    s = re.findall('"(.*?)"', line)

    for i in range(len(s)):
        texto = s[i].replace(" ","_")
        line = line.replace(s[i], texto)

    s = re.findall('catdesc=(.*?) url=', line)
    for i in range(len(s)):
        texto = s[i].replace(" ","_")
        line = line.replace(s[i], texto)
    line = line.replace(' date',' logDate')
    line = line.replace(' time',' logTime')
    line = line.replace('type','logType')
    line = line.replace('level','logLevel')
    line = line.replace('user','logUser')
    line = line.replace('logver','glogver',1)
    espacios = line.count(' ')
    for i in range(espacios):
        x.append(line.split(' ')[i].split('=')[0])
        y.append(line.split(' ')[i].split('=')[1])
    x.append(line.split(' ')[espacios].split('=')[0])
    y.append(line.split(' ')[espacios].split('=')[1])
#____________________---------------_____________
    valores = "("
    vcolumna = "("
    for e in range(len(x) - 1):
        campo = str(x[e])
        valor = str(y[e])
        vcolumna = vcolumna+ valor+","
        valores = valores + campo+","

    campo = str(x[len(x) - 1])
    valor = str(y[len(y) - 1])
    valores = valores +campo +')\n'
    vcolumna = vcolumna +  valor+');'
    consulta = ""

    for e in range(len(columnas)):
        if(valores == columnas[e]):
            #print('valor de e : '+str(e) + "valor de valores: " + str(valores))
            consulta = "insert into table"+str(e)+str(valores)+" values"+ str(vcolumna)

    aInserts = open("archivos_tablas/inserts.txt", 'a')
    aInserts.write(str(consulta))
    aInserts.close()
    print(consulta)
loglines.close()
