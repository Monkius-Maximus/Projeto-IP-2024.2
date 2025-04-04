import pygame
from base_peça import Base

class Bispo(Base):
    def __init__(self, cor, casa, tam_tabuleiro, info_peças):
        super().__init__(cor, casa, tam_tabuleiro, info_peças)
        self.tipo = "bispo"
        self.cor_tabuleiro = self.definir_cor_tabuleiro(casa)  # Opcional, só visual

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

                if not (0 <= nova_linha < 8 and 0 <= nova_coluna < 8):
                    break  # Fora do tabuleiro

                pos = (nova_linha, nova_coluna)
                peça_no_caminho = info_peças.get(pos)

                if peça_no_caminho:
                    if peça_no_caminho.cor != self.cor:
                        movimentos.append(pos)  # Pode capturar
                    break  # Para sempre ao encontrar qualquer peça
                else:
                    movimentos.append(pos)  # Casa vazia

        return movimentos
