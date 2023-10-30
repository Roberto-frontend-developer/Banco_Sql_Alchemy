import pymongo

# Substitua as informações a seguir pelas suas credenciais do MongoDB Atlas
mongo_url = "mongodb+srv://<username>:<password>@<cluster-url>/<database-name>?retryWrites=true&w=majority"

# Conecte-se ao MongoDB Atlas
client = pymongo.MongoClient(mongo_url)


# Defina o banco de dados
db = client.get_database("banco_de_dados.db")

# Defina a coleção
colecao = db["bank"]

# Documento 1
documento1 = {
    "nome": "Cliente 1",
    "cpf": "12345678901",
    "endereco": "Endereço 1",
    "contas": [
        {
            "tipo": "Corrente",
            "agencia": "001",
            "numero": "12345",
            "saldo": 1000.0
        },
        {
            "tipo": "Poupança",
            "agencia": "002",
            "numero": "54321",
            "saldo": 500.0
        }
    ]
}

# Documento 2
documento2 = {
    "nome": "Cliente 2",
    "cpf": "98765432109",
    "endereco": "Endereço 2",
    "contas": [
        {
            "tipo": "Corrente",
            "agencia": "003",
            "numero": "67890",
            "saldo": 1500.0
        }
    ]
}

# Insira os documentos na coleção
colecao.insert_many([documento1, documento2])


# Consulta para encontrar um cliente com um determinado CPF
cliente_com_cpf = colecao.find_one({"cpf": "12345678901"})
print("Cliente com CPF 12345678901:")
print(cliente_com_cpf)

# Consulta para encontrar todos os clientes com contas do tipo "Corrente"
clientes_corrente = colecao.find({"contas.tipo": "Corrente"})
print("Clientes com contas corrente:")
for cliente in clientes_corrente:
    print(cliente)

# Consulta para encontrar todos os clientes com saldo maior que 1000
clientes_saldo_maior_1000 = colecao.find({"contas.saldo": {"$gt": 1000}})
print("Clientes com saldo maior que 1000:")
for cliente in clientes_saldo_maior_1000:
    print(cliente)
