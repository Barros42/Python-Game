from _game._core.item import Item
from _game._core.item import Bilhete
from _game._core.item import Lanterna
from _game._core.item import Chave

BilheteUm = Bilhete(
    0,
    "Bilhete",
    "",
    "Eu queria muito continuar aqui mas não consigo dormir faz dias!\nInfelizmente vou ter que me mudar para a cidade\nSe você é um cliente meu, me procure no (19) 98128-1830\nAss: Barros, o mecânico",
    "Você pegou o bilhete",
    "Você deixou o bilhete",
    "Impossivel pegar! Está grudado na porta!",
    False
)

BilheteDois = Bilhete(
    1,
    "Bilhete sangrento",
    "Há um Bilhete sangrento aqui",
    "Você não devia ter entrado...\n Eu te avisei, infelizmente não há mais volta agora",
    "Você pegou o bilhete sangrento",
    "Você soltou o bilhete sangrento",
    "Impossível coletar",
    True
)

LanternaCozinha = Lanterna(
    2,
    "Lanterna",
    "Há uma lanterna aqui",
    None,
    "Você pegou a lanterna",
    "Você soltou a lanterna",
    None,
    True
)
LanternaCozinha.acaoEmMaos = True

Chave = Chave(
    3,
    "Chave",
    "Há uma chave aqui",
    None,
    "Você pegou uma chave",
    "Você deixou uma chave",
    None,
    True
)