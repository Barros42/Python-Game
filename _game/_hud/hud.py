class Hud(object):

    def imprimir(self, mensagem):
        print("\n>> " + mensagem + "\n")

    def olharLocal(self, local):
        print("\n ## " + local.nome + " ##")
        self.imprimir(local.descricao)
        if local.itens:
            if(len(local.itens) > 0):
                for item in local.itens:
                    print(item.descricao)
            print("\n")

    def caminhoBloqueado(self):
        self.imprimir("Você não pode ir por ai...")

    def imprimirNome(self, local):
        print("\n ## " + local.nome + " ##\n")

    def impossivelColetar(self):
        self.imprimir("Não há nada assim por aqui")

    def impossivelSoltar(self):
        self.imprimir("Você não tem nada disso")

    def coletarItem(self, item):
        self.imprimir(item.nome.upper() + " : " + item.mensagemPegar)

    def soltarItem(self, item):
        self.imprimir(item.mensagemDeixar)

    def listarInventario(self, itens):
        
        if itens:
            print("\n## INVENTÁRIO ##\n")
            if(len(itens) > 0):
                for item in itens:
                    print(" = " + item.getNomeInventario())
            print("\n")
        else:
            self.imprimir("Inventário vazio!")

    def atitudeEstranha(self):
        self.imprimir("Que atitude estranha...")

    def lerBilhete(self, conteudo):
        print("\n-------------------------")
        self.imprimir(conteudo)
        print("-------------------------\n")

    def soltarTudo(self, inventario):
        print("\n")
        for item in inventario.itens:
            print(">> " + item.mensagemDeixar)
        print("\n")

    def coletarTudo(self, itens):

        print("\n")
        for item in itens:
            print(">> " + item.mensagemPegar)
        print("\n")

    def mensagemInicial(self, mensagem, nome):
        self.imprimir(nome.upper())
        print("-----------------------------")
        self.imprimir(mensagem)
        print("-----------------------------")

    def usouItem(self, item):
        print(">> Você usou => ["+item.nome+"]\n")

    def naoEnxergar(self):
        self.imprimir("Não consigo enxergar")