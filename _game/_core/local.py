class Local(object):
    
    nome = str
    descricao = str
    itens = []
    escuro = bool
    msgEscuro = str

    def __init__(self, nome, descricao, itens = []):
        self.nome = nome
        self.descricao = descricao
        self.itens = itens

    def addItem(self, item):
        self.itens.append(item)
    
    def remItem(self, item):
        self.itens.remove(item)