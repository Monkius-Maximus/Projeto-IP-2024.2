import pygame
from base_peça import Base

class Rainha(Base):
    
    tipo = 'rainha'

    def definir_lances_rainha(self, info_peças):
        """
        Retorna uma lista de coordenadas dos lances possíveis para a rainha
        """
        lances_possíveis = []
        
        # Obtém a posição atual da rainha
        linha_atual, coluna_atual = self.casa
        
        # Direções em que a rainha pode se mover (combinação de torre e bispo)
        direções = [
            (-1, 0),  # Cima
            (1, 0),   # Baixo
            (0, -1),  # Esquerda
            (0, 1),   # Direita
            (-1, -1), # Diagonal cima-esquerda
            (-1, 1),  # Diagonal cima-direita
            (1, -1),  # Diagonal baixo-esquerda
            (1, 1)    # Diagonal baixo-direita
        ]
        
        # Para cada direção...
        for dir_linha, dir_coluna in direções:
            # Verificamos até onde a rainha pode andar nesta direção
            for i in range(1, 8):  # No máximo 7 casas em cada direção
                nova_linha = linha_atual + i * dir_linha
                nova_coluna = coluna_atual + i * dir_coluna
                
                # Verificar se a nova posição está dentro do tabuleiro
                if 0 <= nova_linha <= 7 and 0 <= nova_coluna <= 7:
                    # Verificar se há alguma peça na nova posição
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
        # Obtém os lances possíveis
        lances = self.definir_lances_rainha(info_peças)
        
        # Para cada lance possível, desenha um círculo
        for lance in lances:
            linha, coluna = lance
            tam_casa = tam_tabuleiro / 8
            
            # Converter coordenadas do tabuleiro para coordenadas da tela
            x_centro = coluna * tam_casa + tam_casa / 2
            y_centro = tam_tabuleiro - (linha + 1) * tam_casa + tam_casa / 2
            
            # Desenhar círculo semi-transparente
            pygame.draw.circle(tela, (0, 255, 0, 128), (x_centro, y_centro), tam_casa / 4)