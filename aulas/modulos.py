# import aula7 as a7
# joao = a7.Pai()

# #from aula7 import Pai

# print(dir(a7))

import os , sys ,datetime
# os.getlogin = lambda: pwd.getpwuid(os.getuid()[0])
# print(os.getlogin())

#print(os.listdir('/home/developer'))
#print(os.rename('./base.py', 'pandas.py'))
# os.system('echo $USER')

#print(sys.platform)
#print(sys.builtin_module_names)
# print(sys.argv)
# sys.exit()

# for i in range(len(sys.argv)):
#     if i == 0:
#         print(f'Function name: {sys.argv[0]}')
#     else:
#         print(f'Function name: {sys.argv[1]}')

# print(datetime.datetime.now())
# print(datetime.time(14, 0, 0))
# print(datetime.date(2017, 1, 1))

# from datetime import datetime
# acesso = datetime (2019, 10, 12 00,00,00)
# atual = datetime.now()
# if (atual - acesso).total.seconds() >3000:
#     print('Seu token expirou')
# else:
#     print('acesso liberado')



import csv
with open('../arquivos/novo.csv', 'w',) as csvfile:
    arquivo = csv.writer(csvfile, delimiter=',')
    arquivo.writerow(['4linux','Python'])
