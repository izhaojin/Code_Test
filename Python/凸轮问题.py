# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from numpy import *
from scipy import interpolate
from scipy.optimize import minimize, rosen, rosen_der
import matplotlib.pyplot as plt

x = arange(0,2*pi,0.02)
loc = cos(x)
fin = sin
yin = fin(x)


xbc = linspace(0, pi,5)
ybc_=zeros_like(xbc)

def fe(ybc):
    bc = interpolate.interp1d(xbc, ybc, kind = 'cubic')
    bcx = where(x<pi,x,2*pi-x)
    ybc = bc(bcx)
    yout = yin-ybc
    #%%
    imax = argmax(yout)
    imin = argmin(yout)
    xmin = x[imin]
    xmax = x[imax]
    ymin = yout[imin]
    ymax = yout[imax]
    k = (ymax-ymin)/(xmax-xmin)
    b = ymin-k*xmin
    fline = lambda x:k*x+b
    if imax>imin:
        iL,iR = imin,imax
    else:
        iR,iL = imin,imax
    xLR = x[iL:iR]
    youtLR = yout[iL:iR]
    yline = fline(xLR)
    err = linalg.norm(yline-youtLR)
    return err
res = minimize(fe, ybc_,options={'xtol': 1e-8, 'disp': True})

@vectorize
def out(x):
    return x if (x<pi/2)|(x>pi*3/2) else -(x-pi)
def bc(x):
    return sin(x) - out(x)

t = random.random(shape(xbc))
t = (t-0.5)
bc = interpolate.interp1d(xbc, t, kind = 'cubic')
bcx = where(x<pi,x,2*pi-x)
ybc = bc(bcx)
yout = yin-ybc
plt.plot(x,yin,x,yout,x,ybc,'--')
