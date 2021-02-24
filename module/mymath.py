mypi = 3.14

def add(a, b):
  print(__name__)
  return a+b

def area(r):
  print(__name__)
  return mypi * r * r

# if this module was included from other module, the follow code will not work
if __name__ == "__main__":
  print("test add = {})".format(add(2,3)))
  print("Test area = {}".format(area(5)))