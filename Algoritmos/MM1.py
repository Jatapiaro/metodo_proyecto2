# coding=utf-8
ls = lambda l,m: l/(m-l) #número de unidades en el sistema
ws = lambda l,m: 1/(m-l) #tiempo que pasa una unidad en el sistema
lq = lambda l,m: (l*l)/(m*(m-l)) #número promedio de unidades esperando en la fila
wq = lambda l,m: l/(m*(m-l)) #tiempo en que unidad espera en la fila
p = lambda l,m: l/m #factor de uso del sistema
pn = lambda l,m,n: (1-(l/m))*pow((l/m),n) #probabilidad que el sistema tiene n unidades

def mm1(l,m,n=10):
    aux = p(l,m)
    pnl = []
    for x in range(0,n+1):
        pnl.append(pn(l,m,x))
    return ls(l,m),ws(l,m),lq(l,m),wq(l,m),aux,pnl