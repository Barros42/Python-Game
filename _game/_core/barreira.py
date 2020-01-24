from _game._hud.hud import Hud

class Barreira(object):
    
    id = int
    nome = str
    estado = bool
    msgFalse = str
    msgItem = str
    hud = Hud()
    itemAbrir = False

    def __init__(self, id, nome, estado, msgFalse):
        self.id = id
        self.nome = nome
        self.estado = estado
        self.msgFalse = msgFalse
    
    def msgErro(self):
        self.hud.imprimir(self.msgFalse)

    def msgItemAbrir(self):
        self.hud.imprimir(self.msgItem)

class Porta(Barreira):
    
    def abrir(self):
        if self.estado == True:
            self.hud.imprimir("A " + self.nome + " já está aberta")
        else:
            self.estado = True
            self.hud.imprimir("Você abriu a " + self.nome)

    def fechar(self):
        if self.estado == False:
            self.hud.imprimir("A "+ self.nome +" já está fechada")
        else:
            self.estado = False
            self.hud.imprimir("Você fechou a " + self.nome)
