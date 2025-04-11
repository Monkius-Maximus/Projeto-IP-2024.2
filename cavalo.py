import pygame
from base_peça import Base

class Cavalo(Base):

    tipo = 'cavalo'

    def movimentos_possíveis(self, info_peças, verificar_roque=None):

        linha_atual, coluna_atual = self.casa
        cor_cavalo = self.cor
        movimentos_possíveis = []

        # Todas as combinações possíveis de movimento em "L"
        deslocamentos = [
            (2, 1), (2, -1),
            (-2, 1), (-2, -1),
            (1, 2), (1, -2),
            (-1, 2), (-1, -2)
        ]

        # Junta todas as peças no tabuleiro
        casas_ocupadas = {peça.casa: peça for grupo_cor, peças in info_peças.items() for peça in peças}

        for d_linha, d_coluna in deslocamentos:
            nova_linha = linha_atual + d_linha
            nova_coluna = coluna_atual + d_coluna

            if 0 <= nova_linha <= 7 and 0 <= nova_coluna <= 7:
                destino = (nova_linha, nova_coluna)

                if destino not in casas_ocupadas:
                    movimentos_possíveis.append(destino)
                elif casas_ocupadas[destino].cor != cor_cavalo:
                    movimentos_possíveis.append(destino)

        return movimentos_possíveis
