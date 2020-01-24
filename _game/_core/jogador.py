from _game._core.local import Local
from _game._hud.hud import Hud
from _game._core.inventario import Inventario

class Jogador(object):

    inventario = Inventario()
    hud = Hud()

    def olhar(self, blocoAtual):
        if isinstance(blocoAtual.conteudo, Local):
            self.hud.olharLocal(blocoAtual.conteudo)
            
    def descrever(self, blocoAtual):
        if isinstance(blocoAtual.conteudo, Local):
            self.hud.olharLocal(blocoAtual.conteudo)

    def coletar(self, blocoAtual, item):
        
        if(item == "tudo"):
            
            itensRemover = []

            for itemLocal in blocoAtual.conteudo.itens:
                if itemLocal.coletar():
                    itensRemover.append(itemLocal)
                    self.inventario.addItem(itemLocal)
                    self.hud.coletarItem(itemLocal)
            
            for itemRem in itensRemover:
                blocoAtual.conteudo.remItem(itemRem)
        else:
            for itemLocal in blocoAtual.conteudo.itens:
                if itemLocal.nome.lower() == item.lower():
                    if itemLocal.coletar():
                        self.inventario.addItem(itemLocal)
                        blocoAtual.conteudo.remItem(itemLocal)
                        self.hud.coletarItem(itemLocal)
        
    def soltar(self, blocoAtual, item):

        if(item == "tudo"):
            for itemInventario in self.inventario.itens:
                blocoAtual.conteudo.addItem(itemInventario)
                
            self.hud.soltarTudo(self.inventario)
            self.inventario.itens.clear()
        else:
            for itemInventario in self.inventario.itens:
                if itemInventario.nome.lower() == item:
                    self.inventario.remItem(itemInventario)
                    blocoAtual.conteudo.addItem(itemInventario)
                    self.hud.soltarItem(itemInventario)

    def temItem(self, item, estado = None):
        for itemInventario in self.inventario.itens:
            if itemInventario.nome.lower() == item.lower():
                if estado != None:
                    if itemInventario.estado == estado:
                        return True
                    else:
                        return False
                else:
                    return True

        return False