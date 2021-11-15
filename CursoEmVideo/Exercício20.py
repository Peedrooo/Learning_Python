print('ORDER OF APRESENTATION')
from random import shuffle
students=[]
students.append(input('Nome do primeiro aluno '))
students.append(input('Nome do segundo aluno '))
students.append(input('Nome do terceiro aluno '))
students.append(input('Nome do quarto aluno '))
shuffle(students)
print (students)
