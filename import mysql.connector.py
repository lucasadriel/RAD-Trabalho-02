import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL DB conectado com sucesso!")
    except Error as e:
        print(f"O erro '{e}' ocorreu")

    return connection

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"O erro '{e}' ocorreu")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executada com sucesso!")
    except Error as e:
        print(f"O erro '{e}' ocorreu")

connection = create_connection("localhost", "lucas", "95753515", "BANCO")

#PARA INSERIR OS ATRIBUTOS NA TABELA PESSOA ATRAVÉS DO ARQUIVO DE NOMES, BASTA DESCOMENTAR

# f = open("nomes.txt","r")
# for linha in f:
#  query = linha.replace(" ",",")
#  a = query.split(",")
#  sql = "INSERT INTO Pessoa (cpf, primeiro_nome,nome_do_meio,sobrenome,idade,conta) VALUES ( %s, %s, %s, %s, %s, %s)"
#  val = [(a[0],a[1],a[2],a[3],a[4],a[5])]
#  cursor = connection.cursor()
#  cursor.executemany(sql, val)
#  connection.commit()
 
#PARA INSERIR OS ATRIBUTOS NA TABELA CONTA ATRAVÉS DO ARQUIVO DE NOMES, BASTA DESCOMENTAR

# c = open("contas.txt","r")
# for linha in c:
#  query = linha.replace(" ",",")
#  b = query.split(",")
#  sql = "INSERT INTO Conta (agencia, numero, saldo, gerente, titular) VALUES ( %s, %s, %s, %s, %s)"
#  val = [(b[0],b[1],b[2],b[3],b[4])]
#  cursor = connection.cursor()
#  cursor.executemany(sql, val)
#  connection.commit()

#PARA REALIZAR CONSULTA NA TABELA PESSOA, BASTA DESCOMENTAR

select_users = "SELECT * FROM Pessoa"
users = execute_read_query(connection, select_users)

for user in users:
    print(user)

#PARA REALIZAR CONSULTA NA TABELA CONTA, BASTA DESCOMENTAR

# select_accounts = "SELECT * FROM CONTA"
# accounts = execute_read_query(connection, select_accounts)

# for account in accounts:
#     print(account)

#PARA REALIZAR UMA ATUALIZACAO(UPDATE), BASTA DESCOMENTAR

# update_qualquer = """
# UPDATE
#   Pessoa
# SET
#   primeiro_nome = "Adriel"
# WHERE
#   id_pessoa = 1
# """

# execute_query(connection,  update_qualquer)

#PARA DELETAR UMA TABELA OU UMA LINHA INTEIRA NA TABELA, BASTA DESCOMENTAR 

# delete_qualquer = "DELETE FROM Pessoa WHERE id = 1"
# execute_query(connection, delete_qualquer)