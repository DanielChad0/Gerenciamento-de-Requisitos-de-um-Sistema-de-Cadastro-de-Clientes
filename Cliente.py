clientes = {}

def adicionar_cliente():
    email = input('Insira o email: ')
    if email in clientes:
        print('Cliente já cadastrado!')
        return adicionar_cliente
    else: 
        nome = input('Insira o nome: ')
        telefone = input('Insira o telefone: ')
        endereco = input('Insira o endereço: ')

    clientes[email] = {
        'Nome': nome,
        'Telefone': telefone,
        'Email': email,
        'Endereço': endereco
    } 
    print('Cliente cadastrado com sucesso!')

def buscar_cliente():
    email = input('Informe o email do cliente: ')
    if email in clientes:
        cliente = clientes[email]
        print(f'Nome: {cliente['Nome']}')
        print(f'Email: {cliente['Email']}')
        print(f'Endereço: {cliente['Endereço']}')
        print(f'Telefone: {cliente['Telefone']}')
    else:
        print('Cliente não registrado: ')

def exibir_clientes():
     for cliente in clientes.values():
        print(cliente)

def remover_cliente():
    email = input("Digite o e-mail do cliente a ser removido: ")
    if email in clientes:
        del clientes[email]
        print("Cliente removido com sucesso!")
    else:
        print("Cliente não encontrado.")

def menu():
    while True:
        print('''
    menu:
        (1) Adicionar cliente
        (2) Buscar cliente
        (3) Exibir cliente
        (4) Remover cliente
        (5) Sair
''')
        escolha = input('Escolha uma opção:')
        if escolha == '1':
            adicionar_cliente()
        elif escolha == '2':
            buscar_cliente()
        elif escolha == '3':
            exibir_clientes()
        elif escolha == '4':
            remover_cliente()
        elif escolha == '5':
            print('Saindo...')
            break
        else:
            print('Opção inválida!')
resultado = menu()
print(resultado)

