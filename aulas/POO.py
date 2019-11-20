# class Servidor:
#     memoria = None
#     disco = None
#     cpu = None

# dns = Servidor()
# dns.memoria = 2048
# dns.disco =  50
# dns.cpu = 2

# print(f'O servidor tem as seguintes configurações: \nCPU: {dns.cpu}, \nMemoria: {dns.memoria} \nDisco: {dns.disco}')

#********************************************
# class PrimeiraClasse:
#     def __init__(self):
#         print('Acessando o método contrutor')
#     def metodo(self):
#         print('Acessando método')

# classe = PrimeiraClasse()
# classe.metodo()
#*********************************************
class Passaro():
    def __init__(self):
        self.asa = 2
        self.bico = 1
        self.penas = True
        self.patas = 2
        self.rabo = True

    def voar(self):
        self.t = 0
        if self.asa < 2:
            self.t = 1
            print('passaro com problema')

        else:
            print('Passaro voando....')
    def pousar(self):
        print('Pousando...')
    def dormir(self):
        print('Dormindo...')
    def acordar(self):
        print('Acordando...')

sabia = Passaro()
sabia.patas = 1
sabia.asa = 3
sabia.rabo = None

sabia.voar()
sabia.pousar()
sabia.dormir()
sabia.acordar()







