import math

def f(x):
  return -x**3 - math.cos(x)

def secant(p0, p1, tol, N):
  i = 2
  q0 = f(p0)
  q1 = f(p1)
  while i <= N:
    p = p1 - q1*(p1-p0) / (q1-q0)
    print(p)
    if abs(p1 - p) < tol:
      return
    i += 1
    p0, p1, q0, q1 = p1, p, q1, f(p)
  raise TimeoutError("Method failed after", N, "iterations.")
  return

secant(-1, 0, .00001, 10)
