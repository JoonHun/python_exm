import os
import sys

try:
  commitLog = sys.argv[1]
  print(commitLog)
except:
  print("input commit text")
  os.exit()

os.system("git status")
input("Move next step")
os.system("git add .")
input("Move next step")
arg = "git commit -m \"" + commitLog + "\""
#print(arg)
os.system(arg)
input("Move next step")
os.system("git branch -M main")
input("Move next step")
os.system("git push -u origin main")