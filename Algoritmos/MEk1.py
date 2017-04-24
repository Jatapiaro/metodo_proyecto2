from math import sqrt

po = lambda p: 1-p
pn = lambda n,p,por:pow(p,n)*por
lq = lambda l,s,p: (((l*l)*(s*s))+(p*p))/(2*(1-p))
wq = lambda lqr,l: lqr/l
ws = lambda wqr,m: wqr+(1/m)
ls = lambda wsr,l: wsr*l

def mek1(l,m,k,n=10):
    p = (l / m)
    s = (1/sqrt(k))*(1/m)
    lqr = lq(l,s,p)
    wqr = wq(lqr,l)
    wsr = ws(wqr,m)
    lsr = ls(wsr,l)
    por = po(p)
    pnr = [por]
    for x in range(1,n+1):
        pnr.append(pn(x,p,por))
    return p, lqr, lsr, wqr, wsr, pnr