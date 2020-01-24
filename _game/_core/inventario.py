from _game._hud.hud import Hud

class Inventario(object):
    
    hud = Hud()
    itens = []

    def addItem(self, item):
        self.itens.append(item)
    
    def remItem(self, item):
        self.itens.remove(item)

    def listarInventario(self):
        self.hud.listarInventario(self.itens)