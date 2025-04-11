#Função com métodos basilares para todos os tipos de peça do jogo.
class Base: 

    """Um método construtor que define a casa ocupada pela nova torre, assim como seu tipo (caso tenha que ser consultada por alguma função externa) e cor (se é branca ou preta). 

    O formato do input deve ser assim:

    cor = 'branca' ou 'preta'
    casa = (0, 0); (0, 1), etc."""

    dando_xeque = False #No início, nenhuma peça dá xeque no rei. Naturalmente, esse método será inútil para o rei, pois ele não pode dar xeque no rei adversário.

    def __init__(self, cor, casa, tam_tabuleiro, info_peças):

        self.cor = cor
        self.casa = casa

        #A imagem é criada na função main pelo método 'criar_imagem' da classe, de acordo com o icon já importado pelo png. Isso é feito para evitar múltiplas importações de pngs, deixando o aplicativo mais pesado.
        self.imagem = ()
        
        #Define a posição a ser desenhada no tabuleiro, conforme a casa ocupada pela peça. Isso é uma função geral e não um método desta classe, pois tal função poderá ser usada também pelas classes de Peão, Cavalo, Bispo, etc.
        self.pos = self.descobrir_pos(casa, tam_tabuleiro)

    #Move a peça pelo tabuleiro e define as novas casas para as quais ela poderá ir na nova casa.
    def mover_peça(self, nova_casa, info_peças, tam_tabuleiro):

        #Atualiza a casa da peça e a posição conforme o tabuleiro.
        self.casa = nova_casa
        self.pos = self.descobrir_pos(nova_casa, tam_tabuleiro)
        self.movida = True

    #Função para verificar se a peça atual está dando xeque no rei adversário. Naturalmente, esse método será inútil para o rei, pois ele não pode dar xeque no rei adversário.
    def definir_dando_xeque(self, info_peças, vez, simulação=False,daria_xeque=False):

        cor_oposta = 'brancas' if vez == 'pretas' else 'pretas'

        for peça in info_peças[cor_oposta]:

            if peça.tipo == 'rei':

                if peça.casa in self.movimentos_possíveis(info_peças):
                    
                    if not(simulação):
                            
                        peça.em_xeque = True
                        self.dando_xeque = True
                    
                    else:
                        
                        daria_xeque = True
                
        if simulação:

            return daria_xeque

    #Função para remover lances inválidos. Todas as peças vão poder gerar uma lista de movimentos possíveis quando algum lance for requisitado dela. Nesse momento, nós queremos remover os lances inválidos dela (os lances que colocam o rei em xeque).
    def rem_lances_inválidos(self, info_peças, movimentos_possíveis):

        #Lista com todos os movimentos inválidos desta peça.
        movimentos_inválidos = []

        #Salva-se a casa antiga que a peça estava.
        antiga_casa = self.casa

        casa_peça_capturada = ()
        peça_capturada = None

        #Para cada casa que esta peça atualmente pode ir, verificar-se-á se esta casa deixa ou coloca o rei em xeque. Se sim, é inválida. Adiciona-se na lista de movimentos inválidos.
        for nova_casa in movimentos_possíveis:

            #Para cada movimento possível, faz-se uma simulação de movimento para verificar depois se o rei fica em xeque.
            self.casa = nova_casa

            #Define a cor adversária e a cor do jogador atual.
            grupo_cor_oposta = 'brancas' if self.cor in ['preta', 'preto'] else 'pretas'
            vez = 'brancas' if grupo_cor_oposta == 'pretas' else 'pretas'

            captura = False

            #Para cada movimento na simulação, é necessário retirar a peça caso ela tenha sido capturada na simulação.
            for peça in info_peças[grupo_cor_oposta]:
                if peça.casa == nova_casa:
                    captura = True
                    casa_peça_capturada = peça.casa
                    peça_capturada = peça
                    peça.casa = ()

            #Para todas as peças da cor adversária, verifica-se se ela dá xeque no rei considerando a simulação.
            for peça in info_peças[grupo_cor_oposta]:
                
                if peça.casa != ():

                    daria_xeque = peça.definir_dando_xeque(info_peças, grupo_cor_oposta, True)

                    if daria_xeque == True:

                        #Se alguma peça dá xeque no rei após o lance da simulação ser feita, então já descobrimos que o lance em questão é inválido. Portanto, adiciona-se o movimento na lista de movimentos inválidos e não se procede com a verificação para ver se outras peças dão xeque.

                        movimentos_inválidos.append(nova_casa)
                        break

            #A peça capturada é reestabelecida no lugar que ela estava antes da simulação.
            if captura:
                peça_capturada.casa = casa_peça_capturada

        #Após a simulação ser feita, a casa volta a ser o valor original.
        self.casa = antiga_casa

        #Atualiza a lista de movimentos_possíveis retirando os movimentos inválidos.
        movimentos_possíveis = list(set(movimentos_possíveis) - set(movimentos_inválidos))

        return movimentos_possíveis

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
