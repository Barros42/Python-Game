from _game._core.local import *
import _game._core.itens as itens

Lc_Jardim = Local(
    "Jardim Inicial", 
    "Você esté em um jardim abandonado com grama alta e carros velhos espalhados pelo jardim \nAo sul você pode ver sua moto sem gasolina\nAo leste e Oeste cercas de madeira bloqueiam a passagem \nAo norte você vê uma casa de madeira extremamente velha, um bilhete pode ser visto pregado em sua porta",
    [itens.BilheteUm, itens.Chave]
)

Lc_CasaVelha = Local(
    "Casa Velha - Corredor",
    "A casa tem cheiro de mofo e poeira, é visivel que ela não é visitada há anos\nAo sul uma porta, ao norte um corredor leva até uma cozinha\nEstá muito escuro aqui",
    [itens.BilheteDois]
)

Lc_Cozinha = Local(
    "Casa Velha - Cozinha",
    "A cozinha tem uma porta ao sul, a oeste uma porta leva para a sala de estar,\nmas está muito escura para enxergar alguma coisa\nao leste uma porta leva para a garagem",
    [itens.LanternaCozinha]
)

Lc_Garagem = Local(
    "Casa Velha - Garagem",
    "Esta garagem é enorme, não dá pra entender o que uma mecânica tão grande faz perdida no meio do nada\nHá algumas bancadas com ferramentas espalhadas\nHá uma enorme porta de ferro a leste, uma porta comum a oeste e muitos carros ao sul"
)

Lc_SalaEstar = Local(
    "Casa Velha - Sala de Estar",
    "Esta sala de estar está extremamente suja",
    None
)
Lc_SalaEstar.escuro = True
Lc_SalaEstar.msgEscuro = "Está muito escuro ali, não consigo enxergar nada"
Lc_SalaEstar.itens = []