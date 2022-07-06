# pool = list(map(int,input().split()))

from cmath import pi


pool = [3, 4, 5]

for c in range(3):
    print(pool[c]*'+')
    print('+',end='')
    print(' '*(pool[c]-2),end='')
    print('+')
    print(pool[c]*'+')


