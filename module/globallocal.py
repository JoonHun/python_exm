#globallocal.py

a = 1
b = 2

def f():
  localx = 10
  localy = 20
  print ('global : ', globals())
  print ('local : ', locals())
  
f()
print ('global in module : ', globals())
print ('local in moudle : ', locals())

