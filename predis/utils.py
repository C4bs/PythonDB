import redis
import redis.exceptions

def conectar():
    """
    Função para conectar ao servidor
    """
    conn = redis.Redis(host='localhost', port=6379)

    return conn

def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
    conn.connection_pool.disconnect()

def listar():
    """
    Função para listar os produtos
    """
    conn = conectar();

    try:
        dados = conn.keys(pattern='produtos:*')

        if len(dados) > 0:
            print('Listando produtos...')
            print('--------------------')
            for chaves in dados:
                produto = conn.hgetall(chave)
                print(f"ID: {str(chave, 'utf-8', 'ignore')}")
                print(f"Produto: {str(produto[b'nome'], 'utf-8', 'ignore')}")
                print(f"Preço: {str(produto[b'preco'], 'utf-8', 'ignore')}")
                print(f"Estoque: {str(produto[b'estoque'], 'utf-8', 'ignore')}")
        else:
            print('Não existem produtos cadastrados.')
    except redis.exceptions.ConnectionError as e:
        print(f'Não foi possível listar os produtos. {e}')
    desconectar(conn)      

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