# coding: utf-8
import numpy as np
import matplotlib.pylab as plt


def numerical_diff(f, x): # 数値微分
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

def function_1(x):
    return 0.01*x**2 + 0.1*x 

def tangent_line(f, x): # 接線 y-f(x) = d(t-x)
    d = numerical_diff(f, x) # 傾き
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y
     
x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")

tf = tangent_line(function_1, 5) # function_1のx=5の時の接線
y2 = tf(x)

plt.plot(x, y)
plt.plot(x, y2)
plt.title('x=5')
plt.show()

tf = tangent_line(function_1, 10)
y2 = tf(x)

plt.plot(x, y)
plt.plot(x, y2)
plt.title('x=10')
plt.show()
