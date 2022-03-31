# funcao primo 
def primo(num):
    if num == 1 : return 'Não primo.' # exceção um 

    for i in range(2,num):
        if num % i == 0: return 'Não primo.'
    return 'Primo.'


