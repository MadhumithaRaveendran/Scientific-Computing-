# -*- coding: utf-8 -*-
"""Problem_Sheet_8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IbEvxnqlQH6bVAfvsMufIp18dI23qaWL
"""

# Predictor and Corrector Method

from sympy import *
x,y = symbols('x y')

x_0 = 0
y_0 = 1
x = 0.4
n = 4
h = (x - x_0)/n
f = (2*x*y)/((1 + (x**2)))

x1 = []
y1 = []
f1 = []
x1.append(x_0)
y1.append(y_0)
f1.append(f.subs([(x,x_0),(y,y_0)]))


for i in range(1,n):
  k1 = h * (f.subs([(x,x_0),(y,y_0)]))
  k2 = h * (f.subs([(x,(x_0 + (h/2))),(y,(y_0 + (k1/2)))]))
  k3 = h * (f.subs([(x,(x_0 + (h/2))),(y,(y_0 + (k2/2)))]))
  k4 = h * (f.subs([(x,(x_0 + h)),(y, (y_0 + k3))]))
  k = (1/6) * (k1 + (2 * k2) + (2 * k3) + k4)
  y_1 = round((y_0 + k),4)
  x_0 = round(x_0 + h,2)
  x1.append(x_0)
  y1.append(y_1)
  f1.append(f.subs([(x,x_0),(y,y_1)]))
  if x  == x_0:
    break
  print(f'\ny({x_0}) = {y_1}')
  y_0 = y_1


print(f'\nx = {x1}')
print(f'\ny = {y1}')
print(f'\nf = {f1}')

x_0 = x_0 + h
y_p = y1[0] + ((4*h)/3)*((2*f1[1]) - f1[2] + (2*f1[3]))
x1.append(x_0)
y1.append(y_p)
f1.append(f.subs([(x,x_0),(y,y_p)]))
print(f'The Predictor Value is {f.subs([(x,x_0),(y,y_p)])}')


y_c = y1[2] + (h/3) *(f1[2] + (4* f1[3]) + f1[4])
print(f'The Corrector Value is {f.subs([(x,x_0),(y,y_c)])}')

# Adams Predictor Corrector Method

from sympy import *
x,y = symbols('x y')

x_0 = 0
y_0 = 1
x = 0.4
n = 4
h = (x - x_0)/n
f = (2*x*y)/(1 + (x**2))

x1 = []
y1 = []
f1 = []
x1.append(x_0)
y1.append(y_0)
f1.append(f.subs([(x,x_0),(y,y_0)]))


for i in range(1,n):
  k1 = h * (f.subs([(x,x_0),(y,y_0)]))
  k2 = h * (f.subs([(x,(x_0 + (h/2))),(y,(y_0 + (k1/2)))]))
  k3 = h * (f.subs([(x,(x_0 + (h/2))),(y,(y_0 + (k2/2)))]))
  k4 = h * (f.subs([(x,(x_0 + h)),(y, (y_0 + k3))]))
  k = (1/6) * (k1 + (2 * k2) + (2 * k3) + k4)
  y_1 = round((y_0 + k),4)
  x_0 = round(x_0 + h,2)
  x1.append(x_0)
  y1.append(y_1)
  f1.append(f.subs([(x,x_0),(y,y_1)]))
  if x  == x_0:
    break
  print(f'\ny({x_0}) = {y_1}')
  y_0 = y_1


print(f'\nx = {x1}')
print(f'\ny = {y1}')
print(f'\nf = {f1}')

x_0 = x_0 + h
y_p = y1[3] + (h/24) * ( (55 * f1[3]) - (59 * f1[2]) + (37 * f1[1]) - (9 * f1[0]))
x1.append(x_0)
y1.append(y_p)
f1.append(f.subs([(x,x_0),(y,y_p)]))
print(f'The Predictor Value is {f.subs([(x,x_0),(y,y_p)])}')

y_c = y1[3] + (h/24) * ( (9 * f1[4]) + (19 * f1[3]) - (5 * f1[2]) + f1[1])
print(f'The Corrector Value is {f.subs([(x,x_0),(y,y_c)])}')