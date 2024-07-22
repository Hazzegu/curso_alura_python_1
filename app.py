# import this
import os 

restaurantes = [{'Nome':'Sushibar', 'Categoria':'Japonesa', 'Ativo':False},
                {'Nome':'Cebolinha Food', 'Categoria':'Brasileira', 'Ativo':True}]

def show_title():
    print('''
░█▀▀▀█ ─█▀▀█ ░█▀▀█ ░█▀▀▀█ ░█▀▀█ 　 ░█▀▀▀ ▀▄░▄▀ ░█▀▀█ ░█▀▀█ ░█▀▀▀ ░█▀▀▀█ ░█▀▀▀█ 
─▀▀▀▄▄ ░█▄▄█ ░█▀▀▄ ░█──░█ ░█▄▄▀ 　 ░█▀▀▀ ─░█── ░█▄▄█ ░█▄▄▀ ░█▀▀▀ ─▀▀▀▄▄ ─▀▀▀▄▄ 
░█▄▄▄█ ░█─░█ ░█▄▄█ ░█▄▄▄█ ░█─░█ 　 ░█▄▄▄ ▄▀░▀▄ ░█─── ░█─░█ ░█▄▄▄ ░█▄▄▄█ ░█▄▄▄█\n''')

def show_options():
    print('Escolha uma opção: \n')
    print('1 - Cadastrar Restaurante')
    print('2 - Listar Restaurantes')
    print('3 - Alterar Estado Restaurante')
    print('4 - Sair \n')

def exit_app():
    os.system('cls')

    print('Finalizar App \n')

def invalid_option():
    print('Opção inválida \n')

    return_to_main_menu()

def select_options(): 
    try:
        selected_option = int(input('Digite a opção escolhida: \n'))

        match selected_option:
            case 1:
                register_restaurant()
            case 2:
                show_restaurants()
            case 3:
                alter_restaurant_state()
            case 4:
                exit_app()
            case _:
                invalid_option()
    except:
        invalid_option()

def register_restaurant():
    show_subtitle('Cadastro de Restaurantes')
    
    new_restaurant_name = input('Digite o nome do novo restaurante: ')
    new_restaurant_category = input(f'Digite a categoria do restaurante {new_restaurant_name}: ')

    new_restaurant_data = {'Nome':new_restaurant_name, 'Categoria':new_restaurant_category, 'Ativo':False}

    restaurantes.append(new_restaurant_data)

    print('\nRestaurante cadastrado com sucesso!')

    return_to_main_menu()

def show_restaurants():
    show_subtitle('Lista de Restaurantes')
    
    print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | {'Status'.ljust(20)}')
    for restaurante in restaurantes:

        restaurant_name = restaurante['Nome']
        restaurant_category = restaurante['Categoria']
        restaurant_active = 'Ativo' if restaurante['Ativo'] else 'Inativo'

        print(f' - {restaurant_name.ljust(20)} | {restaurant_category.ljust(20)} | {restaurant_active} ')

    return_to_main_menu()

def return_to_main_menu():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def show_subtitle(text): 
    os.system('cls')
    linha = '*' * (len(text))
    print(linha)
    print(text)
    print(linha)

def alter_restaurant_state():
    show_subtitle('Alterando estado do restaurante')

    restaurant_name = input('Digite o nome do restaurante a ser alterado: ')
    restaurant_found : False

    for restaurante in restaurantes:
        if restaurant_name == restaurante['Nome']:
            restaurant_found = True
            restaurante['Ativo'] = not restaurante['Ativo']
            mensagem = f'\nO restaurante {restaurant_name} foi ativado com sucesso' if restaurante['Ativo'] else f'O restaurante {restaurant_name} foi desativado com sucesso'
            print(mensagem)
        if not restaurant_found:
            print('Restauran não encontrado.')

        return_to_main_menu()

def main():
    os.system('cls')
    show_title()
    show_options()
    select_options()

if __name__ == '__main__':
    main()