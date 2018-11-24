def colorir(cor):
    paleta_de_cores = {"verde": "\033[0;32;0m",
                       "amarelo": "\033[0;33;0m",
                       "vermelho": "\033[0;31;0m",
                       "roxo": "\033[0;35;0m",
                       "azul": "\033[0;34;0m",
                       "cor padrao": "\033[0;0;0m"}

    return paleta_de_cores[cor]


def numero_de_cor_existe(cor_em_numero):
    return 1 <= cor_em_numero <= 6


def transformar_numero_de_cor_em_nome_cor(numero_de_cor):
    numeros_de_cor_para_nome_de_cor = {1: "verde",
                                       2: "amarelo",
                                       3: "vermelho",
                                       4: "roxo",
                                       5: "azul",
                                       6: "cor padrao"}
    return numeros_de_cor_para_nome_de_cor[numero_de_cor]
