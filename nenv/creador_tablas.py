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
    reservedWords = ['absolute','add','all','allocate','alter','and','any','are','as','asc','assertion','at','authorization','avg','begin','between','bit','bit_length','both','by','cascade','case','cast |char','character','character_length','char_length','check','close','coalesce','collate','commit','connect','connection','constraint','constraints','continue','convert','corresponding','count','create','cross','current','current_date','current_time','current_timestamp','current_user','cursor','date','deallocate','dec','decimal','declare','default','deferrable','deferred','delete','desc','describe','descriptor','diagnostics','disconnect','distinct','domain','double','drop','else','end','endexec','escape','except','exception','exec','execute','exists','external','extract','false','fetch','first','float','for','foreign','found','from','full','get','global','go','goto','grant','group','having','hour','identity','immediate','in','indicator','initially','inner','input','insensitive','insert','int','integer','intersect','interval','into','is','isolation','join','language','last','leading','left','level','like','local','lower','match','max','min','minute','module','names','national','natural','nchar','next','no','not','null','nullif','numeric','octet_length','of','on','only','open','option','or','outer','output','overlaps','pad','partial','prepare','preserve','primary','prior','privileges','procedure','public','read','real','references','relative','restrict','revoke','right','role','rollback','rows','schema','scroll','second','section','select','session_user','set','shard','smallint','some','space','sqlerror','sqlstate','statistics','substring','sum','sysdate','system_user','table','temporary','then','time','timezone_hour','timezone_minute','to','top','trailing','transaction','trim','true','union','unique','update','upper','user','using','values','varchar','varying','when','whenever','where','with','work','write']
    for e in reservedWords:
        line = line.replace(e + "=", e + "_=")
    line = line.replace('logver', 'logver_', 1)

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