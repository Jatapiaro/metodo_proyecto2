po = lambda p: 1-p
pn = lambda n,p,por:pow(p,n)*por
lq = lambda p: (p*p)/(2*(1-p))
ls = lambda p,lqr: p+lqr
wq = lambda l,lqr: lqr/l
ws = lambda wqr,m: wqr+(1/m)

def md1(l,m,n=10):
    p = (l / m)
    lqr = lq(p)
    lsr = ls(p,lqr)
    wqr = wq(l,lqr)
    wsr = ws(wqr,m)
    por = po(p)
    pnr = [por]
    for x in range(1,n+1):
        pnr.append(pn(x,p,por))
    return p, lqr, lsr, wqr, wsr, pnr

