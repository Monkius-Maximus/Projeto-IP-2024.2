import pygame
from base_peça import Base

class Peão(Base):
    
    #O método construtor é herdado da classe Base.
    
    tipo = 'peão'
    
    def movimentos_possíveis(self, info_peças):
        linha_atual, coluna_atual = self.casa
        cor_peão = self.cor
        movimentos_possíveis = []
        
        # Obtém todas as casas ocupadas no tabuleiro
        casas_ocupadas = {}
        for grupo_cor, peças in info_peças.items():
            for peça in peças:
                casas_ocupadas[peça.casa] = peça
        
        # Define a direção do movimento baseado na cor
        direção = 1 if cor_peão == 'branca' or cor_peão == 'branco' else -1
        
        # Movimento para frente (1 casa)
        nova_linha = linha_atual + direção
        if 0 <= nova_linha <= 7 and (nova_linha, coluna_atual) not in casas_ocupadas:
            movimentos_possíveis.append((nova_linha, coluna_atual))
            
            # Movimento inicial pode ser de 2 casas
            linha_inicial = 1 if cor_peão == 'branca' or cor_peão == 'branco' else 6
            if linha_atual == linha_inicial:
                nova_linha = linha_atual + 2 * direção
                if 0 <= nova_linha <= 7 and (nova_linha, coluna_atual) not in casas_ocupadas:
                    movimentos_possíveis.append((nova_linha, coluna_atual))
        
        # Capturas nas diagonais
        for d_coluna in [-1, 1]:
            nova_linha = linha_atual + direção
            nova_coluna = coluna_atual + d_coluna
            
            if 0 <= nova_linha <= 7 and 0 <= nova_coluna <= 7:
                if (nova_linha, nova_coluna) in casas_ocupadas:
                    peça_alvo = casas_ocupadas[(nova_linha, nova_coluna)]
                    # Verifica se a peça é de cor oposta
                    if (cor_peão == 'branca' or cor_peão == 'branco') and (peça_alvo.cor == 'preta' or peça_alvo.cor == 'preto'):
                        movimentos_possíveis.append((nova_linha, nova_coluna))
                    elif (cor_peão == 'preta' or cor_peão == 'preto') and (peça_alvo.cor == 'branca' or peça_alvo.cor == 'branco'):
                        movimentos_possíveis.append((nova_linha, nova_coluna))

        return movimentos_possíveis
