# Fails : 190.py
# Elvijs Buls
# 

from math import sin, cos

def f(x):
	return sin(x)

def f_fwd_diff(x, step):
	return ((f(x + step) - f(x)) / (x + step - x)) * step

def f_derivative(x):
	return cos(x)

h = 0.01
print("f(x)  = sin(x)")
print("f'(x) = cos(x)")
x0 = int(input("x0 = "))
x1 = int(input("x1 = "))

print("f(x)\tf'(x)")
for xv in [x * h for x in range(x0, int(x1 * 1/h))]:
    print("%.4f\t%.4f\t%.4f"%(xv, f(xv), f_fwd_diff(xv, h)))
