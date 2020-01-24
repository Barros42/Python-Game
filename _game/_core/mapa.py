from _game._core.bloco import Bloco
import _game._core.blocos as blocos
from _game._hud.hud import Hud
from _game._core.barreiras import *
from _game._core.local import Local

class Mapa(object):
    
    primeiroAndar = []
    corX = int
    corY = int
    blocoAtual = ""
    andarAtual = ""
    hud = Hud()
    jogador = object

    def __init__(self, jogador):
        self.jogador = jogador
        for i in range(10):
            self.primeiroAndar.append([Bloco()] * 10)
            i = i

        self.primeiroAndar[0][4] = blocos.Bl_Jardim
        self.primeiroAndar[1][4] = blocos.Bl_CasaAbandonada
        self.primeiroAndar[2][4] = blocos.Bl_CozinhaCasaAbandonada
        self.primeiroAndar[2][5] = blocos.Bl_PortaSemChave
        self.primeiroAndar[2][6] = blocos.Bl_GaragemCasaAbandonada
        self.primeiroAndar[2][7] = blocos.Bl_PortaComChave
        self.primeiroAndar[2][3] = blocos.Bl_SalaEstarCasaAbandonada

        self.corY = 2
        self.corX = 4
        self.andarAtual = self.primeiroAndar
        self.blocoAtual = self.andarAtual[self.corY][self.corX]
        self.andarAtual[self.corY][self.corX].visitado = True

    def tentarMovimento(self, direcao):
        
        if direcao == "norte":
            caminho = self.blocoAtual.norte
            objetoValidar = self.andarAtual[self.corY + 1][self.corX].conteudo
        elif direcao == "sul":
            caminho = self.blocoAtual.sul
            objetoValidar = self.andarAtual[self.corY - 1][self.corX].conteudo
        elif direcao == "leste":
            caminho = self.blocoAtual.leste
            objetoValidar = self.andarAtual[self.corY][self.corX + 1].conteudo
        elif direcao == "oeste":
            caminho = self.blocoAtual.oeste
            objetoValidar = self.andarAtual[self.corY][self.corX - 1].conteudo

        if isinstance(self.blocoAtual.conteudo, Local):
            if self.blocoAtual.conteudo.escuro == True:
                if self.jogador.temItem("Lanterna", True) is False:
                    self.hud.naoEnxergar()
                    return False


        if isinstance(objetoValidar, Barreira):
            if objetoValidar.estado is False:
                objetoValidar.msgErro()
                return False
            else:
                if direcao == "norte":
                    self.corY = self.corY + 1
                elif direcao == "sul":
                    self.corY = self.corY - 1
                elif direcao == "leste":
                    self.corX = self.corX + 1
                elif direcao == "oeste":
                    self.corX = self.corX - 1
                return True
        elif isinstance(caminho, str):
            self.hud.imprimir(caminho)
            return False
        elif caminho is False:
            self.hud.caminhoBloqueado()
            return False
        elif caminho is True:
            if objetoValidar.escuro == True:
                if self.jogador.temItem("Lanterna",True):
                    return True
                else:
                    self.hud.imprimir(objetoValidar.msgEscuro)
                    return False
            else:
                return True
        return True



    def irNorte(self):
        if self.tentarMovimento("norte"):
            self.corY = self.corY + 1
            self.atualizarCoordenadas()

    def irSul(self):
        if self.tentarMovimento("sul"):
            self.corY = self.corY - 1
            self.atualizarCoordenadas()

    def irLeste(self):
        if self.tentarMovimento("leste"):
            self.corX = self.corX + 1
            self.atualizarCoordenadas()

    def irOeste(self):
        if self.tentarMovimento("oeste"):
            self.corX = self.corX - 1
            self.atualizarCoordenadas()

    def atualizarCoordenadas(self):
               
        self.blocoAtual = self.andarAtual[self.corY][self.corX]
        
        if self.blocoAtual.visitado == False:
            self.blocoAtual.visitado = True
            self.hud.olharLocal(self.blocoAtual.conteudo)
        else:
            self.hud.imprimirNome(self.blocoAtual.conteudo)
        
    def testeMapa(self):
        for linha in self.andarAtual:
            for bloco in linha:
                print (bloco, end = " ")
            print("\n")

