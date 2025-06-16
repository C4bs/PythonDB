from pymongo import MongoClient, errors
from bson import objectid

def conectar():
    """
    Função para conectar ao servidor
    """
    conn = MongoClient('localhost', 27017)
    return conn

def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
    if conn:
        conn.close()

def listar():
    """
    Função para listar os produtos
    """
    conn = conectar()
    db = conn.pmongo

    try:
        if db.produtos.count_documents({}) > 0:
            produtos = db.produtos.find()
            print("Listando produtos...")
            print('--------------------------------')
            for produto in produtos:
                print(f"ID: {produtos['_id']}")
                print(f"Produto: {produtos['nome']}")
                print(f"Preço: {produtos['preco']}")
                print(f"Estoque: {produtos['estoque']}")
                print('--------------------------------')
        else:
            print('Não existem produtos cadastrados.')
    except errors.PyMongoError as e:
        print(f'Erro ao acessar o banco de dados: {e}')
    desconectar(conn)

def inserir():
    """
    Função para inserir um produto
    """  
    conn = conectar()
    db = conn.pmongo

    nome =  input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))
    estoque = int(input('Informe o estoque do produto: '))

    try:
        db.produtos.insert_one(
            {
            "nome": nome,
            "preco": preco,
            "estoque": estoque
            }
        )
        print(f"O produto {nome} foi inserido com sucesso!")
    except errors.PyMongoError as e:
        print(f"Erro em inserir o produto. {e}")
    desconectar(conn)

def atualizar():
    """
    Função para atualizar um produto
    """
    

def deletar():
    """
    Função para deletar um produto
    """  
    

def menu():
    """
    Função para gerar o menu inicial
    """
    print('=========Gerenciamento de Produtos==============')
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')