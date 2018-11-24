class Log:
    def __init__(self, tipo, origem="", destino=""):
        self.tipo = tipo
        if self.tipo == "mover":
            self.origem = origem
            self.destino = destino
