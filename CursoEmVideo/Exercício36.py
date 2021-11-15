print('\033[0;33m-=-\033[m'*10)
print('\033[0;34mPROGRAMA EMPRESTIMO\033[m')
print('\033[0;33m-=-\033[m'*10)
valor = int(input('Qual o valor da casa em R$? '))
salario = int(input('Qual a sua renda mensal em R$? '))
tempo = int(input('Em quantos anos gostaria de financiar a casa? '))
custo = (valor/(tempo*12))
if custo <= salario * 30 / 100:
    print(('\033[1;32mEMPRESTIMO LIBERADO\033[m'))
    print(f'Parcelas mensais de R${custo:.2f} reais')
else:
    print('\033[1;31mCRÉDITO NEGADO, tente aumentar o tempo de pagamento\033[m')
    print(f'Parcelas mensais de R${custo:.2f} reais')
