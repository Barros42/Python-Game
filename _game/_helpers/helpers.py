from _game._hud.hud import Hud
from _game._core.barreira import Barreira

class Comando(object):

        verbos = [
            "jogar",
            "ir",
            "lancar",
            "pegar",
            "coletar",
            "soltar",
            "deixar",
            "largar"
        ]

        acionador = [
            "ler",
            "ligar",
            "desligar",
            "abrir",
            "fechar"
        ]

        ligacao = [
            "o","a","os","as"
        ]

        def __init__(self, game, comando):
            comando = comando.lower()
            self.comando = comando
            self.game = game
            self.comandoSplit = self.comando.split()

            for palavra in self.acionador:
                self.verbos.append(palavra)

        def interpretar(self):
            
            if self.validar():

                if self.contem("norte") or self.comando == "n":
                    self.game.mapa.irNorte()
                
                if self.contem("sul") or self.comando == "s":
                    self.game.mapa.irSul()
                
                if self.contem("leste") or self.comando == "l":
                    self.game.mapa.irLeste()
                
                if self.contem("oeste") or self.comando == "o":
                    self.game.mapa.irOeste()

                if self.contem("olhar") or self.comando == "ol":
                    self.game.jogador.olhar(self.game.mapa.blocoAtual)

                if self.contem("descrever"):
                    self.game.jogador.olhar(self.game.mapa.blocoAtual)

                if self.contem("pegar") or self.contem("coletar"):
                    self.comando = self.comando.replace("pegar","")
                    self.comando = self.comando.replace("coletar","")
                    self.comando = self.comando.replace("o ","")
                    self.comando = self.comando.replace("a ","")
                    self.comando = self.comando.strip()
                    
                    if self.validarColeta(self.game.mapa.blocoAtual.conteudo, self.comando):
                        self.game.jogador.coletar(self.game.mapa.blocoAtual, self.comando)
                    else:
                        self.game.hud.impossivelColetar()
                
                if self.contem("inventario") or self.comando == "i":
                    self.game.jogador.inventario.listarInventario()
                
                if self.contem("largar") or self.contem("deixar") or self.contem("soltar"):
                    self.comando = self.comando.replace("soltar","")
                    self.comando = self.comando.replace("largar","")
                    self.comando = self.comando.replace("deixar","")
                    self.comando = self.comando.replace("o ","")
                    self.comando = self.comando.replace("a ","")
                    self.comando = self.comando.strip()

                    if self.validarSoltar(self.game.jogador.inventario, self.comando):
                        self.game.jogador.soltar(self.game.mapa.blocoAtual, self.comando)
                    else:
                        self.game.hud.impossivelSoltar()

                if self.ehAcionador():
                    
                    barreiras = self.procurarBarreiras()
                    acionador = self.getVerboAcao()
                    verboAcao = self.getAcionador()

                    for itemInventario in self.game.jogador.inventario.itens:
                        if itemInventario.nome.lower() == acionador:
                            funcao = getattr(itemInventario, str(verboAcao), None)

                            if callable(funcao):
                                funcao()
                                return True
                            else:
                                self.game.hud.atitudeEstranha()
                                return True

                    for itemLocal in self.game.mapa.blocoAtual.conteudo.itens:
                        if itemLocal.nome.lower() == acionador:
                            if itemLocal.acaoEmMaos == False:
                                funcao = getattr(itemLocal, str(verboAcao), None)

                                if callable(funcao):
                                    funcao()
                                    return True
                                else:
                                    self.game.hud.atitudeEstranha()
                                    return True

                    for itemBarreira in barreiras:
                        if itemBarreira.nome.lower() == acionador:
                                
                                temOItem = False
                                if(itemBarreira.itemAbrir is not False):
                                    for itemInventario in self.game.jogador.inventario.itens:
                                        if itemInventario == itemBarreira.itemAbrir:
                                            temOItem = True
                                            break
                                    
                                    if temOItem is False:
                                        itemBarreira.msgItemAbrir()
                                        return False
                                        
                                funcao = getattr(itemBarreira, str(verboAcao), None)
                                
                                if callable(funcao):
                                    funcao()
                                    if itemBarreira.estado == True and temOItem == True:
                                        self.game.jogador.inventario.itens.remove(itemInventario)
                                        self.game.hud.usouItem(itemBarreira.itemAbrir)
                                        itemBarreira.itemAbrir = False

                                    return True
                                else:
                                    self.game.hud.atitudeEstranha()
                                    return True

                    self.game.hud.atitudeEstranha()

        def procurarBarreiras(self):

            corX = self.game.mapa.corX
            corY = self.game.mapa.corY

            possiveisBarreiras = []

            possiveisBarreiras.append(self.game.mapa.andarAtual[corY - 1][corX].conteudo)
            possiveisBarreiras.append(self.game.mapa.andarAtual[corY + 1][corX].conteudo)
            possiveisBarreiras.append(self.game.mapa.andarAtual[corY][corX + 1].conteudo)
            possiveisBarreiras.append(self.game.mapa.andarAtual[corY][corX - 1].conteudo)

            barreiras = []

            for bar in possiveisBarreiras:
                if isinstance(bar, Barreira):
                    barreiras.append(bar)
            
            return barreiras
           
        def getVerboAcao(self):
            
            todasPalavras = self.comandoSplit
           
            palavraRetornar = []
            for palavra in todasPalavras:
                if palavra not in self.verbos and palavra not in self.ligacao:
                    palavraRetornar.append(palavra)
            
            novaPalavra = ""
            for palavra in palavraRetornar:
                novaPalavra = novaPalavra + " " + palavra

            novaPalavra = novaPalavra.strip()

            return novaPalavra

        def getAcionador(self):
            
            todasPalavras = self.comandoSplit

            for palavra in todasPalavras:
                if palavra in self.verbos and palavra not in self.ligacao:
                    palavraRetornar = palavra

            return palavraRetornar

        def ehAcionador(self):

            todasPalavras = self.comandoSplit

            for palavra in todasPalavras:
                if palavra in self.acionador:
                    return True

            return False

        def contem(self, palavra):
            arrayComando = self.comando.split()    
            for comando in arrayComando:
                if palavra == comando:
                    return True
            
            return False

        def letraValida(self):
            
            letrasValidas = [
                'n','s','l','o','i'
            ]

            if self.comando in letrasValidas:
                return True
            else:
                return False

        def palavraValida(self):

            palavrasValidas = [
                'norte', 'sul', 'leste', 'oeste', 'olhar', 'descrever','ol','teste','pegar',
                'inventario', 'soltar', 'largar', 'deixar', 'ler', 'ligar'
            ]

            if self.comando in palavrasValidas:
                return True
            else:
                return False

        def isVazio(self):
            if self.comando == "":
                return True
            else:
                return False

        def procurarVerbo(self):
            
            qtdVerbos = 0

            arrayComando = self.comando.split()

            for mensagem in arrayComando:
                if(mensagem in self.verbos):
                    qtdVerbos = qtdVerbos + 1

            if(qtdVerbos == 0):
                return False
            else:
                return True

        def validar(self):
            
            if len(self.comando) == 1 and self.letraValida():
                return True

            if len(self.comando.split()) == 1:
                if self.palavraValida() is True:
                    return True
                else:
                    self.game.hud.imprimir('Não reconheço a palavra "'+ self.comando +'"')
                    return False

            if self.isVazio():
                self.game.hud.imprimir("Perdão?")
                return False

            if self.procurarVerbo() is False:
                self.game.hud.imprimir("Não há verbo nesta ação")
                return False
            
            return True

        def validarColeta(self, local, item):
            if local.itens:
                if item == "tudo":
                    return True

                for itemLocal in local.itens:
                    if item == itemLocal.nome.lower():
                        return True
                return False
            else:
                return False
        
        def validarSoltar(self, inventario, item):
            
            if item == "tudo":
                return True
            else:
                for itemInventario in inventario.itens:
                    if itemInventario.nome.lower() == item:
                        return True
            return False
            
