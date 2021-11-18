import math

def f(x):
  return x**2 * math.log(x+2) - .5

def bisection(a,b,tol,N):
  i = 1
  FA = f(a)
  while i <= N:
    p = a + (b-a)/2
    FP = f(p)

    if FP == 0 or (b-a)/2 < tol:
      print(p)
      return
    i += 1
    if FA*FP > 0:
      a = p
      FA = FP
    else:
      b = p

    print(p)
      
  raise TimeoutError("Method failed after", N, "iterations")
  
  return

bisection(-1,1,10**(-5),18)