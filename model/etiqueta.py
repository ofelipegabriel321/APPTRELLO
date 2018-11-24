from user_interface import *
class Etiqueta:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        self.quadros = []

    def alterar_cor(self, nova_cor):
        self.cor = nova_cor
