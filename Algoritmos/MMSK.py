#coding=utf-8
from math import factorial

po_sum = lambda lmd,m,s: sum(pow(lmd/m,n)/factorial(n) for n in range(0,s+1))
po_sum2 = lambda lmd,m,s,k: sum(pow(lmd/m*s,n-s) for n in range(s+1,k+1))
po = lambda lmd,m,s,k: 1 / (po_sum(lmd,m,s) + ((pow(lmd/m,s)/factorial(s))*po_sum2(lmd,m,s,k)))

l = lambda p,k: (p/(1-p)) - (((k+1)*pow(p,k+1))/(1-pow(p,k+1))) #Promedio cleintes en sistema

##lq = lambda lmd,m,s,k,p,por: ((por*pow(lmd/m,s)*p)/(factorial(s))*(pow(1-p,2))) * ((pow(1-p,k-s))-((k-s)*pow(p,k-s)*(1-p)))

pk = lambda p,k: ((1-p)/(1-pow(p,k+1)))*pow(p,k) #Probabiliad de estado estable de estar en el estado k

lmd_prima = lambda lmd,pkr: lmd*(1-pkr) #Tasa promedio de llegadas

w = lambda lr,lmd_primar: lr/lmd_primar #Tiempo promedio dentro del sistema

def mmsk(lmd,m,s,k):

    p = (lmd/m)
    lr = l(p,k) #Return

    pkr = pk(p,k)

    lmd_primar = lmd_prima(lmd,pkr)

    wr = w(lr,lmd_primar) #Return

    por = po(lmd,m,s,k)

    ##lqr = lq(lmd,m,s,k,p,por)

    return lr,wr,por##,lqr