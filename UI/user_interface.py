from funcionalidades import colorir

def opcao_quadro_controller():
    opcao = int(input("\n*---------+++ QUADRO CONTROLLER +++----------*\n"
                      "|                                            |\n"
                      "| 1 - Criar Quadro                           |\n"
                      "| 2 - Remover Quadro                         |\n"
                      "| 3 - Listar Quadros                         |\n"
                      "| 4 - Favoritar/Desfavoritar Quadro          |\n"
                      "| 5 - Acessar Quadro                         |\n"
                      "|                                            |\n"
                      "| 0 - Sair                                   |\n"
                      "*--------------------------------------------*\n"
                      "Digite a Opção: "))
    return opcao


def opcao_quadro(nome, cor):
    opcao = int(input("\n*----------+++ QUADRO +++-----------*\n"
                      "|                                   |\n"
                      "| 1 - Criar Lista                   |\n"
                      "| 2 - Mover Lista                   |\n"
                      "| 3 - Listar Listas                 |\n"
                      "| 4 - Arquivar/Restaurar Lista      |\n"
                      "| 5 - Excluir Lista Arquivada       |\n"
                      "| 6 - Adicionar Etiqueta            |\n"
                      "| 7 - Acessar Lista                 |\n"
                      "|                                   |\n"
                      "| 0 - Sair                          |\n"
                      "*-----------------------------------*\n"
                      "Quadro '{}{}{}'\n"
                      "Digite a Opção: ".format(colorir(cor), nome, colorir("cor padrao"))))
    return opcao


def opcao_lista(nome_lista, nome_quadro, cor_quadro):
    opcao = int(input("\n*----------+++ LISTA +++-----------*\n"
                      "|                                  |\n"
                      "| 1 - Criar Cartão                 |\n"
                      "| 2 - Mover Cartão                 |\n"
                      "| 3 - Listar Cartões               |\n"
                      "| 4 - Arquivar/Restaurar Cartão    |\n"
                      "| 5 - Excluir Cartão Arquivado     |\n"
                      "| 6 - Alterar Descrição de Cartão  |\n"
                      "| 7 - Comentar no Cartão           |\n"
                      "| 8 - Atividades(Logs)             |\n"
                      "|                                  |\n"
                      "| 0 - Sair                         |\n"
                      "*----------------------------------*\n"
                      "Lista '{}' do Quadro '{}{}{}'\n"
                      "Digite a Opção: ".format(nome_lista,
                                                colorir(cor_quadro),
                                                nome_quadro,
                                                colorir("cor padrao"))))
    return opcao


def opcao_cor():
    opcao = int(input("\n*-----+++ COR +++-----*\n" 
                      "| 1 - {}Verde           {}|\n" 
                      "| 2 - {}Amarelo         {}|\n" 
                      "| 3 - {}Vermelho        {}|\n" 
                      "| 4 - {}Roxo            {}|\n" 
                      "| 5 - {}Azul            {}|\n" 
                      "| 6 - Cor Padrão      |\n" 
                      "*---------------------*\n" 
                      "Digite a cor que deseja: ".format(colorir("verde"),
                                                         colorir("cor padrao"),
                                                         colorir("amarelo"),
                                                         colorir("cor padrao"),
                                                         colorir("vermelho"),
                                                         colorir("cor padrao"),
                                                         colorir("roxo"),
                                                         colorir("cor padrao"),
                                                         colorir("azul"),
                                                         colorir("cor padrao"))))

    return opcao


def continuar_menu():
    input("\nDigite ENTER para Continuar...\n")


def pedir_nome_do_quadro():
    nome = input("Digite o nome do quadro: ")
    return nome


def pedir_nome_da_lista():
    nome = input("Digite o nome da lista: ")
    return nome


def pedir_nome_do_cartao():
    nome = input("Digite o nome do cartão: ")


def pedir_indice():
    num_quadro = int(input("\nDigite o índice: "))
    return num_quadro


def linha_de_quadro(indice, quadro):
    print("{} - {}{}{} {}".format(indice+1,
                                  colorir(quadro.cor),
                                  quadro.nome,
                                  colorir("cor padrao"),
                                  quadro.estrela_de_favorito()))


def linha_de_lista(indice, lista):
    print("{} - {}".format(indice, lista.nome))


def linha_de_etiqueta(indice, etiqueta):
    print("{} - {}({}){}".format(indice,
                                 colorir(etiqueta.cor),
                                 etiqueta.nome,
                                 colorir("cor padrao")))


def mensagem_de_quadro_criado():
    print("QUADRO CRIADO COM SUCESSO!")


def mensagem_de_lista_criada():
    print("LISTA CRIADA COM SUCESSO!")


def mensagem_de_titulo_de_lista(titulo):
    print(titulo)


def mensagem_de_lista_a_mover():
    print("\nLISTA QUE SERÁ MOVIDA:")


def mensagem_de_cartao_a_mover():
    print("\nCARTÃO QUE SERÁ MOVIDO:")


def mensagem_de_quadro_a_receber_lista():
    print("\nQUADRO QUE RECEBERÁ A LISTA:")


def mensagem_de_nome_nao_autenticado():
    print("NOME NÃO AUTENTICADO!!!\n")


def mensagem_de_indice_nao_autenticado():
    print("ÍNDICE NÃO AUTENTICADO!!!\n")


def mensagem_de_senha_incorreta():
    print("SENHA INCORRETA!")


def mensagem_de_cor_incorreta():
    print("COR INCORRETA!")


def mensagem_de_saida():
    print("SAINDO . . .")


def imprimir_item(indice, item):
    print("{} - {}".format(indice, item))
