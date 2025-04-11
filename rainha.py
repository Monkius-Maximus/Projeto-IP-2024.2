import pygame
import funcoes_do_jogo as fj
from base_peça import Base

class Rainha(Base):
    
    tipo = 'rainha'
    
    def movimentos_possíveis(self, info_peças):
        
        linha_atual, coluna_atual = self.casa
        cor_rainha = self.cor
        movimentos_possíveis = []
        
        # Obtém todas as casas ocupadas no tabuleiro e associa cada casa à peça que está nela.
        casas_ocupadas = {peça.casa: peça for grupo_cor, peças in info_peças.items() for peça in peças}
        
        # Direções possíveis para a rainha: combina as direções da torre e do bispo.
        direções = [
            (1, 0), (-1, 0), (0, 1), (0, -1),  # Torre (vertical e horizontal)
            (1, 1), (-1, -1), (1, -1), (-1, 1)  # Bispo (diagonais)
        ]
        
        # Para cada direção que a rainha pode se mover.
        for d_linha, d_coluna in direções:
            esbarrou = False
            nova_linha, nova_coluna = linha_atual, coluna_atual
            
            while not esbarrou:
                nova_linha += d_linha
                nova_coluna += d_coluna
                
                # Verifica se a rainha saiu do tabuleiro.
                esbarrou_fim = not (0 <= nova_linha <= 7) or not (0 <= nova_coluna <= 7)
                esbarrou_peça = (nova_linha, nova_coluna) in casas_ocupadas
                
                if esbarrou_fim or esbarrou_peça:
                    esbarrou = True
                    
                    # Se for uma peça adversária, pode capturar.
                    if esbarrou_peça:

                        cor_rainha_real = 'brancas' if cor_rainha in ['branco', 'branca'] else 'pretas'
                        cor_esbarrada_real = 'brancas' if casas_ocupadas[(nova_linha, nova_coluna)].cor in ['branco', 'branca'] else 'pretas'

                        if cor_rainha_real != cor_esbarrada_real:
                            
                            movimentos_possíveis.append((nova_linha, nova_coluna))
                
                else:
                    movimentos_possíveis.append((nova_linha, nova_coluna))
        
        return movimentos_possíveis
