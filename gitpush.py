import os
import sys

try:
  commitLog = sys.argv[1]
  print(commitLog)
except:
  print("input commit text")
  sys.exit()

input = input("Commit log : \"" + commitLog + "\"  Right? (y/n) ")
if( input != 'y' ):
  sys.exit()

os.system("git status")
os.system("git add .")

arg = "git commit -m \"" + commitLog + "\""
os.system(arg)

os.system("git branch -M main")
os.system("git push -u origin main")