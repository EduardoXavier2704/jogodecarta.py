import random
from cartas import Carta

class Baralho:
    def __init__(self):
        self.cartas = []
        for naipe in ['Espadas', 'Paus', 'Copas', 'Ouros']:
            for valor in range(2, 15):
                self.cartas.append(Carta(valor, naipe))

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir_cartas(self, jogadores, cartas_por_jogador):
        for jogador in jogadores:
            for _ in range(cartas_por_jogador):
                carta = self.cartas.pop()
                jogador.receber_carta(carta)