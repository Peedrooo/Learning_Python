print('PROGRAM ICM')
altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))
icm = peso / altura**2
print(f'Seu ICM é de {icm:.2f}')
if icm <= 18.5:
    print('Abaixo o peso MAGRESA') 

elif 18.5 < icm <= 25:
    print('Peso ideal NORMAL')

elif 25 < icm <= 30:
    print('Sobrepeso OBI')

elif 30 < icm <= 40:
    print('Obesidade OBII')

else:
    print('Obesidade Mórbida OBIII')

