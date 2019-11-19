# Manipulando arquivos

# arq1 =  ('../arquivos/sherlock.txt')
# #print(arq1.read()) # mostra conteudo do arquivo
# #print(arq1.tell()) # mostra a quantidade de caracteres
# #print(arq1.seek(3,2))
# print(arq1.read(50))

# arq1.close()

# with open ('arquivo01.txt', 'x') as f:
#     f.write('Abrindo arquivo em python')

# with open(arq1, 'r+') as f:
#     print(f.read())

# Função

# def soma(x, y):
#     print (x + y)
# soma(10,7)
#********************************
# produtos = []
# def cadastraProduto(produto):
#     produtos.append(produto)

# def listarProdutos():
#     for p in produtos:
#         print(p)

# produto = ""
# while produto != "sair":
#     produto = input('Digite o produto que deseja cadastrar: ')
#     cadastraProduto(produto)
#     print('Produtos cadastrados')
#     listarProdutos()
#***********************************

# def primo(num):
# for num in range (2, num):
#     if num % n == 0:
#         print('não é primo')
#         break
#     else:
#         print('é primo')


# def alterbaServidor(atual, novo):
#     print('O Ip autal é: ', atual)
#     print('O nomo IP é: ', novo)

# alterbaServidor('192.168.1.11' , '192.168.1.254')


# def conexao():
#     r = requests.get('https://google.com')
#     print(r.status_code)
# conexao(con)

# def media (x,y):
#     return(x + y)/2
# print(media(10,2))

#**********************************
# def printa(*valores):
#     print(valores[0])
#     print(valores[1])

# printa('nome','sobrenome', 'outros')
#********************
# def printa2(**valores):
#     print(valores)
# printa2(var1='valores', var2='valor2', var3='valor3')

#**********************
texto = ' eusou um cerebo, Watson. O resto é mero apendice'

def split_texto(text):
    return text.split('')

def lower_texto(text):
    return text,lower_texto(texto)
    




