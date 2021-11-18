import numpy as np

def neville(x0, x, y):
  n = len(x)
  Q = np.zeros((n,n))
  for i in range(n):
    Q[i,0] = y[i]
  for i in range(1,n):
    for j in range(1,i+1):
      Q[i,j] = ((x0 - x[i-j])*Q[i,j-1] - (x0 - x[i])*Q[i-1][j-1]) / (x[i] - x[i-j])
  print(Q)

x = [-.25, .25, -.5, .5]
y = [1.33203, .800781, 1.93750, .687500]
neville(0,x,y)