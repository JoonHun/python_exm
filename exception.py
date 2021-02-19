# normal exception handling
"""
try:
  value = int(input("digit : "))
except:
  print("not digit")
else:
  print("input = {}".format(value))
"""

# pass example

list_input = ["123", "456", "abc", "789"]
list_val = []

for item in list_input:
  try:
    float(item)  # can not covert float, exception!!!
    list_val.append(item)
  except:
    pass  # no operation

print(list_val)
