# faça um algoritmo que leia o salario de um funcionário e mostre o seu novo salário, com 15% de aumento

salario = float(input('Qual é o salário do funcionário? R$'))

aumento = salario + (salario * 15 / 100)

print('Um funcionário que ganhava R${:.2f}, Com o reajuste de 15% passará a receber R${:.2f}'.format(salario, aumento))
