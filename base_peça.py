#Função com métodos basilares para todos os tipos de peça do jogo.
class Base: 

    """Um método construtor que define a casa ocupada pela nova torre, assim como seu tipo (caso tenha que ser consultada por alguma função externa) e cor (se é branca ou preta). 

    O formato do input deve ser assim:

    cor = 'branca' ou 'preta'
    casa = (0, 0); (0, 1), etc."""    
    def __init__(self, cor, casa, tam_tabuleiro):

        self.cor = cor
        self.casa = casa

        #A imagem é criada na função main pelo método 'criar_imagem' da classe, de acordo com o icon já importado pelo png. Isso é feito para evitar múltiplas importações de pngs, deixando o aplicativo mais pesado.
        self.imagem = ()
        
        #Define a posição a ser desenhada no tabuleiro, conforme a casa ocupada pela peça. Isso é uma função geral e não um método desta classe, pois tal função poderá ser usada também pelas classes de Peão, Cavalo, Bispo, etc.
        self.pos = self.descobrir_pos(casa, tam_tabuleiro)

    #Move a peça pelo tabuleiro.
    def mover_peça(self, nova_casa):

        self.casa = nova_casa
        self.pos = self.descobrir_pos(nova_casa)

    #Define o icon desenhável de cada peça.
    def definir_peça(self, dict_icons):

        peça_nome = self.tipo + '_' + self.cor
        self.criar_imagem(dict_icons[peça_nome])

    #Função para descobrir a posição na qual uma peça deve ser desenhada, com base na casa que está ocupando.
    def descobrir_pos(self, casa, tam_tabuleiro):

        linha = casa[0]
        coluna = casa[1]

        tam_casa = tam_tabuleiro / 8

        #Primeiro, obtém-se as posições x e y da casa em questão.
        x_casa = coluna * tam_casa
        y_casa = tam_tabuleiro - (linha + 1) * tam_casa

        #Depois, aumenta-se metade do tamanho de uma casa na posição x e o mesmo em y, para obter a posição do centro da casa. 
        x_centro_casa = x_casa + tam_casa / 2
        y_centro_casa = y_casa + tam_casa / 2

        return (x_centro_casa, y_centro_casa)

    #Função para criar a surface desenhável do Pygame a partir do png. 
    def criar_imagem(self, icon):
        
        self.imagem = icon

    #Função para desenhar a peça no tabuleiro.
    def desenhar(self, tela):

        rect = self.imagem.get_rect()
        rect.center = self.pos
        tela.blit(self.imagem, rect)
