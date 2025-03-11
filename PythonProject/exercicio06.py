# Crie um algorítmo que leia um número inteiro e mostre ,o dobro,o triplo e a raiz quadrada.
n = int(input('Digite um número: '))
print('O dobro de: {} vale: {}'.format(n, (n*2)))
print('O triplo  de {} vale: {} e \nA raiz quadrada de {} é igual a {:.2f}.'.format(n,(n*3),n,(n**(1/2))))
# (pow)==> também pode calcular a raiz quadrada de um número é só substituir por (pow(n , (1/2)))
