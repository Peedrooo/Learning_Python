print('PRGRAMA ESCOLAR')
nota1 = float(input('Qual a primeira nota? '))
nota2 = float(input('Qual a segunda nota? '))
media = (nota1 + nota2) / 2
if media >= 7: 
    print(f'Nota {media:.2f} superior a 7, aluno \033[1;34mAPROVADO\033[m')
elif 7 > media >= 5:
    print(f'Nota {media:.2f} iferior a 7, aluno de \033[1;33mRECUPERAÇÃO\033[m')
else:
    print(f'Nota {media:.2f} insuficiente para recuperação, aluno \033[1;31mREPROVADO\033[m')