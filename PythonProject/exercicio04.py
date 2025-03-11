#========== Operadores Aritméticos ==========#

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
#Divisão inteira (di)
di = n1 // n2
#Exponêncial (e)
e = n1 ** n2
#{:.3f} ==>número de casas decimais / end=' '==> colaca o print em uma única linha.
print('A soma é: {}, o produto é: {} e a divisão é: {:.3f}'.format(s,m,d), end=' ')
print('Divisão inteira: {},Potência: {}'.format(di,e))







