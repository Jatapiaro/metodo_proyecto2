# coding=utf-8
ls = lambda l,m: l/(m-l) #número de unidades en el sistema
ws = lambda l,m: 1/(m-l) #tiempo que pasa una unidad en el sistema
lq = lambda l,m: (l*l)/(m*(m-l)) #número promedio de unidades esperando en la fila
wq = lambda l,m: l/(m*(m-l)) #tiempo en que unidad espera en la fila
p = lambda l,m: l/m #factor de uso del sistema
pn = lambda l,m,n: (1-(l/m))*pow((l/m),n) #probabilidad que el sistema tiene n unidades

def mm1(l,m,n):
    aux = p(l,m)
    return ls(l,m),ws(l,m),lq(l,m),wq(l,m),aux,(1-aux),pn(l,m,n)