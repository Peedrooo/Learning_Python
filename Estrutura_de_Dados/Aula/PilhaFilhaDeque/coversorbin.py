from stack import Stack

def conversor_decimal_bin(DecNumber):
    S = Stack()

    while DecNumber > 0 :
        rem = DecNumber%2
        DecNumber = DecNumber//2
        S.push(rem)
    
    bin = ''
    while not S.isEmpty():
        bin = bin + str(S.pop())
    return bin

    
print(conversor_decimal_bin(50))