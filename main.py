from cartas import Carta
from baralho import Baralho
from jogador import Jogador

def main():
    baralho = Baralho()
    baralho.embaralhar()

    jogadores = [Jogador("Jogador 1"), Jogador("Jogador 2")]
    cartas_por_jogador = 5
    baralho.distribuir_cartas(jogadores, cartas_por_jogador)

    for jogador in jogadores:
        print(f"{jogador.nome}: {jogador.mostrar_cartas()}")

if __name__ == "__main__":
    main()