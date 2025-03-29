import pygame
import funcoes_do_jogo as fj
from base_peça import Base

class Torre(Base):
    tipo = 'torre'

    def definir_lances_torre(self, info_peças):
        """
        Define os lances possíveis da torre com base na posição atual e nas posições de outras peças no tabuleiro.
        
        :param info_peças: Dicionário contendo informações sobre todas as peças no tabuleiro.
        :return: Lista de lances possíveis (tuplas de coordenadas).
        """
        # Lista para armazenar os lances possíveis
        lances_possíveis = []
        
        # Obtém a posição atual da torre
        linha_atual, coluna_atual = self.casa
        
        # Direções em que a torre pode se mover: horizontal e vertical
        direções = [
            (-1, 0),  # Cima
            (1, 0),   # Baixo
            (0, -1),  # Esquerda
            (0, 1)    # Direita
        ]
        
        # Para cada direção...
        for dir_linha, dir_coluna in direções:
            # Verificamos até onde a torre pode andar nesta direção
            for i in range(1, 8):  # No máximo 7 casas em cada direção
                nova_linha = linha_atual + i * dir_linha
                nova_coluna = coluna_atual + i * dir_coluna
                
                # Verificar se a nova posição está dentro do tabuleiro
                if 0 <= nova_linha <= 7 and 0 <= nova_coluna <= 7:
                    casa_bloqueada = False
                    peça_capturável = False
                    
                    # Verificar em todas as peças se alguma ocupa a nova posição
                    for grupo_cor in info_peças:
                        for peça in info_peças[grupo_cor]:
                            if peça.casa == (nova_linha, nova_coluna):
                                casa_bloqueada = True
                                # Se a peça é de cor diferente, pode capturar
                                if peça.cor != self.cor:
                                    peça_capturável = True
                    
                    # Se a casa estiver bloqueada por uma peça da mesma cor, para de buscar nessa direção
                    if casa_bloqueada and not peça_capturável:
                        break
                    
                    # Se a casa estiver vazia ou com uma peça de cor diferente, adiciona como lance possível
                    lances_possíveis.append((nova_linha, nova_coluna))
                    
                    # Se houver uma peça capturável, para de buscar nessa direção após adicionar o lance
                    if peça_capturável:
                        break
                else:
                    # Se saiu do tabuleiro, para de buscar nessa direção
                    break

        return lances_possíveis

    def destacar_lances_possíveis(self, tela, info_peças, tam_tabuleiro):
        """
        Destaca os lances possíveis da torre no tabuleiro, desenhando círculos verdes ao redor das casas possíveis.
        
        :param tela: Tela onde o jogo está sendo desenhado.
        :param info_peças: Dicionário contendo informações sobre todas as peças no tabuleiro.
        :param tam_tabuleiro: Tamanho do tabuleiro para calcular a posição das casas.
        :return: Lista de lances possíveis da torre.
        """
        # Obtém os lances possíveis
        lances = self.definir_lances_torre(info_peças)
        
        # Para cada lance possível, desenha um círculo
        for lance in lances:
            linha, coluna = lance
            tam_casa = tam_tabuleiro / 8
            
            # Converter coordenadas do tabuleiro para coordenadas da tela
            x_centro = coluna * tam_casa + tam_casa / 2
            y_centro = tam_tabuleiro - (linha + 1) * tam_casa + tam_casa / 2
            
            # Desenhar círculo semi-transparente
            pygame.draw.circle(tela, (0, 255, 0, 128), (x_centro, y_centro), tam_casa / 4)

        return lances
