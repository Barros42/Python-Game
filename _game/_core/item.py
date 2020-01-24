from _game._hud.hud import Hud

class Item(object):
    
    codigo = int
    nome = str
    descricao = str
    conteudo = str
    mensagemPegar = str
    mensagemDeixar = str
    mensagemPreso = str
    coletavel = False
    acaoEmMaos = False
    hud = Hud()

    def __init__(self, codigo, nome, descricao, conteudo, mensagemPegar, mensagemDeixar, mensagemPreso = "Impossível coletar", coletavel = False):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.conteudo = conteudo
        self.mensagemPegar = mensagemPegar
        self.mensagemDeixar = mensagemDeixar
        self.mensagemPreso = mensagemPreso
        self.coletavel = coletavel

    def coletar(self):
        if self.coletavel is False:
            self.hud.imprimir(self.nome.upper() + " : " + self.mensagemPreso)
            return False
        else:
            return True
    
    def getNomeInventario(self):
        return self.nome

class Bilhete(Item):

    def ler(self):
        self.hud.lerBilhete(self.conteudo)

class Lanterna(Item):
    
    estado = False

    def ligar(self):
        if self.estado:
            self.hud.imprimir("A lanterna já está ligada")
        else:
            self.estado = True
            self.hud.imprimir("Você ligou a lanterna")
    
    def desligar(self):
        if self.estado is False:
            self.hud.imprimir("A lanterna já está desligada")
        else:
            self.estado = False
            self.hud.imprimir("Você desligou a lanterna")
    
    def getNomeInventario(self):
        if(self.estado):
            estado = " (Ligada)"
        else:
            estado = " (Desligada)"
        
        return self.nome + estado

class Chave(Item):
    pass