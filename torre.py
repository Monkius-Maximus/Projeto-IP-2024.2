import pygame
import funcoes_do_jogo as fj
from base_peça import Base

class Torre(Base):

    #O método construtor é herdado da classe Base.
    
    tipo = 'torre'
    movida = False

    #Uma função que retorna os lances possíveis a serem feitos pela Torre, de acordo com as posições de todas as outras peças do tabuleiro. Esta função deve ser acionada quando houver uma tentativa de mover essa torre.
    def movimentos_possíveis(self, info_peças, verificar_roque=None):
        
        linha_atual, coluna_atual = self.casa
        cor_torre = 'brancas' if self.cor in ['branca', 'branco'] else 'pretas'
        movimentos_possíveis = []
        
        #Obtém todas as casas ocupadas no tabuleiro, e associa cada casa à peça que está ocupando essa casa.
        casas_ocupadas = {}

        for grupo_cor, peças in info_peças.items():

            for peça in peças:
                
                casas_ocupadas[peça.casa] = peça

        #Salva as direções possíveis para a torre. Cima, baixo, direita, esquerda. Tudo um quadrado de movimento.
        direções = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        #Para cada deslocamento de linha e de coluna em direções.
        for d_linha, d_coluna in direções:
            
            #Para cada direção que a torre pode ir, devemos checar se ela "esbarrou" em alguma peça. Por exemplo, se ela encontrar uma peça, então ela não poderá ir adiante na mesma direção, pois a torre não atravessa casas. O mesmo se ela esbarrar com o fim do tabuleiro.
            esbarrou = False

            #Essas variáveis estarão sempre atualizadas para checar a próxima casa para a qual a torre pode mover numa determinada direção.
            nova_linha = linha_atual
            nova_coluna = coluna_atual

            while not(esbarrou):
                
                #Move a torre uma casa na direção checada atualmente.
                nova_linha += d_linha
                nova_coluna += d_coluna
                                
                #Se não há mais nenhuma casa para verificar nesta direção, então a torre 'esbarrou' com o fim do tabuleiro. Isso ocorre se a nova linha ou a nova coluna não se encontram no intervalo aceito, que é entre 0 e 7.
                esbarrou_fim = not(0 <= nova_linha <= 7) or not(0 <= nova_coluna <= 7)
                esbarrou_peça = (nova_linha, nova_coluna) in casas_ocupadas.keys()

                #Se esbarrou com o fim do tabuleiro ou se esbarrou com alguma peça.
                if esbarrou_fim or esbarrou_peça:

                    esbarrou = True

                    #Se ele esbarrou em uma peça.                 
                    if esbarrou_peça:

                        #Se esta casa é uma captura possível, e, portanto, um movimento possível.
                        cor_peça_esbarrada = 'brancas' if casas_ocupadas[(nova_linha, nova_coluna)].cor in ['branca', 'branco'] else 'pretas'

                        if cor_peça_esbarrada != cor_torre:

                            movimentos_possíveis.append((nova_linha, nova_coluna))
                
                #Se não há nenhuma peça nesta casa, e a torre ainda não esbarrou com o fim do tabuleiro, e o loop não encontrou nenhuma peça no caminho dela anteriormente, então ela pode ir para esta casa.
                else:

                    movimentos_possíveis.append((nova_linha, nova_coluna))

        return movimentos_possíveis
