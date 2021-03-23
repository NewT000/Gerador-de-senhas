import string 
from pyautogui import alert 
from time import sleep 
from random import choice 

continuar = '1' 

titulo = 'GERADOR DE SENHA'

print('=-' * 20)
print(titulo.center(40))
print('=-' * 20)

def arquivo(): #Função para criar um arquivo .txt com as senhas (O arquivo vai ser gerado na pasta do script)
    arquivo = open("Senhas-Geradas.txt", "a")
    arquivo.write(f'{site} => {senha}\n')

while continuar == '1':    
    valores = string.ascii_letters + string.digits 
    senha = ""
    opcoes = ['1', '2', '3'] 

    print('''Escolha o tamanho da senha
    [1] - 5 caractéres
    [2] - 10 caractéres
    [3] - 15 caractéres''')

    tamanho = str(input('Digite o tamanho da senha: '))

    while tamanho not in opcoes:
        tamanho = str(input('Digite um número válido: '))

    site = str(input('Site que a senha vai ser usada: '))
    print('=-' * 20)

    tamanho = int(tamanho) * 5 

    for i in range(int(tamanho)):
        senha += choice(valores)

    print('Gerando sua senha')
    sleep(1)
    print(f'Sua senha é: {senha}')

    print('''
    [1] - Para continuar
    [2] - Para sair
    ''')

    arquivo() 

    continuar = str(input('Continuar? '))
    
    while continuar not in opcoes[0:2]:
        continuar = str(input('Digite uma opção válida: '))
        
    print('-=' * 20)

alert('Foi gerado um arquivo.txt com as senhas e os sites usados.') 
