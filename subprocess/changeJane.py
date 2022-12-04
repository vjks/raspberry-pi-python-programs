#!/usr/bin/env python3
import sys
import subprocess

filename=sys.argv[1]
with open(filename) as fp:
  lines = fp.readlines()

for line in lines:
  source = line.strip()
  print("source is:" + source)
  destination = line.strip().replace("jane", "jdoe")
  print("destination is:" + destination)
  subprocess.run(["mv", "/home/student-00-37d8576e1856/" + "source", "/home/student-00-37d8576e1856/" + "destination"])