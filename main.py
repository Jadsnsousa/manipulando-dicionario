from time import sleep

"""
Esse programa é parte de um estudo sobre CRUD em python, sem utilizar bibliotecas e banco de dados.
É uma forma de entender como manipular os dados. 
É possível criar, alterar, listar e excluir um determinado dado.
"""

dados = dict()

print(f'Iniciando sistema...')
sleep(2)

while True:
    print(f'[ 1 ] Cadastrar Usuário',
          f'\n[ 2 ] Listar Usuários',
          f'\n[ 3 ] Deletar Usuários',
          f'\n[ 4 ] Atualizar Informações',
          f'\n[ 5 ] Sair')
    opcao_menu = str(input('Escolha: '))[0]
    while opcao_menu not in '12345':
        opcao_menu = str(input('Opção invalida. Escolha: '))[0]

    # Cadastrando usuários.
    if opcao_menu == '1':
        print(f'Cadastrando novo usuário...')
        sleep(1.5)
        linha = []
        try:
            nome = str(input('Nome: ')).capitalize()
            idade = int(input('Idade: '))
            linha.append(nome)
            linha.append(idade)
            id_user = str(input('ID: '))
            while id_user in dados:
                id_user = str(input('ID já cadastrado. Digite um novo ID: '))

            dados[f'{id_user}'] = linha.copy()
            print(f'Usuário cadastrado com sucesso.')
            sleep(1.5)
        except:
            print(f'Não foi possível cadastrar o usuário. Tente novamente.')
        linha.clear()


    # Listando usuários.
    elif opcao_menu == '2':
        if len(dados) >= 1:
            print(f'Listando usuários...')
            print(f'Usuarios cadastrados: {len(dados)}')
            sleep(1.5)
            print(f'Usuários: ')
            for itens in dados.values():
                print(itens)

            print('-' * 45)
        else:
            print(f'Não há registros no sistema. Cadastre um usuário e tente novamente.')
            sleep(1.5)


    # Deletando usuários.
    elif opcao_menu == '3':
        print(f'Carregando sistema, aguarde...')
        sleep(1.5)
        if len(dados) < 1:
            print(f'Não há registros no sistema. Cadastre um usuário e tente novamente.')
        else:
            id_user = str(input('Digite o ID do usuário: '))
            confirm = str(input(f'Deletar usuário? [ S ] Sim ou [ N ] Não: '))[0].upper()
            while confirm not in 'SN':
                confirm = str(input(f'Opção invalida. Deletar usuário? [ S ] Sim ou [ N ] Não: '))[0].upper()
            if confirm == 'S':
                dados.pop(f'{id_user}')
                print(f'Usuário deletado com sucesso.')
                sleep(1.5)
            else:
                print(f'Cancelando ação...')
                sleep(1.5)


    # Alterando dados.
    elif opcao_menu == '4':
        print(f'Carregando sistema, aguarde...')
        sleep(1.5)

        if len(dados) < 1:
            print(f'Não há registros no sistema. Cadastre um usuário e tente novamente.')
        else:
            id_user = str(input('Digite o ID do usuário: '))

            print('[ 1 ] Alterar nome',
                  f'\n[ 2 ] Alterar idade',
                  f'\n[ 3 ] Cancelar')
            confirm = str(input('Escolha: '))[0]

            while confirm not in '123':
                print(f'Opção invalida.')
                print('[ 1 ] Alterar nome',
                      f'\n[ 2 ] Alterar idade',
                      f'\n[ 3 ] Cancelar')
                confirm = str(input('Escolha: '))[0]

            if confirm == '1':
                print(f'Alterando nome de usuário...')
                dados[f'{id_user}'][0] = str(input('Nome: ')).capitalize()

            elif confirm == '2':
                print(f'Alterando idade do usuário...')
                dados[f'{id_user}'][1] = (input('Idade: '))

            elif confirm == '3':
                print(f'Cancelando...')
                sleep(1.5)


    # Finalizando o programa.
    elif opcao_menu == '5':
        print(f'Finalizando sistema...')
        break
    print('=' * 50)
    print('\n')
sleep(3)
