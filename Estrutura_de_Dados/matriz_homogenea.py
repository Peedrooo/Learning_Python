# datas de nascimento:
aluno1 = [5, 10, 1988]
aluno2 = [20, 10, 2003]
aluno3 = [9, 9, 1989]
aluno4 = [27, 10, 2002]

turma_A = [aluno1, aluno2]
turma_E = [aluno3, aluno4]

aniversários = [turma_A, turma_E]

for turma in aniversários:
    for aluno in turma:
        dia,mes,ano = aluno
        print(f'Temos aniversariantes no dia {dia}/{mes}/{ano}')