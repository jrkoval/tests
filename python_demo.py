#!/usr/bin/python

import sys

print(sys.argv)

args = sys.argv[1:]

p = int(args[0])
r = int(args[1])
t = int(args[2])
print(p*r*t/100)
