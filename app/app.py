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

        elif opcao == 1:
            nome = pedir_nome_do_cartao()
            lista.adicionar_cartao(nome)
            mensagem_de_cartao_criado()
            cartao = lista.acessar_cartao(-1)
            log = "Adicionou o cartão '{}' à lista '{}'".format(cartao.nome,
                                                                lista.nome)
            cartao.adicionar_log(log)
            quadro.adicionar_log(log)

        elif opcao == 2:
            while True:
                lista.organizar_cartoes()
                lista.listar_cartoes()
                mensagem_de_cartao_a_mover()
                indice_cartao = pedir_indice()
                if not lista.indice_de_cartao_existe(indice_cartao):
                    mensagem_de_indice_nao_autenticado()
                    continue
                cartao = lista.acessar_cartao(indice_cartao - 1)

                quadro.organizar_listas()
                quadro.listar_listas()
                mensagem_de_lista_a_receber_cartao()
                indice_lista = pedir_indice()
                if not quadro.indice_de_lista_existe(indice_lista):
                    mensagem_de_indice_nao_autenticado()
                    continue
                lista_recipiente = quadro.acessar_lista(indice_lista - 1)

                lista.remover_cartao(cartao)
                lista_recipiente.adicionar_cartao_criado(cartao)

                log = "Moveu o cartão '{}' da lista '{}' para a lista '{}'".format(cartao.nome,
                                                                                   lista.nome,
                                                                                   lista_recipiente.nome)

                cartao.adicionar_log(log)
                quadro.adicionar_log(log)

                break

        elif opcao == 3:
            lista.organizar_cartoes()
            lista.listar_cartoes()

        elif opcao == 4:
            while True:
                lista.organizar_cartoes()
                lista.listar_cartoes()
                lista.listar_cartoes_arquivados()
                indice_cartao = pedir_indice()
                if not lista.indice_de_cartao_existe(indice_cartao):
                    mensagem_de_indice_nao_autenticado()
                    continue
                cartao = lista.acessar_cartao(indice_cartao - 1)
                cartao.arquivar_ou_restaurar()

                if cartao.arquivado:
                    mensagem = "Arquivou"
                else:
                    mensagem = "Restaurou"

                log = "{} cartão '{}' na lista '{}'".format(mensagem,
                                                            cartao.nome,
                                                            lista.nome)
                cartao.adicionar_log(log)
                quadro.adicionar_log(log)

                break

        elif opcao == 5:
            while True:
                lista.organizar_cartoes_arquivados()
                lista.listar_cartoes_arquivados()
                indice_cartao = pedir_indice()
                if not lista.indice_de_cartao_existe(indice_cartao):
                    mensagem_de_indice_nao_autenticado()
                    continue
                cartao = lista.acessar_cartao(indice_cartao - 1)
                lista.remover_cartao(cartao)

                log = "Excluiu o cartão '{}' na lista '{}'".format(cartao.nome,
                                                                   lista.nome)

                cartao.adicionar_log(log)
                quadro.adicionar_log(log)

                break

        elif opcao == 6:
            while True:
                lista.organizar_cartoes()
                lista.listar_cartoes()
                indice_cartao = pedir_indice()
                if not lista.indice_de_cartao_existe(indice_cartao):
                    mensagem_de_indice_nao_autenticado()
                    continue
                cartao = lista.acessar_cartao(indice_cartao - 1)
                nova_descricao = pedir_descricao()
                cartao.alterar_descricao(nova_descricao)

                break

        elif opcao == 7:
            while True:
                lista.organizar_cartoes()
                lista.listar_cartoes()
                indice_cartao = pedir_indice()
                if not lista.indice_de_cartao_existe(indice_cartao):
                    mensagem_de_indice_nao_autenticado()
                    continue
                cartao = lista.acessar_cartao(indice_cartao - 1)
                comentario = pedir_comentario()
                cartao.adicionar_comentario(comentario)

                log = "Comentário '{}' no cartão '{}' na lista '{}'".format(comentario,
                                                                            cartao.nome,
                                                                            lista.nome)

                cartao.adicionar_log(log)
                quadro.adicionar_log(log)

                break

        elif opcao == 8:
            while True:
                lista.organizar_cartoes()
                lista.listar_cartoes()
                indice_cartao = pedir_indice()
                if not lista.indice_de_cartao_existe(indice_cartao):
                    mensagem_de_indice_nao_autenticado()
                    continue
                cartao = lista.acessar_cartao(indice_cartao - 1)

                quadro.listar_etiquetas()
                indice_etiqueta = pedir_indice()
                if not quadro.indice_de_etiqueta_existe(indice_etiqueta):
                    mensagem_de_indice_nao_autenticado()
                    continue
                etiqueta = quadro.acessar_etiqueta(indice_etiqueta - 1)
                cartao.adicionar_ou_remover_etiqueta(etiqueta)

                break

        elif opcao == 9:
            lista.organizar_cartoes()
            lista.listar_cartoes()
            indice_cartao = pedir_indice()
            if not lista.indice_de_cartao_existe(indice_cartao):
                mensagem_de_indice_nao_autenticado()
                continue
            cartao = lista.acessar_cartao(indice_cartao - 1)

            mensagem_de_titulo_de_lista("NOME: " + cartao.nome)
            mensagem_de_titulo_de_lista("DESCRIÇÃO: " + str(cartao.descricao))
            mensagem_de_titulo_de_lista("COMENTÁRIOS: " + "\n".join(cartao.comentarios))
            mensagem_de_titulo_de_lista("ETIQUETAS: " + "\n".join([etiqueta.nome for etiqueta in cartao.etiquetas]))
            mensagem_de_titulo_de_lista("ARQUIVADO: " + cartao.arquivado)
            mensagem_de_titulo_de_lista("LOGS: " + "\n".join(cartao))
            pass

        continuar_menu()


def menu_quadro(quadro):
    while True:
        opcao = opcao_quadro(quadro.nome, quadro.cor)

        if opcao == 0:
            mensagem_de_saida()
            break

        elif opcao == 1:
            nome = pedir_nome_da_lista()
            quadro.adicionar_lista(nome)
            mensagem_de_lista_criada()

            quadro.adicionar_log("Adicionou a lista '{}' a este quadro".format(nome))

        elif opcao == 2:
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
                log = "Moveu lista '{}' do quadro '{}{}{}' para o quadro '{}{}{}'".format(
                    lista.nome,
                    colorir(quadro.cor),
                    quadro.nome,
                    colorir("cor padrao"),
                    colorir(quadro_recipiente.cor),
                    quadro_recipiente.nome,
                    colorir("cor padrao"))
                quadro.adicionar_log(log)

                break

        elif opcao == 3:
            quadro.organizar_listas()
            quadro.listar_listas()

        elif opcao == 4:
            while True:
                quadro.organizar_listas()
                quadro.listar_listas()
                quadro.listar_listas_arquivadas()
                indice_lista = pedir_indice()
                if not quadro.indice_de_lista_existe(indice_lista):
                    mensagem_de_indice_nao_autenticado()
                    continue
                lista = quadro.acessar_lista(indice_lista - 1)
                lista.arquivar_ou_restaurar()

                break
            if lista.arquivado:
                mensagem = "Arquivou"
            else:
                mensagem = "Restaurou"

            log = "{} lista '{}'".format(mensagem, lista.nome)
            quadro.adicionar_log(log)

        elif opcao == 5:
            while True:
                quadro.listar_etiquetas()
                indice_etiqueta = pedir_indice()
                if not quadro.indice_de_etiqueta_existe(indice_etiqueta):
                    mensagem_de_indice_nao_autenticado()
                    continue
                novo_nome = pedir_nome_da_etiqueta()
                etiqueta = quadro.acessar_etiqueta(indice_etiqueta - 1)
                etiqueta.renomear(novo_nome)
                break

        elif opcao == 6:
            while True:
                quadro.listar_listas()
                indice_lista = pedir_indice()
                if not quadro.indice_de_lista_existe(indice_lista):
                    mensagem_de_indice_nao_autenticado()
                    continue
                lista = quadro.acessar_lista(indice_lista - 1)
                menu_lista(lista, quadro)
                break

        elif opcao == 7:
            mensagem_de_titulo_de_lista("LOGS:")
            imprimir_logs(quadro.logs)

        continuar_menu()


def menu_quadro_controller(quadro_controller):
    while True:
        opcao = opcao_quadro_controller()

        if opcao == 0:
            mensagem_de_saida()
            break
        elif opcao == 1:
            nome = pedir_nome_do_quadro()
            while True:
                numero_de_cor = opcao_cor()
                if not numero_de_cor_existe(numero_de_cor):
                    mensagem_de_cor_incorreta()
                    continue
                cor = transformar_numero_de_cor_em_nome_cor(numero_de_cor)

                break
            quadro_controller.adicionar_quadro(nome, cor)

            quadro = quadro_controller.acessar_quadro(-1)
            quadro.adicionar_log("Esse Quadro foi criado")

            mensagem_de_quadro_criado()

        elif opcao == 2:
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

        elif opcao == 3:
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

        elif opcao == 5:
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
