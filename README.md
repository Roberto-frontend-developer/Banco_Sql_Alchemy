# Banco_Sql_Alchemy
Uma aplicação de integração com SQLite usando SQLAlchemy e representar as tabelas do banco de dados relacional para o contexto de Cliente e Conta

# Projeto de Banco de Dados NoSQL com MongoDB

Este projeto demonstra como criar um banco de dados NoSQL usando o MongoDB e realizar operações básicas de conexão, criação de banco de dados, definição de coleção, inserção de documentos e recuperação de informações.

## Pré-requisitos

- [Python](https://www.python.org/) instalado.
- [PyMongo](https://pypi.org/project/pymongo/) instalado.
- Uma conta no [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) configurada.

## Configuração

1. Clone este repositório:

```bash
git@github.com:Roberto-frontend-developer/Banco_Sql_Alchemy.git


Crie um arquivo .env na raiz do projeto com suas credenciais do MongoDB Atlas:

MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/<database-name>?retryWrites=true&w=majority

Instale as dependências:

pip install pymongo

### Executando o Projeto

1. Execute o script Python para criar o banco de dados e inserir documentos:

-python database.py

2.Execute os exemplos de consultas para recuperar informações do banco de dados:

-python queries.py

### Estrutura do Projeto
`database.py`: Código para conectar ao MongoDB Atlas, criar o banco de dados, definir a coleção e inserir documentos.
`queries.py`: Exemplos de consultas para recuperar informações do banco de dados.
`.env`: Arquivo de configuração com as credenciais do MongoDB Atlas





