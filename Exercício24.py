print('PROGRAMA CIDADE')
cidade=input('Digite o nome da sua cidade ').strip().title().split()
city=' '.join(cidade)
print(city,'Inicia com Santos?','Santos' in cidade[0])
