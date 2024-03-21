from baralho import Baralho
from cartas import Carta 

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def receber_carta(self, carta):
        self.mao.append(carta)

    def mostrar_cartas(self):
        print(f"{self.nome} possui as seguintes cartas:")
        for carta in self.mao:
            print(f"  {carta}")
