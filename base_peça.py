#Função com métodos basilares para todos os tipos de peça do jogo.
class Base:

    #Move a peça pelo tabuleiro.
    def mover_peça(self, nova_casa):

        self.casa = nova_casa
        self.pos = self.descobrir_pos(nova_casa)

    #Define o icon desenhável de cada peça.
    def definir_peça(self, dict_icons):

        peça_nome = self.tipo + '_' + self.cor
        self.criar_imagem(dict_icons[peça_nome])

    #Função para descobrir a posição na qual uma peça deve ser desenhada, com base na casa que está ocupando.
    def descobrir_pos(self, casa):

        linha = casa[0]
        coluna = casa[1]

        #Primeiro, obtém-se as posições x e y da casa em questão.
        x_casa = coluna * 100
        y_casa = 800 - (linha + 1) * 100

        #Depois, aumenta-se 50 na posição x e 50 na posição y, para obter a posição do centro da casa.
        x_centro_casa = x_casa + 50
        y_centro_casa = y_casa + 50

        return (x_centro_casa, y_centro_casa)

    #Função para criar a surface desenhável do Pygame a partir do png. 
    def criar_imagem(self, icon):
        
        self.imagem = icon

    #Função para desenhar a peça no tabuleiro.
    def desenhar(self, tela):

        rect = self.imagem.get_rect()
        rect.center = self.pos
        tela.blit(self.imagem, rect)
