#coding=utf-8
from math import factorial


l = lambda p,k: (p/(1-p)) - (((k+1)*pow(p,k+1))/(1-pow(p,k+1))) #Promedio cleintes en sistema

pk = lambda p,k: ((1-p)/(1-pow(p,k+1)))*pow(p,k) #Probabiliad de estado estable de estar en el estado k

lmd_prima = lambda lmd,pkr: lmd*(1-pkr) #Tasa promedio de llegadas

w = lambda lr,lmd_primar: lr/lmd_primar #Tiempo promedio dentro del sistema

wq = lambda lqr,lmd_primar: lqr/lmd_primar #Tiempo Promedio en Fila

def po(lmd,m,s,k):
  var = pow(lmd/m,s)/factorial(s)
  sumatoria_uno = sum((pow(lmd/m,n)/factorial(n)) for n in range(0,s+1))
  sumatoria_dos = sum(pow(lmd/(s*m),n-s) for n in range(s+1,k+1))
  parte_dos = var*sumatoria_dos
  total = sumatoria_uno+parte_dos
  return pow(total,-1)

def lq(lmd,m,s,k,por,p):
    division_arriba = por*pow(lmd/m,s)*p
    division_abajo = factorial(s)*((1-p)*(1-p))
    division_final = division_arriba/division_abajo
    multiplicacion = (k-s)*pow(p,k-s)*(1-p)
    parte_dos = 1-pow(p,k-s)-multiplicacion
    return division_final*parte_dos


def mmsk(lmd,m,s,k):

    p = (lmd/m) #Return
    lr = l(p,k) #Return

    pkr = pk(p,k)

    lmd_primar = lmd_prima(lmd,pkr) #Return - lmd_e

    wr = w(lr,lmd_primar) #Return

    por = po(lmd,m,s,k)
    lqr = lq(lmd,m,s,k,por,p) #Return
    wqr = wq(lqr,lmd_primar) #Return
    return lr,wr,por,lqr,wqr