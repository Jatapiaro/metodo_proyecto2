#coding=utf-8
from math import factorial

po_expresion = lambda l,m,s: pow(l/ m,s)/(factorial(s) * (1-(l/(s*m))))
po_sum = lambda l,m,s: sum((pow(l/m,n)/factorial(n)) for n in range(0,s))
po = lambda l,m,s: 1 / (po_sum(l,m,s) + po_expresion(l,m,s))


lq = lambda l,m,s,por: por * (pow(l/m,s+1) / (factorial(s-1)*pow(s-(l/m),2))) #Promedio de Clientes en fila

wq = lambda lqr,l: lqr/l #Tiempo Promedio en fila

ls = lambda l,m,s,por: ((l*m*pow(l/m,s)*por)/(factorial(s-1)*pow(s*m-l,2))) + (l/m) #Promedio de Clientes en el Sistema

ws = lambda lsr,l: lsr/l #Tiempo Promedio Dentro del Sistema

pn_menors = lambda l,m,n,por: (pow(l/m,n)*por)/(factorial(n))
pn_mayors = lambda l,m,n,s,por: (pow(l/m,n)*por)/(factorial(s)*pow(s,n-s))

def mms(l,m,s,n=10):
    por = po(l,m,s)
    lqr = lq(l,m,s,por)
    wqr = wq(lqr,l)
    lsr = ls(l,m,s,por)
    wsr = ws(lsr,l)
    p = l/(m*s) #Utilización de los servidores
    return lsr,lqr,wsr,wqr,p