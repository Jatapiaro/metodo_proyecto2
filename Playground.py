from Algoritmos.MM1 import mm1
from Algoritmos.MMS import mms
from Algoritmos.MMSK import mmsk
from Algoritmos.MG1 import mg1

l = float(input("Ingresa lambda: "))
m = float(input("Ingresa mu: "))
#n = int(input("Ingresa n: "))
#s = int(input("Ingresa s: "))
#k = int(input("Ingresa k: "))
s = float(input("Ingresa s: "))

##rint(mm1(l,m,n))
##print(mms(l,m,s))
##print (mmsk(l,m,s,k))
print(mg1(l,m,s))
