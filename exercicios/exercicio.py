#!/usr/bin/python3

# Faca um programa que imprima o nome do seu time

#nomedotime = input('Digite o nome do seu time: ')
#
#if nomedotime == ('Sp'):
#    print('acertou')
#    print(nomedotime)

#Faça um program que peça um numero e imprima esse numero

#print(int(input('Digite um numero: ')))

#numero ='5'
#print(type(numero))

#primero_numero =5
#segundo_numero =23
#terceiro_numero =23
#
#print(primero_numero + segundo_numero +terceiro_numero)

linguagem = 'java'

#if linguagem == 'python':
#    print('A linguagem é Python')
#else:
#    print('A linguagem não é python' ' a linguagem é: '+linguagem)


# faca um programa que receba 'F' ou 'M' e moste feminino ou masculino

# sexo = str(input('Digite sexo: '))
# sexo = sexo.capitalize()
# if sexo == ('F'):
#     print('genero femenino')
# elif sexo =='M':
#     print('masculino')
# else:
#     print('genero invalido')

# Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo


# try:
    # numero =int(input('digite um valor: '))
    # if numero >= 0:
        # print('O numero é positivo')
    # else:
        # print('O numero é negativo')
# except ValueError as e:
        # print('Valor não numerico',e)
# 
# 

#data a lista ['Corinthians', [1, 2, 3, 4, 5] ,'Palmeiras', 'São Paulo', [10, 11, 12, 13, 14],'Flamengo', 'Vasco']
#print 3, 13, vasco
#print 5, São paulo, 14
#mudar o valor do 4 = 30
#mudar o valor do 10 = 100
#mudar o valor do 14 = 150
#mudar o valor do vasco = bragatino

# lista = ['Corinthians', [1, 2, 3, 4, 5] ,'Palmeiras', 'São Paulo', [10, 11, 12, 13, 14],'Flamengo', 'Vasco']
# #print(lista[1][2], lista[4][3], lista[6])
# #print(lista[1][-1], lista[3], lista[4][4])
# #lista[1][3] = 30
# lista[4][0]=100
# lista[4][-1]=150
# lista[-1]='Bragantino'
# print(lista)



#tupla

#dicionario

dados = {
    'cidades':{
       'saopaulo':{
           'nome': 'São Paulo',
           'municipios': 645,
           'populacao': 12.18
       },
       'riodejaneiro':{
           'nome': 'Rio de Janeiro',
           'municipios': 92,
           'populacao': 6.32
       },
       'minasgerais':{
           'nome': 'Minas Gerais',
           'municipios': 31,
           'populacao': 20.82
       }
    }

}



#  print a quantidade de municipios de minas
# print(dados['cidades']['minasgerais']['municipios'])
#  print a quantidade de municipios do rio
# print(dados['cidades']['riodejaneiro']['municipios'])
#  print a populacao de minas em milhoes
# print(dados['cidades']['minasgerais']['populacao'] * 1000000)
#  print a populacao de sao paulo em milhoes
# print(dados['cidades']['saopaulo']['populacao'] * 1000000)
#  print o nome de sao paulo
# print(dados['cidades']['saopaulo']['nome'])


# conversão de tipos

# var = 15
#dado a variavel var, peça que usuario digite um numero e mutiplique por var

var = 15
print(int(input('Digite um numero: ')) * var)


