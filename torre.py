import pygame
import funcoes_do_jogo as fj
from base_peça import Base

class Torre(Base):

    """Um método construtor que define a casa ocupada pela nova torre, assim como seu tipo (caso tenha que ser consultada por alguma função externa) e cor (se é branca ou preta). 
    
        O formato do input deve ser assim:

        cor = 'branca' ou 'preta'
        casa = (0, 0); (0, 1), etc."""
    def __init__(self, cor, casa):

        self.tipo = 'torre'
        self.cor = cor
        self.casa = casa

        #A imagem é criada na função main pelo método 'criar_imagem' da classe, de acordo com o icon já importado pelo png. Isso é feito para evitar múltiplas importações de pngs, deixando o aplicativo mais pesado.
        self.imagem = ()
        
        #Define a posição a ser desenhada no tabuleiro, conforme a casa ocupada pela peça. Isso é uma função geral e não um método desta classe, pois tal função poderá ser usada também pelas classes de Peão, Cavalo, Bispo, etc.
        self.pos = self.descobrir_pos(casa)
    
