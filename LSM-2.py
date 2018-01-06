# -*- coding: utf-8 -*-
"""
     author:leehongbo
探索密度和甜度的关系。开始吧！
"""
import numpy as np
from sympy import *
import scipy as sp
import math
import matplotlib.pyplot as plt
from pylab import mpl 
x = []
y = []
f_x = []
a = []
plt.figure(1)
plt.figure(2)
#读取数据 密度&甜度
with open("data.txt","r") as f:
    readlines = f.readlines()
#求最小二乘法的k and b
def k_and_b():
    n = 0
    for line in readlines:
        line = line.rstrip('\n').split(',')
        x.append(float(line[0])*10)
        y.append(float(line[1])*10)
        n += 1       
    xs = np.array(x)
    ys = np.array(y)
    a,b,c,d,e=sp.polyfit(xs,ys,1,full=true)
    plt.figure(1)
    for i in range(n):
        plt.plot(xs[i],ys[i],'o')
    return a
def map():
    a = k_and_b()
    plt.figure(1)
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    plt.xlabel(u'p')  
    plt.ylabel(u'sugar')  
    plt.title(u'nature-data')
    xN=np.arange(0,10,0.1)
    y_b = a[0] * xN + a[1]
    plt.plot(xN,y_b)
    
    return a
map()
#y_star = kb[0] * xN + kb[1]
plt.show()