import math

def f(x):
  return 3**(-x)

def FPI(p0, tol, N):
  i = 1
  while i <= N:
    p = f(p0)
    print(p)
    if abs(p -p0) < tol:
      return
    i += 1
    p0 = p
  raise TimeoutError("Method failed after", N, "iterations.")
  return


def steff(p0, tol, N):
  i = 1
  while i <= N:
    p1 = f(p0)
    p2 = f(p1)
    p = p0 - (p1 - p0)**2 / (p2 - 2*p1 + p0)
    print(p)
    if abs(p -p1) < tol:
      return
    i += 1
    p0 = p
  raise TimeoutError("Method failed after", N, "iterations.")
  return

steff(2, 10**(-5), 9)