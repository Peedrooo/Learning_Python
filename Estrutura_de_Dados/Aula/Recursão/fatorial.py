#      +----------------------------------+
#      |                                  |
#      V                                  |
def fatorial(n):                          
    if n == 0:   # caso base              |
        return 1 #                        |
    else:        #                        |
        return n * fatorial(n - 1)  # ----+ recursão