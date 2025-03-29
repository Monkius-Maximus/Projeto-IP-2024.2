import pygame
from base_peça import Base

class Rei(Base):
    
    tipo = 'rei'
    
    def __init__(self, cor, casa, tam_tabuleiro):
        super().__init__(cor, casa, tam_tabuleiro)
        self.movido = False  # Para controlar o roque

    def definir_lances_rei(self, info_peças):
        """
        Retorna uma lista de coordenadas dos lances possíveis para o rei
        """
        lances_possíveis = []
        
        # Obtém a posição atual do rei
        linha_atual, coluna_atual = self.casa
        
        # O rei pode se mover em todas as direções, mas apenas uma casa
        direções = [
            (-1, -1), (-1, 0), (-1, 1),  # Diagonal cima-esquerda, Cima, Diagonal cima-direita
            (0, -1), (0, 1),             # Esquerda, Direita
            (1, -1), (1, 0), (1, 1)      # Diagonal baixo-esquerda, Baixo, Diagonal baixo-direita
        ]
        
        for dir_linha, dir_coluna in direções:
            nova_linha = linha_atual + dir_linha
            nova_coluna = coluna_atual + dir_coluna
            
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
                    # Verificar se a casa não está sob ataque (para evitar mover o rei para um xeque)
                    # Esta verificação seria mais complexa e não está incluída aqui
                    lances_possíveis.append((nova_linha, nova_coluna))
        
        # TODO: Adicionar lógica para o roque
        
        return lances_possíveis
        
    def destacar_lances_possíveis(self, tela, info_peças, tam_tabuleiro):
        # Obtém os lances possíveis
        lances = self.definir_lances_rei(info_peças)
        
        # Para cada lance possível, desenha um círculo
        for lance in lances:
            linha, coluna = lance
            tam_casa = tam_tabuleiro / 8
            
            # Converter coordenadas do tabuleiro para coordenadas da tela
            x_centro = coluna * tam_casa + tam_casa / 2
            y_centro = tam_tabuleiro - (linha + 1) * tam_casa + tam_casa / 2
            
            # Desenhar círculo semi-transparente
            pygame.draw.circle(tela, (0, 255, 0, 128), (x_centro, y_centro), tam_casa / 4)