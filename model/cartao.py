class Cartao:
    def __init__(self, nome):
        self.nome = nome
        self.descricao = ""
        self.comentarios = []
        self.arquivado = False  #So pode ser excluido depois de arquivado, card arquivado nao aparece na listagem
        self.logs = []  #Cada alteraçao feita no arquivo

    def renomear_card(self, novo_nome):
        self.nome = novo_nome

    def alterar_descricao_card(self, nova_descricao):
        self.descricao = nova_descricao

    # def adicionar_comentario

    def arquivar_desarquivar_card(self):
        self.arquivado = not self.arquivado

    def adicionar_log(self, log):
        self.logs.append(log)

    def remover_ultimo_log(self):
        self.logs.pop()
