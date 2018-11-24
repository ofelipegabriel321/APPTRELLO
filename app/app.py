from user_interface import *
from funcionalidades import *
from quadro_controller import QuadroController


quadro_controller = QuadroController()

def menu_lista(lista, quadro):
    while True:
        opcao = opcao_lista(lista.nome, quadro.nome, quadro.cor)

        if opcao == 0:
            mensagem_de_saida()
            break
        elif opcao == 1:  #Criar Cartão
            nome = pedir_nome_do_cartao()
            lista.adicionar_cartao(nome)
            mensagem_de_lista_criada()
        elif opcao == 2:  # Mover Cartão
            while True:
                lista.organizar_cartoes
                lista.listar_cartoes
                mensagem_de_cartao_a_mover()
                indice_cartao = pedir_indice()
                if not lista.indice_de_cartao_existe(indice_cartao):
                    mensagem_de_indice_nao_autenticado()
                    continue
                ####
                lista = quadro.acessar_lista(indice_cartao - 1)

                quadro_controller.organizar_quadros()
                quadro_controller.listar_quadros()
                mensagem_de_quadro_a_receber_lista()
                indice_quadro = pedir_indice()
                if not quadro_controller.indice_existe(indice_quadro):
                    mensagem_de_indice_nao_autenticado()
                    continue
                quadro_recipiente = quadro_controller.acessar_quadro(indice_quadro - 1)

                quadro.remover_lista(lista)
                quadro_recipiente.adicionar_lista_criada(lista)

                break
        elif opcao == 3:  # Listar Cartões
            pass
        elif opcao == 4:  # Arquivar/Restaurar Cartão
            pass


def menu_quadro(quadro):
    while True:
        opcao = opcao_quadro(quadro.nome, quadro.cor)

        if opcao == 0:
            mensagem_de_saida()
            break

        elif opcao == 1:  #Criar Lista
            nome = pedir_nome_da_lista()
            quadro.adicionar_lista(nome)
            mensagem_de_lista_criada()

        elif opcao == 2:  #Mover Lista
            while True:
                quadro.organizar_listas()
                quadro.listar_listas()
                mensagem_de_lista_a_mover()
                indice_lista = pedir_indice()
                if not quadro.indice_de_lista_existe(indice_lista):
                    mensagem_de_indice_nao_autenticado()
                    continue
                lista = quadro.acessar_lista(indice_lista - 1)

                quadro_controller.organizar_quadros()
                quadro_controller.listar_quadros()
                mensagem_de_quadro_a_receber_lista()
                indice_quadro = pedir_indice()
                if not quadro_controller.indice_existe(indice_quadro):
                    mensagem_de_indice_nao_autenticado()
                    continue
                quadro_recipiente = quadro_controller.acessar_quadro(indice_quadro - 1)

                quadro.remover_lista(lista)
                quadro_recipiente.adicionar_lista_criada(lista)

                break

        elif opcao == 3:  #Listar Listas
            quadro.organizar_listas()
            quadro.listar_listas()

        elif opcao == 4:  #Arquivar ou Restaurar Lista
            while True:
                quadro.organizar_listas()
                quadro.listar_listas()
                indice_lista = pedir_indice()
                if not quadro.indice_de_lista_existe(indice_lista):
                    mensagem_de_indice_nao_autenticado()
                    continue
                lista = quadro.acessar_lista(indice_lista - 1)
                lista.arquivar_ou_restaurar()

        elif opcao == 5:  # Excluir Lista Arquivada
            while True:
                quadro.organizar_listas_arquivadas()
                quadro.listar_listas_arquivadas()
                indice_lista = pedir_indice()
                if not quadro.indice_de_lista_existe(indice_lista):
                    mensagem_de_indice_nao_autenticado()
                    continue
                lista = quadro.acessar_lista(indice_lista - 1)
                quadro.remover_lista(lista)

        elif opcao == 6:  # Editar Etiqueta
            while True:
                quadro.listar_etiquetas()
                indice_etiqueta = pedir_indice()
                if not quadro.indice_de_etiqueta_existe(indice_etiqueta):
                    mensagem_de_indice_nao_autenticado()
                    continue
                while True:
                    numero_de_cor = opcao_cor()
                    if not numero_de_cor_existe(numero_de_cor):
                        mensagem_de_cor_incorreta()
                        continue
                    cor = transformar_numero_de_cor_em_nome_cor(numero_de_cor)

                    break
                quadro.alterar_cor_de_etiqueta(indice_etiqueta - 1, cor)
                break
        elif opcao == 7:  # Acessar Lista
            while True:
                quadro.listar_listas()
                indice_lista = pedir_indice()
                if not quadro.indice_de_lista_existe(indice_lista):
                    mensagem_de_indice_nao_autenticado()
                    continue
                lista = quadro.acessar_lista(indice_lista - 1)
                menu_lista(lista)
                break

        continuar_menu()


def menu_quadro_controller(quadro_controller):
    while True:
        opcao = opcao_quadro_controller()

        if opcao == 0:
            mensagem_de_saida()
            break
        elif opcao == 1:  # Criar Quadro
            nome = pedir_nome_do_quadro()
            while True:
                numero_de_cor = opcao_cor()
                if not numero_de_cor_existe(numero_de_cor):
                    mensagem_de_cor_incorreta()
                    continue
                cor = transformar_numero_de_cor_em_nome_cor(numero_de_cor)

                break
            quadro_controller.adicionar_quadro(nome, cor)
            mensagem_de_quadro_criado()

        elif opcao == 2:  #Remover Quadro
            while True:
                quadro_controller.organizar_quadros()
                quadro_controller.listar_quadros()
                indice_quadro = pedir_indice()
                if not quadro_controller.indice_existe(indice_quadro):
                    mensagem_de_indice_nao_autenticado()
                    continue
                quadro = quadro_controller.acessar_quadro(indice_quadro - 1)
                quadro_controller.remover_quadro(quadro)
                break

        elif opcao == 3:  #Listar Quadros
            quadro_controller.organizar_quadros()
            quadro_controller.listar_quadros()

        elif opcao == 4:  # Favoritar ou Desfavoritar Quadro
            while True:
                quadro_controller.organizar_quadros()
                quadro_controller.listar_quadros()
                indice_quadro = pedir_indice()
                if not quadro_controller.indice_existe(indice_quadro):
                    mensagem_de_indice_nao_autenticado()
                    continue
                quadro = quadro_controller.acessar_quadro(indice_quadro - 1)
                quadro.favoritar_ou_desfavoritar()
                break

        elif opcao == 5:  #AcessarQuadro
            while True:
                quadro_controller.organizar_quadros()
                quadro_controller.listar_quadros()
                indice_quadro = pedir_indice()
                if not quadro_controller.indice_existe(indice_quadro):
                    mensagem_de_indice_nao_autenticado()
                    continue
                quadro = quadro_controller.acessar_quadro(indice_quadro - 1)
                menu_quadro(quadro)
                break
        continuar_menu()


def main():
    menu_quadro_controller(quadro_controller)


if __name__ == '__main__':
    main()



