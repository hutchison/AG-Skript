#!/usr/bin/env python

# Berechnet eine lineare Funktion aus zwei eingegebenen Punkten.
# Gibt Funktionswerte zu Eingabewerten aus.

import sys

try:
    s1 = raw_input("Punkt 1: ")
    s2 = raw_input("Punkt 2: ")
except (KeyboardInterrupt, EOFError):
    print
    sys.exit()
s1, s2 = '(' + s1 + ')', '(' + s2 + ')'
p1, p2 = eval(s1), eval(s2)

m = (float(p1[1]) - float(p2[1])) / (float(p1[0]) - float(p2[0]))
n = float(p1[1]) - m * float(p1[0])

print "y =", m, "x +", n

while True:
    try:
        x = float(raw_input("x: "))
    except (KeyboardInterrupt, EOFError):
        print
        sys.exit()
    y = m*x+n
    print y
