from cartao import Cartao


class Lista:
    def __init__(self, nome):
        self.nome = nome
        self.arquivado = False
        self.cartoes = []

    def adicionar_cartao(self, nome): # OK #
        cartao = Cartao(nome)
        self.cartoes.append(cartao)

    def remover_card(self, cartao):
        self.cartoes.remove(cartao)

    def arquivar_ou_restaurar(self):
        self.arquivado = not self.arquivado

    def organizar_cartoes(self):
        cartoes_nao_arquivados = []
        for cartao in self.cartoes:
            if not cartao.arquivado:
                cartoes_nao_arquivados.append(cartao)
        cartoes_nao_arquivados.sort(key=lambda cartao: cartao.nome)

        cartoes_arquivados = []
        for cartao in self.cartoes:
            if cartao.arquivado:
                cartoes_arquivados.append(cartao)
        cartoes_arquivados.sort(key=lambda cartao: cartao.nome)

        self.cartoes = cartoes_nao_arquivados + cartoes_arquivados
