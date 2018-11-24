from lista import Lista
from etiqueta import Etiqueta
from user_interface import *

class Quadro:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        self.listas = []
        self.etiquetas = [Etiqueta("-", "verde"),
                          Etiqueta("-", "amarelo"),
                          Etiqueta("-", "vermelho"),
                          Etiqueta("-", "roxo"),
                          Etiqueta("-", "azul"),
                          Etiqueta("-", "cor padrao")]
        self.favorito = False

    def adicionar_lista(self, nome): # OK #
        lista = Lista(nome)
        self.listas.append(lista)

    def adicionar_lista_criada(self, lista):
        self.listas.append(lista)

    def remover_lista(self, lista):
        self.listas.remove(lista)

    def favoritar_ou_desfavoritar(self):
        self.favorito = not self.favorito

    def estrela_de_favorito(self):
        if self.favorito:
            return "*"
        return ""

    def acessar_lista(self, indice_lista):
        return self.listas[indice_lista]

    def acessar_etiqueta(self, indice_etiqueta):
        return self.etiquetas[indice_etiqueta]

    def organizar_listas(self):
        listas_nao_arquivadas = []
        for lista in self.listas:
            if not lista.arquivado:
                listas_nao_arquivadas.append(lista)

        listas_arquivadas = []
        for lista in self.listas:
            if lista.arquivado:
                listas_arquivadas.append(lista)

        self.listas = listas_nao_arquivadas + listas_arquivadas

    def organizar_listas_arquivadas(self):
        listas_arquivadas = []
        for lista in self.listas:
            if lista.arquivado:
                listas_arquivadas.append(lista)
        listas_arquivadas.sort(key=lambda lista: lista.nome)

        listas_nao_arquivadas = []
        for lista in self.listas:
            if not lista.arquivado:
                listas_nao_arquivadas.append(lista)
        listas_nao_arquivadas.sort(key=lambda lista: lista.nome)

        self.listas = listas_arquivadas + listas_nao_arquivadas

    def listar_listas(self):
        mensagem_de_titulo_de_lista("LISTAS:")
        for indice, lista in enumerate(self.listas):
            if not lista.arquivado:
                linha_de_lista(indice + 1, lista)

    def listar_listas_arquivadas(self):
        mensagem_de_titulo_de_lista("LISTAS ARQUIVADAS:")
        for indice, lista in enumerate(self.listas):
            if lista.arquivado:
                linha_de_lista(indice + 1, lista)

    def listar_etiquetas(self):
        mensagem_de_titulo_de_lista("ETIQUETAS:")
        for indice, etiqueta in enumerate(self.etiquetas):
            linha_de_etiqueta(indice + 1, etiqueta)

    def indice_de_lista_existe(self, indice_lista):
        return 1 <= indice_lista <= len(self.listas)

    def indice_de_etiqueta_existe(self, indice_etiqueta):
        return 1 <= indice_etiqueta <= len(self.etiquetas)


    def botar_na_posicao(self, lista, posicao):
        self.listas.append(lista)
        item_transferido = self.listas[-1]
        posicao_analisada = len(self.listas)
        while posicao_analisada > posicao:
            self.listas[posicao_analisada] = self.listas[posicao - 1]
            posicao_analisada -= 1
        self.listas[posicao] = item_transferido
