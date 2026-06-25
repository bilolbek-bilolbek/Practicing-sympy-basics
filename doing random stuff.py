import sympy as sp

x = sp.symbols('x')

f = x**3 + 2*x**2 - 5*x +1

result = sp.diff(f, x)
print(result)