# Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar desconsidere-o.

soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite 0 {} valor: '.format(c)))
    soma += num
    cont += 1
print('Foi informado {} números e a soma é {}.'.format(cont,soma))
