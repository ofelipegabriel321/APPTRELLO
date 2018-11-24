from card import Card


class Lista:
    def __init__(self, nome):
        self.nome = nome
        self.arquivado = False
        self.cards = []

    def adicionar_card(self, nome): # OK #
        card = Card(nome)
        self.cards.append(card)

    def remover_card(self, card):
        self.cards.remove(card)

    def arquivar_ou_restaurar(self):
        self.arquivado = not self.arquivado
