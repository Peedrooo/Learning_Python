from stack import Stack

caracteres = input().split()
pilha_num = Stack()
pilha_str = Stack()

for e in caracteres:
    if e.isnumeric():
        pilha_num.push(e)
    else:
        pilha_str.push(e)

print('Palavras:')
while not(pilha_str.isEmpty()):
    print(pilha_str.pop())

print('')

print('Numeros:')
while not(pilha_num.isEmpty()):
    print(pilha_num.pop())