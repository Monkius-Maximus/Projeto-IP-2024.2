import pygame
from configuracoes import *
from casa import Casa

#Função feita para inicializar a tela. É chamada no início do jogo para configurar o menu.
def _init_tela():

    tela = pygame.display.set_mode(tam_tela) #O parâmetro é o tamanho da tela.
    pygame.display.set_caption(str_janela_menu) #Define título do menu.

    return tela

#Função para inicializar o título que aparece no menu principal.
def _init_tit_menu():

    #Definindo fonte.
    fonte_título = pygame.font.SysFont(str_fonte_menu, tam_fonte_menu)

    #Renderiza o texto em uma superfície. Define-se: string do título, anti-aliasing e cor do título.
    antialais = True
    txt_menu = fonte_título.render(str_menu, antialais, cor_menu)

    #Define a posição x e y do título do menu.
    txt_menu_rect = txt_menu.get_rect()
    txt_menu_rect.centerx = tam_tela_x / 2
    txt_menu_rect.top = 30

    #Retorna-se a superfície final do título do menu.
    return txt_menu, txt_menu_rect

#Função para inicializar o botão de Jogar.
def _init_jogar():

    #Definindo superfície e cor do botão de jogar.
    jogar = pygame.Surface(tam_jogar) #Cria uma surface com o tamanho do botão jogar, criando algo como um retângulo.

    jogar.fill(cor_jogar) #Pinta a surface de vermelho.

    #Definindo posição do botão segundo o referencial da tela.
    jogar_x = (tam_tela_x) / 2 - (tam_jogar_x / 2)
    jogar_y = (tam_tela_y) / 2 - (tam_jogar_y / 2)

    #Definindo o retângulo do botão jogar e especificando a posição do seu canto superior esquerdo na tela do menu.
    jogar_rect = jogar.get_rect(topleft=(jogar_x, jogar_y))

    #Retorna-se o botão e seu retângulo.
    return jogar, jogar_rect

#Função para inicializar o texto do botão de Jogar.
def _init_txt_jogar(jogar):

    fonte_jogar = pygame.font.SysFont('Ubuntu', 30)
    str_jogar = 'Jogar'
    cor_txt_jogar = (0, 0, 0) #Define que a cor do texto 'Jogar' no botão será preta.
    antialias = True
    txt_jogar = fonte_jogar.render(str_jogar, antialias, cor_txt_jogar)

    #Faz com que o centro do texto 'Jogar' seja idêntico ao centro do botão Jogar.
    txt_jogar_rect = txt_jogar.get_rect() #Obtém o retângulo do texto 'Jogar'.
    txt_jogar_rect.center = jogar.get_rect().center

    return txt_jogar, txt_jogar_rect

#Função para importar os pngs das peças do xadrez. Essa função retorna dois valores: 1) a peça transformada para ter um tamanho no tabuleiro de fato; 2) a peça transformada em uma versão menor, para aparecer no quadro ao lado do tabuleiro, de peças capturadas.
def importar_peças(peça_png):

    caminho = 'imagens/peças/'

    #Transforma o png de cada peça em uma superfície para desenhar no programa.
    peça = pygame.image.load(f'{caminho}{peça_png}')

    #Redimensiona a superfície para um tamanho razoável da peça normal considerando a nossa tela.
    peça = pygame.transform.scale(peça, (80, 80))

    #Redimensiona a superfície para um tamanho razoável da peça pequena considerando a nossa tela.
    peça_pequena = pygame.transform.scale(peça, (45, 45))

    return peça, peça_pequena

#Função para lidar com os eventos do menu.
def eventos_menu(evento, jogar_rect):

    #Quando se verifica um evento da tela menu, a tela atual é o menu. Mas, poderá mudar, caso o usuário tenha decidido mudar de tela. Exemplo: decidindo jogar o xadrez
    tela_atual = 'menu'

    #Se o usuário clicou no Mouse.
    if evento.type == pygame.MOUSEBUTTONDOWN:

        #Se o usuário clicou no botão de Jogar.
        if jogar_rect.collidepoint(evento.pos):

            #Caso o usuário tenha apertado em Jogar, a tela atual deve se tornar a do xadrez.
            tela_atual = 'xadrez'

    return tela_atual

#Função para lidar com os eventos da tela de xadrez. Ela recebe o evento que ocorreu, e também uma variável que armazena se já há uma casa selecionada.
def eventos_xadrez(evento, casa_origem):

    #Quando se verifica um evento da tela xadrez, a tela atual é o xadrez. Mas, poderá mudar, caso o usuário tenha decidido mudar de tela. Exemplo: voltando para o menu.
    tela_atual = 'xadrez'

    #Cria uma variável para armazenar a casa de destino do lance.
    casa_destino = ()

    #Se o mouse foi clicado.
    if evento.type == pygame.MOUSEBUTTONDOWN:

        #Capta a posição x e y do clique do mouse.
        pos_x, pos_y = evento.pos

        #Função para encontrar a linha e a coluna do clique do jogador.
        def encontrando_linha_coluna(pos_x, pos_y):
            
            #Resposta da função começa vazia.
            resposta = None

            #Se o clique foi dentro do tabuleiro.
            if pos_x <= 800 and pos_y <= 800:

                #Identificando qual foi a linha da casa selecionada.
                encontrou_linha = False
                pos_teste_x = 100
                linha = 0

                while not(encontrou_linha):

                    if pos_teste_x >= pos_x:

                        encontrou_linha = True

                    else:

                        linha += 1
                        pos_teste_x += 100

                #Identificando qual foi a coluna da casa selecionada.
                encontrou_coluna = False
                pos_teste_y = 100
                coluna = 7

                while not(encontrou_coluna):

                    if pos_teste_y >= pos_y:

                        encontrou_coluna = True
                    
                    else:
                        
                        coluna -= 1
                        pos_teste_y += 100

                resposta = (linha, coluna)

            #Se o clique foi fora do tabuleiro.
            else:

                resposta = False

            return resposta

        casa_clicada = encontrando_linha_coluna(pos_x, pos_y)

        #Se não há casa anterior selecionada.
        if casa_origem == ():
            
            casa_origem = casa_clicada

        #Se houve uma casa anteriormente selecionada.
        else:
            
            casa_destino = casa_clicada

        print(f'{casa_origem} /// {casa_destino}')

    return tela_atual, casa_origem, casa_destino

#Função para fazer os desenhos da tela menu.
def desenhar_menu(tela, jogar, txt_menu, txt_menu_rect):

    #Pinta o fundo da tela de roxo.
    tela.fill("purple")

    #Desenhando as coisas na tela.

    #Desenhando o botão jogar na tela.
    tela.blit(jogar, (jogar_x, jogar_y))

    #Desenhando o título do menu na tela.
    tela.blit(txt_menu, txt_menu_rect)

#Função que define as informações iniciais sobre todas as casas.
def definir_casas(dict_icons):

    #Criando as casas.
    matriz_casas = [[None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None]]
    
    #Criando a matriz de casas.
    for i in range(64):

        """Comportamento:

            (linha, coluna).
            0, 0.
            0, 1.
            ...
            0, 7.
            1, 0.
            1, 1.
            ...
            1, 7.
            ...
            7, 7.

        """
        
        coluna = i % 8
        linha = i // 8

        casa = Casa(linha, coluna)

        matriz_casas[linha][coluna] = casa

    #Desenhando peças iniciais nas casas.
    tabuleiro_inicial = {
        'torre_preta' : [(7, 0), (7, 7)],
        'cavalo_preto' : [(7, 1), (7, 6)],
        'bispo_preto' : [(7, 2), (7, 5)],
        'rainha_preta' : [(7, 3)],
        'rei_preto' : [(7, 4)],
        'peao_preto' : [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)],
        
        'torre_branca' : [(0, 0), (0, 7)],
        'cavalo_branco' : [(0, 1), (0, 6)],
        'bispo_branco' : [(0, 2), (0, 5)],
        'rainha_branca' : [(0, 3)],
        'rei_branco' : [(0, 4)],
        'peao_branco' : [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)]
    }

    #Exemplo de valor possível para 'peça': ('torre_preta', [(7, 0), (7, 7)])
    for peça in tabuleiro_inicial.items():

        #Exemplo de valor possível para casa (no exemplo acima): (7, 0)
        for casa in peça[1]:

            linha = casa[0]
            coluna = casa[1]
            matriz_casas[linha][coluna].ocupar_casa(peça[0], dict_icons)

    return matriz_casas

#Função para fazer os desenhos da tela do xadrez.
def desenhar_tabuleiro(tela, matriz_casas):

    #Pinta a tela de roxo.
    tela.fill('purple')

    for i in matriz_casas:
        for j in i:
            j.print_surface(tela)
