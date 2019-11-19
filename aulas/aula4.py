#!/usr/bin/python3


#while

# x = 0
# while x < 10:
#     x += 1
#     print(x)

# x = 1 
# while x <= 10:
#     print(f'numero:{x}')
#     x += 1
# print('O while acabou!')

# a = 500
# while a > 10:
#     a -= 10
#     print(a)


# x = 1 
# while True:
#     print(x)
#     x +=1

# x = 1
# lista = []
# while x < 1000:
#     lista.append(x)
#     x += 1
# print(lista)

# comando FOR

# fruta = ['laranja', 'melancia', 'uva']

# for f in fruta:
#     print(f)


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for var in l:
#     print(var)

#frutas =['abacaxi', 'banana', 'pera', 'maca', 'ameixa']
# for num,frutas in enumerate(frutas):
#     print(num, frutas)

# for item  in  range(10, 0, -1):
#     print(item)

# cont = 0 
# while cont < 10:
#     print(f'vezes de execução {cont + 1}')
#     if cont == 2:
#         print('bloco de condição que interrompe o loop')
#         break
#     cont += 1 

# t = 0 
# while t < 10:
#     print(t)
#     if t == 5:
#         print('continue')
#     t += 1
#     continue

#erros e exceções

# try:
#     if 'mariana' == nome:
#         print('nome correto')
#     else:
#         print ('nome errado')
# except Exception as e:
#   #  print('variavel não atribuida', e)
#     nome ='mariana'
# finally:
#     print(nome)

# try:
#     x = int(input('Digite o primeiro numero: '))
#     y = int(input('Digite o segundo numero: '))
#     print(x + y)
# except ValueError as v:
#     print('esse é um erro', v)

# while True:


#     try:
#         idade = int(input('Digite sua idade:'))
#         if idade < 16:
#             print('Voce não pode comprar bebida alcoolica e nem tirar titulo de eleitor')
#             break
#         else:
#             if idade >= 16 and idade <18:
#                 print('Voce pode ter um titulo de eleitor')
#                 break
#             else:
#                 print('Voce pode comprar bebida e ter um titulo de eleitor')
#                 break
#             break
#     except Exception as e:
#         print('Isso não é um numero', e)
#         continue

# Raise Exception

# while True:
#     try:
#         login = input('Digite o login: ')
#         if login.lower() == 'bryan':
#             raise NameError('Bryan está banido!')
#         else:
#             print(f'Bem vindo {login}, acesso permitido')
#             break
#     except NameError as e:
#         print(e)
#         continue

# try:
#     x =int(input('Digite o primeiro numero:'))
#     y =int(input('Digite o segundo numero:'))
# except Exception as e :
#     print ('Digite apenas numero', e )

# while True:
#     try:
#            x =int(input('Digite o primeiro numero:'))
#            y =int(input('Digite o segundo numero:'))  
#            print ( x +y)
#            break
#     except Exception as e:
#         print('Digite apenas numeros!')
#         continue

# usuarios = ['Ana', 'Caio', 'Felipe']
# try:
#     user = input('Digite o nome de usuario:')
#     if user == 'Ana':
#         raise NameError('Usuario bloqueado!!')
#     else: 
#         print(f'Bem Vindo')
# except NameError as n:
#     print(n)


# try:
#     login = input('Digite seu login:')
#     if login == 'caio':
#         raise NameError ('Usuario banido')
#     else:
#         print(f'Bem Vindo !{login}!')
# except NameError as n:
#     print(n)
# finally:
#     print('finally!!')