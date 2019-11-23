#################
#    Postgres   #
#################

# import psycopg2
# try:
#     con = psycopg2.connect("host=localhost dbname=projeto user=admin password=4linux")
#     cur = con.cursor()
#     #cur.execute("insert into scripts(nome, conteudo) values('devops', 'projeto de python')")
#     #cur.execute("update scripts set nome='devops_novo' where nome='devops'")
#     #cur.execute("delete from scripts where nome='devops_novo'")
#     cur.execute("select * from scripts")
#     #print(cur.fetchone())
#     #print(cur.fetchall())
#     #con.commit()
#     print('Registro criado com sucesso')
# except Exception as e:
#     print(f'Erro: {e}')
#     print('Fazendo Rollback')
#     con.Rollback()
# finally:
#     print('Finalizando conexao com o banco de dados')
#     cur.close()
#     con.close()

#########################################################

###########
#   mysql #
###########

# import MySQLdb
# try:
#     con = MySQLdb.connect(host="localhost", user="developer", passwd="4linux", db="projetos")
#     cur = con.cursor()
#    cur.execute("insert into clientes(nome,endereco) values ('novo_nome, 'novo_endereco')")
#    # cur.execute("select * from clientes")
#     print(cur.fetchone())
#     print(cur.fetchall())

#     con.commit()
# except Exception as e:
#     print(f'Erro: {e}') 
#     con.rollback()

# finally:
#     print('Finalizando...')
#     cur.close()
#     con.close()


#################################


from pymongo  import MongoClient
cliente = MongoClient('localhost')
db = cliente['dexterops']

def insert_dados():
    try:
        db.fila.insert({"_id":200,
                        "empresa": "4linux",
                        "curso":[{
                                "nome": "Python Fundamentals",
                                "carga horaria":40},
                                {"nome":"Linux Fundamentals",
                                "carga horaria": 40}
                                ]})
    except Exception as e:
        print(f'Erro {e}')

def buscar_dados():
    for r in db.fila.find():
        print(f'Empresa{r["empresa"]}')
        for c in r ["cursos"]:
            print("==============")
            print(f'Nome{c["nome"]} Carga horaria: {c["carga horaria"]}')

    
#insert_dados()
buscar_dados()

# db = cliente['dexterops']
# db.fila.insert({"_id":1,
#                 "servico":"Intranet",
#                 "status": 0})
# db.fila.remove()

