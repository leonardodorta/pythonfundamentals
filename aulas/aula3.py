
# Dicionarios

endereco = {'logradouro':'Rua Vergueiro',
            'numero':'3057',
            'bairro':'Vila Mariana',
            'cidade':'são paulo',
            'UF':'SP',
            'cep':'04101-300'
}
endereco_2 = {'logradouro':{'user1': 'Rua vergueiro',
                            'user2': 'Rua augusta'
},
            'numero':{'user1': '3057',
                    'user2': '1050'
            },

            'bairro':{'user1':'Vila Mariana', 'user2': 'cerqueira cesar'},
            'cidade':{'user1':'são paulo','user2': 'são paulo'},
            'UF':{'user1':'SP', 'user2':'SP'},
            'cep':{'user1':'104101-300',   'user2': '01212-030'}            
}
# print(endereco.keys()) # retorna as chaves
# print(endereco.values()) # retorna os valores
# print(endereco_2.items())
# print(endereco_2.keys())
# endereco_2.__setitem__('numero', {'user1': '3057',
#                     'user2': '1030'})
# print(endereco_2)

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



# var_dict = dict(nome='leonardo', sobrenome='dorta')
# var_str = '5'
# var_int = int(var_str)
# var_float = float(var_int)
# print(var_str, var_int, var_float)

#concatenar e inserir dados

# municipio_br = '5.570'
# estados_br = '26'

# brasil = 'O brasil é uma republica federativa formada pela união de {} estados federados,{} municipios e do distrito Federal.'.format(estados_br, municipio_br)
# print(brasil)

# brasil2 = f'O brasil é uma republica federativa formada pela união de, {estados_br}, estados federados,{municipio_br} municipios e do distrito Federal.'
# print(brasil2)

teste = 'teste'
teste2 ='teste2'
print(teste+teste2)
print(teste,teste2)

pais = 'brasil'
print(pais * 3)


num = 4
print(hex(num))




