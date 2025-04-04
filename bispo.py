import pygame
from base_peça import Base

class Bispo(Base):
    def __init__(self, cor, casa, tam_tabuleiro, info_peças):
        super().__init__(cor, casa, tam_tabuleiro, info_peças)
        self.tipo = "bispo"
        self.cor_tabuleiro = self.definir_cor_tabuleiro(casa)  # Define automaticamente a cor do tabuleiro

    def definir_cor_tabuleiro(self, casa):
        # Determina se o bispo está em uma casa clara ou escura
        linha, coluna = casa
        return "claro" if (linha + coluna) % 2 == 0 else "escuro"

    def movimentos_possiveis(self, info_peças, tam_tabuleiro):
        # Retorna todas as casas que o bispo pode alcançar, garantindo que ele fique na mesma cor
        movimentos = []
        direcoes = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # Direções diagonais

        for dx, dy in direcoes:
            nova_linha, nova_coluna = self.casa

            while True:
                nova_linha += dx
                nova_coluna += dy

                if 0 <= nova_linha < 8 and 0 <= nova_coluna < 8:  # Verifica se está dentro do tabuleiro
                    # Verifica se a nova casa tem a mesma cor do tabuleiro
                    if self.definir_cor_tabuleiro((nova_linha, nova_coluna)) != self.cor_tabuleiro:
                        break  # Sai do loop se a casa tiver cor diferente

                    if (nova_linha, nova_coluna) in info_peças:
                        if info_peças[(nova_linha, nova_coluna)].cor != self.cor:
                            movimentos.append((nova_linha, nova_coluna))  # Pode capturar peça adversária
                        break  # Para ao encontrar uma peça
                    else:
                        movimentos.append((nova_linha, nova_coluna))  # Casa vazia, pode andar
                else:
                    break  # Saiu do tabuleiro, para

        return movimentos
