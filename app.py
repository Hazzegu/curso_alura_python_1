# import this
import os 

restaurantes = ['sushibar','cebolinha food']

def show_title():
    print('''
░█▀▀▀█ ─█▀▀█ ░█▀▀█ ░█▀▀▀█ ░█▀▀█ 　 ░█▀▀▀ ▀▄░▄▀ ░█▀▀█ ░█▀▀█ ░█▀▀▀ ░█▀▀▀█ ░█▀▀▀█ 
─▀▀▀▄▄ ░█▄▄█ ░█▀▀▄ ░█──░█ ░█▄▄▀ 　 ░█▀▀▀ ─░█── ░█▄▄█ ░█▄▄▀ ░█▀▀▀ ─▀▀▀▄▄ ─▀▀▀▄▄ 
░█▄▄▄█ ░█─░█ ░█▄▄█ ░█▄▄▄█ ░█─░█ 　 ░█▄▄▄ ▄▀░▀▄ ░█─── ░█─░█ ░█▄▄▄ ░█▄▄▄█ ░█▄▄▄█\n''')

def show_options():
    print('Escolha uma opção: \n')
    print('1 - Cadastrar Restaurante')
    print('2 - Listar Restaurantes')
    print('3 - Ativar Restaurante')
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
                print('Ativar Restaurante')
            case 4:
                exit_app()
            case _:
                invalid_option()
    except:
        invalid_option()

def register_restaurant():
    show_subtitle('Cadastro de Restaurantes')
    
    new_restaurant = input('Digite o nome do novo restaurante: ')

    restaurantes.append(new_restaurant)

    print('\nRestaurante cadastrado com sucesso!')

    return_to_main_menu()

def show_restaurants():
    show_subtitle('Lista de Restaurantes')
    
    for restaurante in restaurantes:
        print(f'.{restaurante}')

    return_to_main_menu()

def return_to_main_menu():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def show_subtitle(text): 
    os.system('cls')
    print(f'\n{text}\n')

def main():
    os.system('cls')
    show_title()
    show_options()
    select_options()

if __name__ == '__main__':
    main()