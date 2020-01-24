class Bloco(object):

    def __init__(self, conteudo = False):
        self.norte = False
        self.sul = False
        self.oeste = False
        self.leste = False
        self.conteudo = conteudo
        self.visitado = False
