#FPS do programa
FPS = 60

#Sobre a tela do jogo em geral.
tam_tela = tam_tela_x, tam_tela_y = 1100, 800

#Sobre a tela principal (Menu).

#Nome da janela.
str_janela_menu = 'Xadrez do CIn'

#Sobre o título do Menu.
str_fonte_menu = 'Ubuntu' #Uma string com o nome da fonte do título.
tam_fonte_menu = 48
tam_x_menu = 529
tam_y_menu = 54
str_menu = 'Bem-vindo ao Chess CIn!' #Nome do título que aparecerá como principal.
cor_menu = (0, 0, 0) #Define a cor do título do menu como azul.

#Sobre o botão de Jogar. Definindo tamanho, cor e posição do botão Jogar.
tam_jogar = tam_jogar_x, tam_jogar_y = 300, 100 #Define o tamanho do botão. Ordem: largura e comprimento.
cor_jogar = (255, 255, 255) #Define que a cor do botão 'Jogar' será vermelha.

#Sobre o texto do botão jogar. Definindo string, cor e fonte.
str_jogar = 'Jogar'
cor_txt_jogar = (0, 0, 0) #Define que a cor do texto 'Jogar' no botão será preta.
str_fonte_jogar = 'Ubuntu'
tam_fonte_jogar = 30
tam_x_txt_jogar = 78
tam_y_txt_jogar = 34

#Sobre a tela do xadrez.

#Tamanho do tabuleiro em pixels. Dimensão x e y.
tam_tabuleiro = 800
tam_casa = 100 #Tamanho da casa de xadrez.
tam_peça = 80 #Tamanho que cada peça vai ocupar nas casas.

#Informações sobre a configuração inicial do xadrez.
tabuleiro_inicial = {
    'torre_preta' : [(7, 0), (7, 7)],
    'cavalo_preto' : [(7, 1), (7, 6)],
    'bispo_preto' : [(7, 2), (7, 5)],
    'rainha_preta' : [(7, 3)],
    'rei_preto' : [(7, 4)],
    'peão_preto' : [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)],
    
    'torre_branca' : [(0, 0), (0, 7)],
    'cavalo_branco' : [(0, 1), (0, 6)],
    'bispo_branco' : [(0, 2), (0, 5)],
    'rainha_branca' : [(0, 3)],
    'rei_branco' : [(0, 4)],
    'peão_branco' : [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)]
}

#Sobre a sidebar.

tam_sidebar = tam_tela_x - tam_tabuleiro #Tamanho inteiro da sidebar.
tam_peça_sidebar = 60 #Tamanho de cada peça na sidebar.
tam_fonte_sidebar = 48 #Tamanho dos textos de cada peça na sidebar.
tam_x_txt_sidebar = 90
tam_y_txt_sidebar = 54
distancia_peça_texto = 5
str_fonte_sidebar = 'Ubuntu'
cor_txt_sidebar = (0, 255, 0)
distancia_tabuleiro = 20 #Distância das peças com relação ao tabuleiro, segundo o eixo horizontal.
distancia_peças = 10 #Distância das peças entre si, segundo o eixo vertical.

#Sobre o filtro da tela de fim.
filtro_cor = (0, 0, 0)
filtro_transparência = 150