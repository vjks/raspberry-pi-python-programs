#!/usr/bin/env python
from multiprocessing import Pool
import os
import subprocess

src = "../data/prod/"
dirs = next(os.walk(src))[1]

def backingup(dirs):
  dest = "../data/prod_backup/"
  subprocess.call(["rsync", "-arq", src, dest])

p = Pool(len(dirs))
p.map(backingup, dirs)