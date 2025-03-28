import pygame, os
import funcoes_do_jogo as fj
from configuracoes import *

#Limpa o terminal para fazer impressões.
os.system('cls')

#Inicializa os módulos do Pygame.
pygame.init()

#Inicializa a tela do programa de acordo com as exigências do menu.
tela = fj._init_tela()

#Objeto para administrar o tempo do programa.
relógio = pygame.time.Clock()

#Criando o título de menu e o retângulo correspondente à superfície.
txt_menu, txt_menu_rect = fj._init_tit_menu()

#Criando o botão de jogar (superfície).

#Definindo tamanho, superfície, cor e posição do botão Jogar.
jogar, jogar_rect = fj._init_jogar()

#Definindo fonte, texto, cor e superfície do texto do botão Jogar. O botão de Jogar é passado como parâmetro para definir a posição do texto.
txt_jogar, txt_jogar_rect = fj._init_txt_jogar(jogar)

#Colocando o texto 'Jogar' na superfície do botão Jogar.
jogar.blit(txt_jogar, txt_jogar_rect) #Desenha o texto 'Jogar' no botão Jogar.

# Importando as peças do xadrez.
torre_preta, torre_preta_pequena = fj.importar_peças('torre_preta.png')
cavalo_preto, cavalo_preto_pequeno = fj.importar_peças('cavalo_preto.png')
bispo_preto, bispo_preto_pequeno = fj.importar_peças('bispo_preto.png')
rainha_preta, rainha_preta_pequena = fj.importar_peças('rainha_preta.png')
rei_preto, rei_preto_pequeno = fj.importar_peças('rei_preto.png')
peao_preto, peao_preto_pequeno = fj.importar_peças('peao_preto.png')

torre_branca, torre_branca_pequena = fj.importar_peças('torre_branca.png')
cavalo_branco, cavalo_branco_pequeno = fj.importar_peças('cavalo_branco.png')
bispo_branco, bispo_branco_pequeno = fj.importar_peças('bispo_branco.png')
rainha_branca, rainha_branca_pequena = fj.importar_peças('rainha_branca.png')
rei_branco, rei_branco_pequeno = fj.importar_peças('rei_branco.png')
peao_branco, peao_branco_pequeno = fj.importar_peças('peao_branco.png')

dict_icons = {
    'torre_preta' : torre_preta,
    'cavalo_preto' : cavalo_preto,
    'bispo_preto' : bispo_preto,
    'rainha_preta' : rainha_preta,
    'rei_preto' : rei_preto,
    'peao_preto' : peao_preto,

    'torre_branca' : torre_branca,
    'cavalo_branco' : cavalo_branco,
    'bispo_branco' : bispo_branco,
    'rainha_branca' : rainha_branca,
    'rei_branco' : rei_branco,
    'peao_branco' : peao_branco,
}

#Loop principal do jogo.
while usr_jogando:

    #Limita o FPS do programa.
    relógio.tick(FPS)

    #Lidando com os eventos do aplicativo.
    for evento in pygame.event.get():

        #Se o usuário clicou no botão de fechar o programa (da janela do sistema operacional). Isso independe da tela atual.
        if evento.type == pygame.QUIT:
            
            #O pygame é finalizado.
            pygame.quit()

            #Limpa o terminal no final.
            os.system('cls')

            #O programa em si é finalizado.
            exit()

        #Se a tela atual for o menu, lida-se com os eventos interessantes que o menu pode receber.
        elif tela_atual == 'menu':

            #Eventos de menu são resolvidos e a tela atual é atualizada.
            tela_atual = fj.eventos_menu(evento, jogar_rect)

        #Se a tela for do jogo de xadrez, lida-se com os eventos interessantes que a tela do xadrez pode receber.
        elif tela_atual == 'xadrez':

            #Eventos da tela do xadrez são resolvidos e a tela atual é atualizada. A casa de destino não é enviada como parâmetro, pois, ela sempre será vazia ao checar novos eventos.
            tela_atual, casa_origem, casa_destino = fj.eventos_xadrez(evento, casa_origem)

    #Desenhando as coisas no aplicativo de acordo com a tela do menu.
    if tela_atual == 'menu':

        fj.desenhar_menu(tela, jogar, txt_menu, txt_menu_rect)

    #Desenhando as coisas no aplicativo de acordo com a tela do xadrez.
    elif tela_atual == 'xadrez':

        #Se o tabuleiro ainda não foi criado, isto é, o usuário está começando um novo jogo.
        if matriz_casas == []:

            #Chama uma função que define as informações iniciais sobre todas as casas.
            matriz_casas = fj.definir_casas(dict_icons)

        #Desenha-se o tabuleiro a partir da matriz de casas.
        fj.desenhar_tabuleiro(tela, matriz_casas)

    #Atualiza a tela desde as últimas alterações.
    pygame.display.update()