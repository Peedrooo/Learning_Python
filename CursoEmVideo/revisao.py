# import datetime
'''
int 9 , 6 , 5 
float 9.0 , 6.0 , 5.0
str "9" , "6" , "5"
bool True False
'''

'''
nome = input("Qual o seu nome ")
sobre = input("Qual o seu sobrenome ")
idade = input("Qual a sua idade ")


print(nome + sobre + idade)
'''
'''
a = int(input("Número1: "))
b = int(input("Número2: "))

c = a - b
print("A subtração entre",a ,"e",b,"resulta",c)
'''
'''
ano = datetime.date.today().year
nasc = int(input("ano de nascimento: "))
print("Sua idade é ",ano - nasc)
'''

dado = input("Digite um valor: ")

print(f"{dado} é {dado.isspace()}") 
