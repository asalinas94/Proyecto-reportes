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
        line = line.replace(str(cambiodate), ' date_')
    reservedWords = ['absolute', 'add', 'all', 'allocate', 'alter', 'and', 'any', 'are', 'as', 'asc', 'assertion', 'at',
                     'authorization', 'avg', 'begin', 'between', 'bit', 'bit_length', 'both', 'by', 'cascade', 'case',
                     'cast |char', 'character', 'character_length', 'char_length', 'check', 'close', 'coalesce',
                     'collate', 'commit', 'connect', 'connection', 'constraint', 'constraints', 'continue', 'convert',
                     'corresponding', 'count', 'create', 'cross', 'current', 'current_date', 'current_time',
                     'current_timestamp', 'current_user', 'cursor', 'date', 'deallocate', 'dec', 'decimal', 'declare',
                     'default', 'deferrable', 'deferred', 'delete', 'desc', 'describe', 'descriptor', 'diagnostics',
                     'disconnect', 'distinct', 'domain', 'double', 'drop', 'else', 'end', 'endexec', 'escape', 'except',
                     'exception', 'exec', 'execute', 'exists', 'external', 'extract', 'false', 'fetch', 'first',
                     'float', 'for', 'foreign', 'found', 'from', 'full', 'get', 'global', 'go', 'goto', 'grant',
                     'group', 'having', 'hour', 'identity', 'immediate', 'in', 'indicator', 'initially', 'inner',
                     'input', 'insensitive', 'insert', 'int', 'integer', 'intersect', 'interval', 'into', 'is',
                     'isolation', 'join', 'language', 'last', 'leading', 'left', 'level', 'like', 'local', 'lower',
                     'match', 'max', 'min', 'minute', 'module', 'names', 'national', 'natural', 'nchar', 'next', 'no',
                     'not', 'null', 'nullif', 'numeric', 'octet_length', 'of', 'on', 'only', 'open', 'option', 'or',
                     'outer', 'output', 'overlaps', 'pad', 'partial', 'prepare', 'preserve', 'primary', 'prior',
                     'privileges', 'procedure', 'public', 'read', 'real', 'references', 'relative', 'restrict',
                     'revoke', 'right', 'role', 'rollback', 'rows', 'schema', 'scroll', 'second', 'section', 'select',
                     'session_user', 'set', 'shard', 'smallint', 'some', 'space', 'sqlerror', 'sqlstate', 'statistics',
                     'substring', 'sum', 'sysdate', 'system_user', 'table', 'temporary', 'then', 'time',
                     'timezone_hour', 'timezone_minute', 'to', 'top', 'trailing', 'transaction', 'trim', 'true',
                     'union', 'unique', 'update', 'upper', 'user', 'using', 'values', 'varchar', 'varying', 'when',
                     'whenever', 'where', 'with', 'work', 'write']
    for e in reservedWords:
        line = line.replace(e + "=", e + "_=")
    line = line.replace('logver', 'logver_', 1)


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

        valor = valor.replace('"','')
        valor = valor.replace('_',' ')
        valores = valores + campo+","
        valor = valor.replace("'", '"')

        if valor.isdigit() == True:
            vcolumna = vcolumna + valor + ","
        else:
            vcolumna = vcolumna +"'"+ valor +"'"+ ","

    campo = str(x[len(x)-1])
    valor = str(y[len(y)-1])
    valor = valor.replace('"', '')
    valor = valor.replace('_', ' ')
    valor = valor.replace("'",'"')
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
