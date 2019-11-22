# POO (Herença e polimorfismo)

# class Pai():
#     '''Classe Pai'''
    
#     def __init__(self):
#         self.sobrenome = 'Pereira'

#     def get_sobrenome(self):
#         print(self.sobrenome)

# class Filho(Pai):
#     '''Classe Filho'''
#     def __init__(self):
#         super().__init__()

# joao = Pai()
# joaquim = Filho()
# joaquim.get_sobrenome
#****************************

# class Animal():
#     def __init__(self, raca, idade):
#         self.raca = raca
#         self.idade = idade
#         self.olhos = True
#         self.orgaos = True

#     def Nascer(self):
#         print('Nasceu')

#     def Alimentar (self):
#         print('Se alimentando....')

#     def Morrer(self):
#         print('Morreu')


# class Mamifero():
#     def __init__(self, raca, idade):
#         super().__init__(raca, idade)
#         self.pele = True
#         self.mamilos = True

# class Humano(Mamifero):
#     def __init__(self):
#         super().__init__()
#         self.bracos = 2
#         self.pernas = 2
#         self.cabeca = 1
#         self.tronco = 1
#     def Pensa(self):
#         print('Pensando!!!')
# humano1 = Humano
# humano1.Pensa
#**************************************

# Polimorfismo

class Pai():
    def trabalhar(self):
        print('Trabalhando de engenheiro')

class Filho(Pai):
    def fazernada(self):
        print ('fazendo nada..')
    #def trabalhar(self):
        print('Trabalhando de programador')


joao = Pai()
joao.trabalhar()

joaquim = Filho()
joaquim.trabalhar()


