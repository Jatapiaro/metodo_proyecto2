from Algoritmos.MM1 import mm1
from Algoritmos.MMS import mms
from math import factorial
import scipy


l = float(input("Ingresa lambda: "))
m = float(input("Ingresa mu: "))
n = float(input("Ingresa n: "))
s = int(input("Ingresa s: "))


print(mms(l,m,s,n))

