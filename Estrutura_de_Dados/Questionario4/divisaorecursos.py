def MDC(x, y):
  while(y != 0):
    resto = x % y
    x = y
    y = resto
  return x
 

g1, g2 = map(int, input().split())
print(MDC(g1, g2))
   
