import pygame
from base_peça import Base

class Peao(Base):
    
    tipo = 'peao'
    
    def __init__(self, cor, casa, tam_tabuleiro):
        super().__init__(cor, casa, tam_tabuleiro)
        self.primeiro_movimento = True  # Para controlar o movimento duplo

    def definir_lances_peao(self, info_peças):
        """
        Retorna uma lista de coordenadas dos lances possíveis para o peão
        """
        lances_possíveis = []
        
        # Obtém a posição atual do peão
        linha_atual, coluna_atual = self.casa
        
        # Direção de movimento depende da cor do peão
        direção = 1 if self.cor in ['preta', 'preto'] else -1
        
        # Movimento para frente (1 casa)
        nova_linha = linha_atual + direção
        nova_coluna = coluna_atual
        
        # Verificar se a casa à frente está dentro do tabuleiro
        if 0 <= nova_linha <= 7:
            # Verificar se a casa à frente está vazia
            casa_bloqueada = False
            for grupo_cor in info_peças:
                for peça in info_peças[grupo_cor]:
                    if peça.casa == (nova_linha, nova_coluna):
                        casa_bloqueada = True
            
            # Se a casa à frente estiver vazia, o peão pode se mover para lá
            if not casa_bloqueada:
                lances_possíveis.append((nova_linha, nova_coluna))
                
                # Movimento duplo no primeiro lance
                if self.primeiro_movimento:
                    nova_linha_dupla = linha_atual + 2 * direção
                    # Verificar se a segunda casa à frente está dentro do tabuleiro
                    if 0 <= nova_linha_dupla <= 7:
                        # Verificar se a segunda casa à frente está vazia
                        casa_bloqueada_dupla = False
                        for grupo_cor in info_peças:
                            for peça in info_peças[grupo_cor]:
                                if peça.casa == (nova_linha_dupla, nova_coluna):
                                    casa_bloqueada_dupla = True
                        
                        # Se a segunda casa à frente estiver vazia, o peão pode se mover para lá
                        if not casa_bloqueada_dupla:
                            lances_possíveis.append((nova_linha_dupla, nova_coluna))
        
        # Movimento de captura (diagonal)
        for deslocamento_coluna in [-1, 1]:
            nova_linha = linha_atual + direção
            nova_coluna = coluna_atual + deslocamento_coluna
            
            # Verificar se a casa diagonal está dentro do tabuleiro
            if 0 <= nova_linha <= 7 and 0 <= nova_coluna <= 7:
                # Verificar se há uma peça do adversário na diagonal
                for grupo_cor in info_peças:
                    for peça in info_peças[grupo_cor]:
                        if peça.casa == (nova_linha, nova_coluna) and peça.cor != self.cor:
                            lances_possíveis.append((nova_linha, nova_coluna))
        
        # TODO: Adicionar lógica para en passant
        
        return lances_possíveis
        
    def destacar_lances_possíveis(self, tela, info_peças, tam_tabuleiro):
        # Obtém os lances possíveis
        lances = self.definir_lances_peao(info_peças)
        
        # Para cada lance possível, desenha um círculo
        for lance in lances:
            linha, coluna = lance
            tam_casa = tam_tabuleiro / 8
            
            # Converter coordenadas do tabuleiro para coordenadas da tela
            x_centro = coluna * tam_casa + tam_casa / 2
            y_centro = tam_tabuleiro - (linha + 1) * tam_casa + tam_casa / 2
            
            # Desenhar círculo semi-transparente
            pygame.draw.circle(tela, (0, 255, 0, 128), (x_centro, y_centro), tam_casa / 4)