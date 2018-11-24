from user_interface import *
from quadro import Quadro


class QuadroController:
    def __init__(self):
        self.quadros = []

    def adicionar_quadro(self, nome, cor):
        quadro = Quadro(nome, cor)
        self.quadros.append(quadro)

    def remover_quadro(self, quadro):
        self.quadros.remove(quadro)

    def organizar_quadros(self):
        lista_de_quadros_favoritos = []
        for quadro in self.quadros:
            if quadro.favorito:
                lista_de_quadros_favoritos.append(quadro)
        lista_de_quadros_favoritos.sort(key=lambda quadro: quadro.nome)

        lista_de_quadros_normais = []
        for quadro in self.quadros:
            if not quadro.favorito:
                lista_de_quadros_normais.append(quadro)
        lista_de_quadros_normais.sort(key=lambda quadro: quadro.nome)

        self.quadros = lista_de_quadros_favoritos + lista_de_quadros_normais

    def listar_quadros(self):
        mensagem_de_titulo_de_lista("QUADROS:")
        for indice, quadro in enumerate(self.quadros):
            linha_de_quadro(indice, quadro)

    def acessar_quadro(self, indice_quadro):
        return self.quadros[indice_quadro]

    def indice_existe(self, indice_quadro):
        return 1 <= indice_quadro <= len(self.quadros)
