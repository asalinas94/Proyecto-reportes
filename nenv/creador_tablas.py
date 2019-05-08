import io
import time
import os
import re

f = open('log.txt', 'r')
nt = 0
tabla3 = [' ']
tablaf = []
columnas = []
columna = ""
def follow(f):
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
        line = line.replace(str(cambiodate), ' date_')

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

    tabla1 = 'Create table '
    ntabla = "tabla"
    valores = "("
    tabla2 = tabla1 + ntabla + str(nt)+'('
    columna = "("
    for e in range(len(x)-1):
        campo = str(x[e])
        valor = str(y[e])
        columna = columna+campo+","
        if valor.isdigit() == True:
            valores = valores + ' '+campo+' int unsigned,'
        else:
            if campo == 'url':
                valores = valores + ' ' + campo + ' varchar(1000),'
            else:
                if campo == 'cfgattr':
                    valores = valores + ' '+campo+' varchar(1000),'
                else:
                    valores = valores + ' ' + campo + ' varchar(200),'
    campo = str(x[len(x)-1])
    valor = str(y[len(y)-1])
    columna = columna +campo+")"
    if valor.isdigit() == True:
        valores = valores + ' '+campo+' int unsigned);'
    else:
        valores = valores + ' '+campo+' varchar(200));'

    if valores not in tabla3:
        rtabla = tabla1+ntabla+str(nt)+valores
        tablaf.append(rtabla)
        tabla3.append(valores)
        columnas.append(columna)
        nt += 1

aTablas = open('archivos_tablas/tablas.txt','a')
for e in range(len(tablaf)):
    aTablas.write(tablaf[e]+"\n")
aTablas.close()

aColumnas = open('archivos_tablas/columnas.txt','w')
for e in range(len(columnas)):
    aColumnas.write(columnas[e]+"\n")
aColumnas.close()

#print(columnas)