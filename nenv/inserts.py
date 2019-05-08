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
    for i in range(7):
        cambiodate = " <"+str(i)+">date"
        line = line.replace(str(cambiodate), ' fecha')
    line = line.replace('date','date_')
    line = line.replace(' time',' time_')
    line = line.replace('type','type_')
    line = line.replace('level','leve_')
    line = line.replace('user','user_')
    line = line.replace('logver','logver_',1)
    line = line.replace('action','action_')
    line = line.replace('status','status_')
    line = line.replace('group','group_')
    line = line.replace('log','log_')
    line = line.replace('count','count_')
    line = line.replace('desc','desc_')
    line = line.replace('mode','mode_')
    line = line.replace('version','version_')
    line = line.replace('from','from_')
    line = line.replace('to','to_')
    line = line.replace('checksum','checksum_')
    line = line.replace('file','file_')

    espacios = line.count(' ')
    for i in range(espacios):
        x.append(line.split(' ')[i].split('=')[0])
        y.append(line.split(' ')[i].split('=')[1])
    x.append(line.split(' ')[espacios].split('=')[0])
    y.append(line.split(' ')[espacios].split('=')[1])

    valores = "("
    vcolumna = "("
    for e in range(len(x) - 1):
        campo = str(x[e])
        valor = str(y[e])

        #vcolumna = vcolumna+ valor+","
        valores = valores + campo+","

        if valor.isdigit() == True:
            vcolumna = vcolumna + valor + ","
        else:
            vcolumna = vcolumna +"'"+ valor +"'"+ ","

    campo = str(x[len(x)-1])
    valor = str(y[len(y)-1])
    valores = valores +campo+')'
    valoresc = valores+'\n'

    if valor.isdigit() == True:
        vcolumna =vcolumna+valor+");"
    else:
        vcolumna =vcolumna+ "'" +str(valor)+"');"

    consulta = ""

    for e in range(len(columnas)):
        if(valoresc == columnas[e]):
            consulta = "insert into tabla"+str(e)+str(valores)+" values "+ str(vcolumna)
            consulta = consulta.replace("\n","")
            consulta = consulta+"\n"
   # print(consulta)
    aInserts = open("archivos_tablas/inserts.txt", 'a')
    aInserts.write(str(consulta))
    aInserts.close()

loglines.close()
