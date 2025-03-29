import pygame
from base_peça import Base

class Cavalo(Base):
    
    tipo = 'cavalo'

    def definir_lances_cavalo(self, info_peças):
        """
        Retorna uma lista de coordenadas dos lances possíveis para o cavalo
        """
        lances_possíveis = []
        
        # Obtém a posição atual do cavalo
        linha_atual, coluna_atual = self.casa
        
        # O cavalo move-se em "L": 2 casas em uma direção e 1 casa em direção perpendicular
        movimentos = [
            (-2, -1), (-2, 1),  # 2 para cima, 1 para os lados
            (2, -1), (2, 1),    # 2 para baixo, 1 para os lados
            (-1, -2), (-1, 2),  # 1 para cima, 2 para os lados
            (1, -2), (1, 2)     # 1 para baixo, 2 para os lados
        ]
        
        for mov_linha, mov_coluna in movimentos:
            nova_linha = linha_atual + mov_linha
            nova_coluna = coluna_atual + mov_coluna
            
            # Verificar se a nova posição está dentro do tabuleiro
            if 0 <= nova_linha <= 7 and 0 <= nova_coluna <= 7:
                # Verificar se há alguma peça na nova posição
                casa_ocupada = False
                peça_capturável = False
                
                # Verificar em todas as peças se alguma ocupa a nova posição
                for grupo_cor in info_peças:
                    for peça in info_peças[grupo_cor]:
                        if peça.casa == (nova_linha, nova_coluna):
                            casa_ocupada = True
                            # Se a peça é de cor diferente, pode capturar
                            if peça.cor != self.cor:
                                peça_capturável = True
                
                # Se a casa estiver vazia ou com uma peça de cor diferente, adiciona como lance possível
                if not casa_ocupada or peça_capturável:
                    lances_possíveis.append((nova_linha, nova_coluna))
        
        return lances_possíveis
        
    def destacar_lances_possíveis(self, tela, info_peças, tam_tabuleiro):
        # Obtém os lances possíveis
        lances = self.definir_lances_cavalo(info_peças)
        
        # Para cada lance possível, desenha um círculo
        for lance in lances:
            linha, coluna = lance
            tam_casa = tam_tabuleiro / 8
            
            # Converter coordenadas do tabuleiro para coordenadas da tela
            x_centro = coluna * tam_casa + tam_casa / 2
            y_centro = tam_tabuleiro - (linha + 1) * tam_casa + tam_casa / 2
            
            # Desenhar círculo semi-transparente
            pygame.draw.circle(tela, (0, 255, 0, 128), (x_centro, y_centro), tam_casa / 4)