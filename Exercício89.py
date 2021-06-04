total = [[[],[]]]
aluno = 0

while True:
    nome = (input('Nome: '))
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    total[aluno][0].append(nome)
    total[aluno][1].append(nota1)
    total[aluno][1].append(nota2)

    aluno += 1

    c = input('Gostaria de continuar? ').strip()
    if c in 'Nn':
        break
    total.append([[],[]])

print('-='*20)
print('ID  NOME     MÉDIA')
for d, c in enumerate(range(len(total))):
    print(f'{d} {total[c][0][0]}     {(total[c][1][0] + total[c][1][1])/2}')
   
id = int(input('Mostrar notas de qual aluno? Digite o id, para cancelar digite 999 '))

while id != 999:
    print(f"As notas de {total[id][0][0]} são {total[id][1][0]} e {total[id][1][1]} ")
    id = int(input('Mostrar notas de qual aluno? Digite o id, para cancelar digite 999 '))

print('FIM DO PROGRAMA')