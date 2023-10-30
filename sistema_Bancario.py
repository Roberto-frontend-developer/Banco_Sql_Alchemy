from sqlalchemy import create_engine , Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import random
import string


db_uri = 'sqlite:///banco_de_dados.db'
engine = create_engine(db_uri)


Base = declarative_base()

#Definação  da  class Cliente

class Cliente(Base):
  __tablename__ = 'cliente'

  id = Column(Integer, primary_key=True)
  nome = Column(String)
  cpf = Column(String)
  endereco = Column(String)

  # relacionamento com tabela Conta 

  contas = relationship("Conta", back_populates="cliente")

#Definição da tabela Conta

class Conta(Base):
  __tablename__ = 'conta'

  id = Column(Integer, primary_key=True)
  tipo = Column(String)
  agencia = Column(String)
  num = Column(Integer)
  saldo = Column(DECIMAL)

  id_cliente = Column(Integer, ForeignKey('cliente.id'))

  cliente = relationship("Cliente", back_populates="contas")


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


cpfs_exixtentes = set()
numeros_conta_existentes = set()


def gerar_cpfs():
   while True:
      cpf = ''.join(random.choice(string.digits) for _ in range(11))
      if cpf not in cpfs_exixtentes:
         cpfs_exixtentes.add(cpf)
         return cpf 


def gerar_numero_conta():
   while True:
      numero_conta = ''.join(random.choice(string.digits) for _ in range(5))
      if numero_conta not in numeros_conta_existentes:
         numeros_conta_existentes.add(numero_conta)
         return numero_conta

#Inserir no banco
""" cliente1 = Cliente(nome="Cliente 1", cpf="12345678901", endereco="Endereço 1")
conta1 = Conta(tipo="Corrente", agencia="001", num="12345", saldo=1000.0, cliente=cliente1)
cliente2 = Cliente(nome="Cliente 2", cpf="98765432109", endereco="Endereço 2")
conta2 = Conta(tipo="Poupança", agencia="002", num="54321", saldo=500.0, cliente=cliente2) """

for i in range(3, 13):
    cliente = Cliente(nome=f"Cliente {i}", cpf=f"{i}2345678901", endereco=f"Endereço {i}")
    conta = Conta(tipo="Corrente" if i % 2 == 0 else "Poupança",
                  agencia=f"00{i}",
                  num=gerar_numero_conta(),
                  saldo=1000.0 + (i * 100),
                  cliente=cliente)


session.add(cliente)
session.add(conta)

session.commit()


# Recuperação de dados
clientes = session.query(Cliente).all()
print("Clientes:")
for cliente in clientes:
    print(f"Nome: {cliente.nome}, CPF: {cliente.cpf}, Endereço: {cliente.endereco}")

contas = session.query(Conta).all()
print("\nContas:")
for conta in contas:
    print(f"Tipo: {conta.tipo}, Agência: {conta.agencia}, Número: {conta.num}, Saldo: {conta.saldo}")

# Feche a sessão
session.close()