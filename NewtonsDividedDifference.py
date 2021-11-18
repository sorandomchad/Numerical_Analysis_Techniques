import numpy as np

def divDiff(x, y, x0 = None):
  n = len(x)
  F = np.zeros((n,n))
  for i in range(n):
    F[i,0] = y[i]

  for i in range(1,n):
    for j in range(1,i+1):
      F[i,j] = (F[i][j-1] - F[i-1][j-1]) / (x[i] - x[i-j])
  print(F)
  return

x = [-3.72,2.2]
y = [2.6503,2.5]
divDiff(x, y)