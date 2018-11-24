from cartao import Cartao
from user_interface import *


class Lista:
    def __init__(self, nome):
        self.nome = nome
        self.arquivado = False
        self.cartoes = []

    def adicionar_cartao(self, nome):
        cartao = Cartao(nome)
        self.cartoes.append(cartao)

    def remover_cartao(self, cartao):
        self.cartoes.remove(cartao)

    def adicionar_cartao_criado(self, cartao):
        self.cartoes.append(cartao)

    def arquivar_ou_restaurar(self):
        self.arquivado = not self.arquivado

    def acessar_cartao(self, indice_cartao):
        return self.cartoes[indice_cartao]

    def organizar_cartoes(self):
        cartoes_nao_arquivados = []
        for cartao in self.cartoes:
            if not cartao.arquivado:
                cartoes_nao_arquivados.append(cartao)

        cartoes_arquivados = []
        for cartao in self.cartoes:
            if cartao.arquivado:
                cartoes_arquivados.append(cartao)

        self.cartoes = cartoes_nao_arquivados + cartoes_arquivados

    def organizar_cartoes_arquivados(self):
        cartoes_arquivados = []
        for cartao in self.cartoes:
            if cartao.arquivado:
                cartoes_arquivados.append(cartao)

        cartoes_nao_arquivados = []
        for cartao in self.cartoes:
            if not cartao.arquivado:
                cartoes_nao_arquivados.append(cartao)

        self.cartoes = cartoes_arquivados + cartoes_nao_arquivados

    def listar_cartoes(self):
        mensagem_de_titulo_de_lista("CARTÕES:")
        for indice, cartao in enumerate(self.cartoes):
            if not cartao.arquivado:
                linha_de_cartao(indice + 1, cartao)

    def listar_cartoes_arquivados(self):
        mensagem_de_titulo_de_lista("CARTÕES ARQUIVADOS:")
        for indice, cartao in enumerate(self.cartoes):
            if cartao.arquivado:
                linha_de_lista(indice + 1, cartao)

    def indice_de_cartao_existe(self, indice_cartao):
        return 1 <= indice_cartao <= len(self.cartoes)
