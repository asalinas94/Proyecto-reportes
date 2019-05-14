import io
import time
import os
import re
import mysql.connector as mariadb
import smtplib

def lectorLinea(line,tipoValor):
    a = ""
    b = ""
    x = []
    y = []
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
    if tipoValor == 'Virus':
        deteccionVirus(valor)

def deteccionVirus(v):
    mariadb_connection = mariadb.connect(user='root', password='RealNet2019', database='bd_prueba')
    cursor = mariadb_connection.cursor()
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
    envioCorreo(Asunto)
    mariadb_connection.close()
    print(Asunto)

def envioCorreo(mensaje):
    sendto = 'asalinas@realnet.com.mx'
    user = 'allan.salinas.ramirez@gmail.com'
    password = 'Reflektor94'
    smtpsrv = 'smtp.gmail.com'
    smtpserver = smtplib.SMTP(smtpsrv, 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(user, password)
    smtpserver.sendmail(user, sendto,mensaje)
    print 'it works!'
    smtpserver.close()
