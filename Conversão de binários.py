import os

num = int(input('Digite um número inteiro: '))

print('Escolha umas das bases para conversão:\n[ 1 ]Converter para binário\n[ 2 ]Converter para octal\n[ 3 ]Converter para Hexadecimal')
opcao = int(input('Digite a opção desejada: '))

os.system('cls')

if opcao == 1:
    print('{} convertido para binário é igual à {}'.format(num, bin(num)[2:]))
    
    input()
elif opcao == 2:
    print('{} convertido para octal é igual à {}'.format(num, oct(num)[2:]))
    
    input()
elif opcao == 3:
    print('{} convertido para hexadecimal é igual à{}'.format(num, hex(num)[2:]))
    
    input()
else:
    print('Escolha uma opção!')
    
    input()