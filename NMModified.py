import math

def f(x):
  return x**2 * math.log(x+2) - .5

def df(x):
  return 2*x*math.log(x+2) + x**2 / (x+2)

def newton(p0, tol, N):
  i = 1
  while i <= N:
    p = p0 - f(p0) / df(p0)
    print(p)
    if abs(p-p0) < tol:
      print("Newton did it in", i, "iterations")
      return
    i += 1
    p0 = p
  raise TimeoutError("Method failed after", N, "iterations")
  return

newton(1, 10**(-5), 30)
print('\n')

def ddf(x):
  return 120*x**3 + 108*x**2 - 12*x - 12 + 30*x**4

def modNewton(p0, tol, N):
  i = 1
  while i <= N:
    p = p0 - (f(p0)*df(p0)) / (df(p0)**2 - f(p0)*ddf(p0))
    print(p)
    if abs(p-p0) < tol:
      print("Modded Newton did it in", i, "iterations")
      return
    i += 1
    p0 = p
  raise TimeoutError("Method failed after", N, "iterations")
  return

# modNewton(-2.5, 10**(-5), 200)