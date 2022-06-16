def hash(chave, tamanho_tabela):
     soma = 0
     for i in range(len(chave)):
         sum = sum + ord(chave[i])

     return sum % tamanho_tabela 