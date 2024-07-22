# import this
import os 

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

def select_options():
    selected_option = int(input('Digite a opção escolhida: \n'))

    match selected_option:
        case 1:
            print('Cadastrar Restaurante')
        case 2:
            print('Listar Restaurantes')
        case 3:
            print('Ativar Restaurante')
        case 4:
            exit_app()
        case _:
            print('Opção inválida')

def main():
    show_title()
    show_options()
    select_options()

if __name__ == '__main__':
    main()