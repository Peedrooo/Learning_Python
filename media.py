def delta(*x):
  total = sum(x)/len(x)
  print(total)
  for c in range (len(x)):
    y=x[c]-total
    print(round(y,3))
  return ()

delta(4.6,4.52,4.48,4.55,4.59)

# Programa média

a = 4.60
b = 4.52
c = 4.48
d = 4.55
e = 4.59
print((a+b+c+d+e))





