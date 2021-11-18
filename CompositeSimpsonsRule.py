fa = -.5
fb = .59861

f = [-.5, -.39863, -.5, -.27092, .59861]
def simpson_comp(a,b,n):
  h =(b - a) / n
  XI0 = fa + fb
  XI1 = 0
  XI2 = 0

  for i in range(1,n):
    # X = a + i*h
    if (i%2 == 0):
      XI2 += f[i]
    else:
      XI1 += f[i]
  
  XI = h * (XI0 + 2*XI2 + 4*XI1) / 3
  print(XI)

  return

simpson_comp(-1, 1, 4)