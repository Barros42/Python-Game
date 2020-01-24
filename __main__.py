from _game._core.game import Game
import os

os.system("cls")

novoGame = Game()
novoGame.iniciar()

while(1):
    print("<< ", end =" ")
    novoGame.lerComando(input())