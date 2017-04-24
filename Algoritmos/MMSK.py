#coding=utf-8
from math import factorial

lmd_prima = lambda lmd,m,k,por: lmd * (1-(pow(lmd/m,k)*por))

w = lambda lr,lmd_primar: lr/lmd_primar
wq = lambda lqr,lmd_primar: lqr/lmd_primar

def po(lmd,m,s,k):
  var = pow(lmd/m,s)/factorial(s)
  sumatoria_uno = sum((pow(lmd/m,n)/factorial(n)) for n in range(0,s+1))
  sumatoria_dos = sum(pow(lmd/(s*m),n-s) for n in range(s+1,k+1))
  parte_dos = var*sumatoria_dos
  total = sumatoria_uno+parte_dos
  return pow(total,-1)

def lq(lmd,m,s,k,p,por):
    if lmd == s*m:
        multiplicacion = por*pow(lmd/m,s)
        multiplicacion_dos = k-s+pow(k-s,2)
        multiplicacion_final = multiplicacion*multiplicacion_dos
        resultado = multiplicacion_final/factorial(s)
        return 0.5*resultado
    else:
        multiplicacion = por*pow(lmd/m,s)*p
        multiplicacion_tres = (k-s)*pow(p,k-s)*(1-p)
        multiplicacion_dos = 1-pow(p,k-s)-multiplicacion_tres
        final = multiplicacion*multiplicacion_dos
        return final / (factorial(s)*pow(1-p,2))


def pn(lmd,m,s,k,por,n):
    if n<=s:
        return (pow(lmd,n)/(factorial(n)*pow(m,n)))*por
    elif n>s and n<=k:
        return (pow(lmd,n)/(factorial(s)*pow(m,n)*pow(s,n-s)))*por

def l(lmd,m,s,k,lqr,pnr):
    sumatoria_uno = sum(x*pnr[x] for x in range(0,s)) + lqr
    sumatoria_dos = 1 - sum(pnr[x] for x in range(0,s))
    parte_dos = s * sumatoria_dos
    return sumatoria_uno+parte_dos

def mmsk(lmd,m,s,k,n=10):
    p = (lmd/(m*s)) #Return
    por = po(lmd,m,s,k)
    lqr = lq(lmd,m,s,k,p,por)

    pnr = [por]
    for x in range(1,k+1):
        pnr.append(pn(lmd,m,s,k,por,x))

    lr = l(lmd,m,s,k,lqr,pnr)
    lmd_primar = lmd_prima(lmd,m,k,por)
    wr = w(lr,lmd_primar)
    wqr = wq(lqr,lmd_primar)

    return lr,lqr,wr,wqr,p,pnr
