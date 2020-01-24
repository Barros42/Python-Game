from _game._core.barreira import Barreira
from _game._core.barreira import Porta
from _game._core.itens import Chave

Br_PortaSemChave = Porta(0,"Porta", False,"A porta está fechada")

Br_PortaComChave = Porta(1,"Porta de Ferro", False, "Esta porta de ferro é enorme e está fechada")
Br_PortaComChave.itemAbrir = Chave
Br_PortaComChave.msgItem = "Você precisa de uma chave para abrir esta porta de ferro"
Br_PortaComChave