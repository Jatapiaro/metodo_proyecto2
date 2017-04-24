#coding=utf-8

lq = lambda l,s,p: (((l*l)*(s*s))+(p*p))/(2*(1-p))

ls = lambda lqr,p: lqr+p

wq = lambda lqr,l: lqr/l

ws = lambda wqr,m: wqr+(1/m)

po = lambda p: 1-p

pn = lambda n,p,por:pow(p,n)*por

def mg1(l,m,s,n=10):

    p = (l/m)
    lqr = lq(l,s,p)
    lsr = ls(lqr,p)
    wqr = wq(lqr,l)
    wsr = ws(wqr,m)
    por = po(p)

    pnr = [por]
    for x in range(1,n+1):
        pnr.append(pn(x,p,por))

    return p,lqr,lsr,wqr,wsr,pnr
