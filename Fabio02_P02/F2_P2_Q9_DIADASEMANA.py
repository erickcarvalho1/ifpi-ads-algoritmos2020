#Leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda etc.), se digitar outro  aparece valor invalido

dia = int(input('Digite o número correspondente ao dia semana: '))

if dia == 1:
    print('Domingo')

elif dia == 2:
    print('Segunda')

elif dia == 3:
    print('Terça')

elif dia == 4:
    print('Quarta')

elif dia == 5:
    print('Quinta')

elif dia == 6:
    print('Sexta')

elif dia == 7:
    print('Sábado')

else:
    print('Valor inválido')