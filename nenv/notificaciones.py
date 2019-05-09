import io
import time
import os
import re
import mysql.connector as mariadb
import smtplib

mariadb_connection = mariadb.connect(user='root',password='RealNet2019',database='bd_prueba')
cursor = mariadb_connection.cursor()

def envioCorreo(mensaje):
    sendto = 'asalinas@realnet.com.mx'
    user = 'allan.salinas.ramirez@gmail.com'
    #password = ''
    smtpsrv = 'smtp.gmail.com'
    smtpserver = smtplib.SMTP(smtpsrv, 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(user, password)
    smtpserver.sendmail(user, sendto,mensaje)

    print 'it works!'
    smtpserver.close()


def deteccionVirus(v):
    asunto = 'Deteccion de {} \n'.format(v[6])
    mensaje = ''
    consulta = "SELECT nombre,encargado,equipo from datos_empresas where equipo='{}'".format(str(v[2]))
    cursor.execute(consulta)
    for(nombre,encargado,equipo) in cursor:
        Nombre = nombre
        Encargado = encargado
        Equipo = equipo
    Mensaje = 'Hola {} \n' \
              'Buen dia \n' \
              'Parte de nuestro servicio administrado PG que tiene contratado la empresa {} con RealNet es el monitoreo diario de su equipo,' \
              'el dia de hoy a las {} se detecto un virus, la vulnerabilidad llego a traves del correo {}, hacia el usuario {} y la ip {} , el archivo infectado que se detecto ' \
              'tiene por nombre: {} .\n' \
              'El archivo fue bloqueado por el equipo de Productivity Guru \n' \
              'Saludos' \
              ''.format(Encargado,Nombre,v[1],v[36],v[33],v[15],v[26])
    Asunto = 'Subject: {}\n\n {}'.format(asunto,Mensaje)
    #envioCorreo(Asunto)
    return


f = open('log2.txt', 'r')
loglines = (f)
for line in loglines:
    a = ""
    b = ""
    x = []
    y = []
    s = re.findall('"(.*?)"', line)
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
        x.append(line.split(' ')[i].split('=')[0].replace('"',''))
        y.append(line.split(' ')[i].split('=')[1].replace('"',''))
    x.append(line.split(' ')[espacios].split('=')[0])
    y.append(line.split(' ')[espacios].split('=')[1])
    campo = []
    valor = []
    for e in range(len(x)-1):
        campo.append(str(x[e]))
        valor.append(str(y[e]))

    deteccionVirus(valor)

