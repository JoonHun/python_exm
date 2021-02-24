import random

print("random module")

print("random() ", random.random())

print("uniform(10,20) ", random.uniform(10,20))

print("randrange(10) ", random.randrange(10))

print("randrange(10, 20) ", random.randrange(10,20))

print("choice([1, 2, 3, 4, 5]) ", random.choice([1, 2, 3, 4, 5]))

print("shuffle([1, 2, 3, 4, 5]) ", random.shuffle([1, 2, 3, 4, 5]))

print("sample([1, 2, 3, 4, 5], k=2) ", random.sample([1, 2, 3, 4, 5], k=2))

a = "Test "
b = "Test2"
print(a+b)