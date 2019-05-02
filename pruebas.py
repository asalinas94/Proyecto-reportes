ntable = "tabla"
i = 0

a = ['a','b',5]
b = ""
create = "CREATE TABLE"+ str(i)

#for e in range(len(a)):
    #valor = str(a[e])
   # if valor.isdigit() == True:
  #      print( str(a[e])+" es numero")
 #   else:
#        print( a[e]+" no es numero")
    #b = b+str(a[e])
#print(b)
print a
print(len(a))
for e in range(len(a)):
    a.append(e)
    print a
print(len(a))

c = 'c'
print(str(c) in a)