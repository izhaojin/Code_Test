# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 23:29:16 2022

@author: Administrator
"""

import numpy as np
import numba as nb
from matplotlib.pyplot import plot
import sympy as sym
# %%
# 关于r_的用法
# r_[a:b:Nj]：区间[a,b]等分为N份
# r_[a:b:step]:区间[a,b)，步长为step
xv = np.linspace(-10, 10,10000)
# 矩阵连接 r_,c_
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[11, 22, 33], [44, 55, 66]]

mr = np.r_[m1, m2]
mc = np.c_[m1, m2]

# 我们假定
# 行向量-[1,2,3]
# 列向量[[1],[2],[3]]
# r_：改变总行数叠加，不改变列数（每一行数量不变）
# c_：改变总列数叠加，不改变行数（每一行的数量不变）
#
# r_
# mr =
# array([[ 1,  2,  3],
#        [ 4,  5,  6],
#        [11, 22, 33],
#        [44, 55, 66]])

# mc =
# array([[ 1,  2,  3, 11, 22, 33],
#        [ 4,  5,  6, 44, 55, 66]])

# %%
# 分段函数实现方案
# 方案1 numpy.vectrorize
# 方案2 numba.vectorize

f1 = nb.vectorize(lambda x: -x**3 if x < 0 else x**2 if x < 2 else x)

# 方案2 使用where
f2 = lambda x: np.where(x < 0, -x**3, np.where(x < 2, x**2, x))

# 方案3 使用Piswise
x = sym.var('x')
f3 = sym.lambdify(x,
                  sym.Piecewise((-x**3, x < 0), (x**2, x < 2), (x, True)), "numpy")

# 根据实际测试运行时间，numba最牛！
# numba.vectorize: 2.7 us
# numba.jit(where): 14.2 us
# where: 148 us
# Piecewise: 177 us
# numpy.vectorize：1120 us

# numba.jit加在任意函数前面装饰，可以加速
#%% 使用mpmath 快速绘图
import  mpmath as mp
f1 = lambda x:x*x
mp.plot(f1,[-10,10])

#%% 数值微分方案
# 参考文献：https://blogs.mathworks.com/cleve/2013/10/14/complex-step-differentiation/
import sympy as sym
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

# 标准值
x = sym.Symbol('x')
y = sym.exp(x)/((sym.cos(x))**3 + (sym.sin(x))**3)
dy = y.diff(x)
f = sym.lambdify(x,y,'numpy')
df = sym.lambdify(x,dy,'numpy')

# 三种微分方案：复数，双边差分，单边差分
dfc = lambda x,h:np.imag(f(x+h*1j)/h)
dfn = lambda x,h:(f(x+h)-f(x-h))/(2*h)
dfn2 = lambda x,h:(f(x+h)-f(x))/(h)

# 三种微分方案精度对比

def feps(dfv):
    return lambda x,h:np.abs(dfv(x,h)-df(x))
s = np.arange(1,30)
hv = 1/10**s
eps_c = feps(dfc)(pi/4,hv)
eps_n = feps(dfn)(pi/4,hv)
eps_n2 = feps(dfn2)(pi/4,hv)


plt.plot(eps_c,label='complex')
plt.plot(eps_n,label='normal')
plt.plot(eps_n2,label='normal2')
plt.yscale('log')
plt.legend()
plt.show()