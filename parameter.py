import os
import time
import datetime

def print_n_times(*values, n=2):
    
    for i in range(n):
      for value in values:
        print(value)
    print(n);

print_n_times("Hello Python1", "Hello Python2", "Hello Python3", 3)
print_n_times("Hello Python1", "Hello Python2", "Hello Python3", n=3)