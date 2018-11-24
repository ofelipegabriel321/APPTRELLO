class Cartao:
    def __init__(self, nome):
        self.nome = nome
        self.descricao = ""
        self.comentarios = []
        self.etiquetas = []
        self.arquivado = False
        self.logs = []

    def renomear_cartao(self, novo_nome):
        self.nome = novo_nome

    def alterar_descricao(self, nova_descricao):
        self.descricao = nova_descricao

    def arquivar_ou_restaurar(self):
        self.arquivado = not self.arquivado

    def adicionar_comentario(self, comentario):
        self.comentarios.append(comentario)

    def adicionar_ou_remover_etiqueta(self, etiqueta):
        if etiqueta in self.etiquetas:
            self.etiquetas.remove(etiqueta)
        else:
            self.etiquetas.append(etiqueta)

    def adicionar_log(self, log):
        self.logs.append(log)

    def remover_ultimo_log(self):
        self.logs.pop()
