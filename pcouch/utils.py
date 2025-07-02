import socket
import couchdb

def conectar():
    """
    Função para conectar ao servidor
    """
    user = 'admin' # Colocar aqui o usuário criado para o banco
    password = 'admin' # Colocar aqui a senha do usuário criado no banco
    conn = couchdb.Server(f'http://{user}:{password}@localhost:5984')

    banco = 'pcouchdb'

    if banco in conn:
        db = conn[banco]

        return db
    else:
        try:
            db = conn.create[banco]

            return db
        except socket.gaierror as e:
            print(f'Erro ao conectar ao servidor: {e}')
        except couchdb.http.Unauthorized as f:
            print(f'Você não tem permissão ao acesso: {f}')
        except ConnectionRefusedError as g:
            print(f'Não foi possível conectar ao servidor: {g}')


def desconectar():
    """ 
    Função para desconectar do servidor.
    """


def listar():
    """
    Função para listar os produtos
    """
    

def inserir():
    """
    Função para inserir um produto
    """  
    

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