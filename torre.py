import pygame
import funcoes_do_jogo as fj
from base_peça import Base

class Torre(Base):
    
    tipo = 'torre'

    #Uma função que retorna os lances possíveis a serem feitos pela Torre, de acordo com as posições de todas as outras peças do tabuleiro. Esta função deve ser acionada quando essa torre for selecionada pelo usuário.
    def definir_lances_torre(self, info_peças):
        
        pass
