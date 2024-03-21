import random

class Carta:
    def _init_(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def _str_(self):
        return f"{self.valor} de {self.naipe}"
