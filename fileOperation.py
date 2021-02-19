# simple file operation
"""
file = open("cputemp.py", "r")
content = file.read()
print(content);
file.close()
"""

# file will be closed out of with block
"""
with open("cputemp.py", "r") as file:
  content = file.read()

print(content)
"""

# write ramdom data, and read line by line
import random

hanguls = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

with open ("test.txt", "w") as file:
  for i in range(1000):
    name = random.choice(hanguls) + random.choice(hanguls) + random.choice(hanguls)
    weight = random.randrange(40, 100)
    height = random.randrange(140, 200)
    
    file.write("{}, {}, {}\n".format(name, weight, height))

with open("test.txt", "r") as file:
  for line in file:
    (name, weight, height) = line.strip().split(", ")
    if(not name) or (not weight) or (not height):
      continue
    
    BMI = int(weight)/((int(height)/100)**2)
    result = ""
    if(BMI >= 25):
      result = "Over"
    elif (BMI>=18.5):
      result = "Normal"
    else:
      result = "Under"
    
    print('\n'.join(["name : {}", "weight = {}", "height = {}", "BMI = {}", "Result = {}"]).format(name, weight, height, BMI, result))
    print()
