import math

def f(x):
  return x**2 * math.log(x+2) - .5

def fixedPoint(p0, TOL, N):
  i = 1

  while i <= N:
    p = f(p0)
    if abs(p-p0) < TOL:
      print(p)
      print("Fixed point found in", i, "iterations")
      return
    i += 1
    p0 = p
  
    print(p)

  raise TimeoutError("Method failed after", N, "iterations")
  return

fixedPoint(-1,10**(-6),14)