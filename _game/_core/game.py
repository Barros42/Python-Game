from _game._core.mapa import Mapa
from _game._helpers import helpers
from _game._core.jogador import Jogador
from _game._hud.hud import Hud
from _game._helpers.mensagens import Mensagens

class Game(object):
    
    nome = "A CABANA ABANDONADA"
    hud = Hud()
    jogador = Jogador()
    mapa = Mapa(jogador)
    mensagens = Mensagens()
    

    def iniciar(self):
        self.hud.mensagemInicial(self.mensagens.inicial(), self.nome)

    def lerComando(self, comando):
        helpers.Comando(self, comando).interpretar()
