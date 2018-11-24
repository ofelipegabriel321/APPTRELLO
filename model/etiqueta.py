from user_interface import *
class Etiqueta:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        self.quadros = []

    def renomear(self, novo_nome):
        self.nome = novo_nome
