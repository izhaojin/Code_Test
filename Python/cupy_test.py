# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 02:06:53 2022

@author: Administrator
"""
# TensorFlow and tf.keras
import tensorflow as tf
import numba as nb
import numpy as np
import matplotlib.pyplot as plt


@nb.vectorize
def f(x):
    k = 1
    if x<np.pi/2:
        return k*x
    else:
        return -k*(x-np.pi)

xv = np.arange(-10.,10.,0.1)
yv = f(xv)