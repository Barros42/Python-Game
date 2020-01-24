import _game._core.locais as locais
from _game._core.bloco import Bloco
import _game._core.barreiras as barreiras


    # ESTE É O JARDIM INICIAL PELO QUAL VOCê COMEÇA
Bl_Jardim = Bloco(locais.Lc_Jardim)
Bl_Jardim.norte = True
Bl_Jardim.sul = "Impossível voltar! sua moto está sem combustível"
Bl_Jardim.leste = "Impossível passar! Estas cercas velhas estão no caminho"
Bl_Jardim.oeste = "Impossível passar! Estas cercas velhas estão no caminho"

    # CORREDOR DA CASA ABANDONADA  
Bl_CasaAbandonada = Bloco(locais.Lc_CasaVelha)
Bl_CasaAbandonada.norte = True
Bl_CasaAbandonada.sul = True
Bl_CasaAbandonada.oeste = "Estas paredes fedem..."

    # COZINHA DA CASA ABANDONADA
Bl_CozinhaCasaAbandonada = Bloco(locais.Lc_Cozinha)
Bl_CozinhaCasaAbandonada.oeste = True
Bl_CozinhaCasaAbandonada.sul = True
Bl_CozinhaCasaAbandonada.leste = True
Bl_CozinhaCasaAbandonada.norte = "Esta janela está muito suja"

    # PORTA SEM CHAVE
Bl_PortaSemChave = Bloco(barreiras.Br_PortaSemChave)

    # PORTA COM CHAVE
Bl_PortaComChave = Bloco(barreiras.Br_PortaComChave)

    # GARAGEM ABANDONADA
Bl_GaragemCasaAbandonada = Bloco(locais.Lc_Garagem)
Bl_GaragemCasaAbandonada.sul = "Quantos carros..."
Bl_GaragemCasaAbandonada.norte = "Ele devia gostar mesmo disso, olhe quantas ferramentas"
Bl_GaragemCasaAbandonada.oeste = True
Bl_GaragemCasaAbandonada.leste = True

Bl_SalaEstarCasaAbandonada = Bloco(locais.Lc_SalaEstar)
Bl_SalaEstarCasaAbandonada.sul = "Esta janela está muito suja, mas ainda posso ver o jardim"
Bl_SalaEstarCasaAbandonada.norte = False
Bl_SalaEstarCasaAbandonada.oeste = False 
Bl_SalaEstarCasaAbandonada.leste = True