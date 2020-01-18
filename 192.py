# Fails : 192.py
# Elvijs Buls


from math import sin, cos

def f(x):
	return sin(x)

def f_fwd_diff(x, step):
	return ((f(x + step) - f(x)) / (x + step - x)) * step

def f_fwd_diff2(x, step):
	return f_fwd_diff(x, step) * f_fwd_diff(x, step) * (step * step)

def f_derivative(x):
	return cos(x)

h = 0.01
print("f(x)  = sin(x)")
print("f'(x) = cos(x)")
x0 = int(input("x0 = "))
x1 = int(input("x1 = "))

datu_fails = open("92.dat", "w")

for xv in [x * h for x in range(x0, int(x1 * 1/h))]:
    datu_fails.write("%.4f\t%.4f\t%.4f\t%.12f\n"%(xv, f(xv), f_fwd_diff(xv, h), f_fwd_diff2(xv, h)))


datu_fails.close()
