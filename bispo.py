import pygame
from base_peça import Base

class Bispo(Base):
    
    tipo = 'bispo'
    
    def movimentos_possíveis(self, info_peças, verificar_roque=None):
        
        linha_atual, coluna_atual = self.casa
        cor_bispo = self.cor
        movimentos_possíveis = []
        
        # Junta todas as peças no tabuleiro
        casas_ocupadas = {peça.casa: peça for grupo_cor, peças in info_peças.items() for peça in peças}
        
        # Direções diagonais (somente as do bispo)
        direções = [
            (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]
        
        for d_linha, d_coluna in direções:
            esbarrou = False
            nova_linha, nova_coluna = linha_atual, coluna_atual
            
            while not esbarrou:
                nova_linha += d_linha
                nova_coluna += d_coluna
                
                # Fora do tabuleiro
                esbarrou_fim = not (0 <= nova_linha <= 7) or not (0 <= nova_coluna <= 7)
                esbarrou_peça = (nova_linha, nova_coluna) in casas_ocupadas
                
                if esbarrou_fim or esbarrou_peça:
                    esbarrou = True
                    
                    if esbarrou_peça and casas_ocupadas[(nova_linha, nova_coluna)].cor != cor_bispo:
                        movimentos_possíveis.append((nova_linha, nova_coluna))  # Captura possível
                else:
                    movimentos_possíveis.append((nova_linha, nova_coluna))  # Casa vazia
        
        return movimentos_possíveis
