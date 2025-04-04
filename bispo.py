import pygame
from base_peça import Base

class Bispo(Base):
    def __init__(self, cor, casa, tam_tabuleiro, info_peças):
        super().__init__(cor, casa, tam_tabuleiro, info_peças)
        self.tipo = "bispo"
        self.cor_tabuleiro = self.definir_cor_tabuleiro(casa)  # Ainda pode deixar isso se quiser, mas não é necessário pro movimento

    def definir_cor_tabuleiro(self, casa):
        linha, coluna = casa
        return "claro" if (linha + coluna) % 2 == 0 else "escuro"

    def movimentos_possíveis(self, info_peças):
        movimentos = []
        direcoes = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # Direções diagonais

        for dx, dy in direcoes:
            nova_linha, nova_coluna = self.casa

            while True:
                nova_linha += dx
                nova_coluna += dy

                if 0 <= nova_linha < 8 and 0 <= nova_coluna < 8:

                    if (nova_linha, nova_coluna) in info_peças:
                        if info_peças[(nova_linha, nova_coluna)].cor != self.cor:
                            movimentos.append((nova_linha, nova_coluna))  # Pode capturar peça adversária
                        break  # Para ao encontrar qualquer peça
                    else:
                        movimentos.append((nova_linha, nova_coluna))  # Casa vazia
                else:
                    break  # Fora do tabuleiro

        return movimentos
