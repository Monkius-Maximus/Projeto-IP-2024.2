import pygame
class Casa:

    #Método construtor para definir a surface da casa e sua cor.
    def __init__(self, linha, coluna):

        self.peça = '' #Peça que está ocupando a casa.
        self.peça_icon = None
        self.peça_rect = None

        self.tamanho = 100
        self.linha, self.coluna = linha, coluna
        self.surface = ()
        self.pos_x = None
        self.pos_y = None
        self._init_surface()
        self._init_cor()

    #Função para definir a posição da casa na tela do jogo, de acordo com sua linha e coluna.
    def _init_surface(self):
        
        self.pos_x = 100 * self.coluna
        self.pos_y = 800 - (100 * (self.linha + 1))

        self.surface = pygame.Surface((100, 100))

    #Função para inicializar a cor da casa de acordo com sua posição no tabuleiro.
    def _init_cor(self):

        if self.linha % 2 == 0:

            if self.coluna % 2 == 0:

                self.surface.fill((0, 0, 0))
            
            else:

                self.surface.fill((255, 255, 255))
        
        else:

            if self.coluna % 2 == 0:

                self.surface.fill((255, 255, 255))
            
            else:

                self.surface.fill((0, 0, 0))

    #Função para deletar a peça da casa.
    def deletar_peça(self):

        self.peça = ''

    #Função para desenhar a casa.
    def print_surface(self, tela):

        if self.peça != '':

            self.desenhar_peça()

        tela.blit(self.surface, (self.pos_x, self.pos_y))

    #Função para fazer com que uma certa peça passe a ocupar a casa.
    def ocupar_casa(self, peça_nome, dict_icons):
        
        self.peça = peça_nome
        self.peça_icon = dict_icons[peça_nome]
        self.peça_rect = self.peça_icon.get_rect()

        centro_casa = self.surface.get_rect().center
        self.peça_rect.center = centro_casa
        
    #Função para desenhar a peça atual da casa (caso haja alguma).
    def desenhar_peça(self):

        self.surface.blit(self.peça_icon, self.peça_rect)