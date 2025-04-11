import pygame, os
import funcoes_do_jogo as fj
import configuracoes as cfg
import copy

#Limpa o terminal para fazer impressões.
os.system('clear')

#Inicializa os módulos do Pygame.
pygame.init()

#Som da peça sendo movida
som_captura = pygame.mixer.Sound('sons/movimento_peça.mp3')

#Inicia o mixer do pygame para o jogo ter sons
pygame.mixer.init()

#Sobre o menu.

#Variável armazenando a tela atual do jogo. Começa com menu.
tela_atual = 'menu'

#Variável que define o funcionamento do aplicativo.
usr_jogando = True

#Inicializa a tela do programa de acordo com as exigências do menu.
tela = fj._init_tela()

#Salva os tamanhos x e y reais da tela, após ajustada para atender às proporções do monitor em questão.
tam_tela = tela_x, tela_y = tela.get_size()

#Sobre a tela do final.

#Inicializando informações sobre o filtro preto (quando houver tela de empate ou tela de jogador que venceu).
filtro = fj._init_filtro(tela_x, tela_y)

#Objeto para administrar o tempo do programa.
relógio = pygame.time.Clock()

#Criando o título de menu e o retângulo correspondente à superfície de acordo com o tamanho da tela.
txt_menu, pos_txt_menu = fj._init_tit_menu(tela_x, tela_y)

#Criando o botão de jogar (superfície).

#Definindo tamanho, superfície, cor e posição do botão Jogar.
jogar, pos_jogar = fj._init_jogar(tela_x, tela_y)

#Definindo fonte, texto, cor e superfície do texto do botão Jogar. O botão de Jogar é passado como parâmetro para definir a posição do texto.
txt_jogar, pos_txt_jogar = fj._init_txt_jogar(jogar)

#Colocando o texto 'Jogar' na superfície do botão Jogar.
jogar.blit(txt_jogar, pos_txt_jogar) #Desenha o texto 'Jogar' no botão Jogar.

# Aqui vamos carregar a música de fundo por enquanto só o de loop
musica_fundo = pygame.mixer.Sound('sons/musica_fundo.mp3')

# música de fundo está tocando ou não
musica_tocando = False

#Sobre a tela do xadrez.

#Importando o tabuleiro.
tabuleiro = fj.importar_tabuleiro(tela_x)
tam_tabuleiro = tabuleiro.get_size()[0]

#Importando as peças do xadrez.
torre_preta, torre_preta_pequena = fj.importar_peças('torre_preta.png', tabuleiro)
cavalo_preto, cavalo_preto_pequeno = fj.importar_peças('cavalo_preto.png', tabuleiro)
bispo_preto, bispo_preto_pequeno = fj.importar_peças('bispo_preto.png', tabuleiro)
rainha_preta, rainha_preta_pequena = fj.importar_peças('rainha_preta.png', tabuleiro)
rei_preto = fj.importar_peças('rei_preto.png', tabuleiro)[0]
peão_preto, peão_preto_pequeno = fj.importar_peças('peao_preto.png', tabuleiro)

torre_branca, torre_branca_pequena = fj.importar_peças('torre_branca.png', tabuleiro)
cavalo_branco, cavalo_branco_pequeno = fj.importar_peças('cavalo_branco.png', tabuleiro)
bispo_branco, bispo_branco_pequeno = fj.importar_peças('bispo_branco.png', tabuleiro)
rainha_branca, rainha_branca_pequena = fj.importar_peças('rainha_branca.png', tabuleiro)
rei_branco = fj.importar_peças('rei_branco.png', tabuleiro)[0]
peão_branco, peão_branco_pequeno = fj.importar_peças('peao_branco.png', tabuleiro)

tam_real_sidebar = torre_branca_pequena.get_size()[0]

#Importando a capa do menu.
capa_menu = pygame.image.load('imagens/capa_menu.jpeg')
capa_menu = pygame.transform.scale(capa_menu, (tela_x, tela_y))

#Importando a imagem da sidebar.
img_sidebar = pygame.image.load('imagens/imagem_sidebar.jpeg')
x_img_sidebar = tela_x - tam_tabuleiro
y_img_sidebar = tela_y
img_sidebar = pygame.transform.scale(img_sidebar, (x_img_sidebar, y_img_sidebar))

#Sobre a sidebar (Contadores).

#Inicializa a posição das peças brancas capturadas na sidebar e insere elas em uma lista, assim como os textos correspondentes às capturas. 
brancas_capturadas = fj._init_brancas_capturadas(torre_branca_pequena,
                                                 cavalo_branco_pequeno,
                                                 bispo_branco_pequeno,
                                                 rainha_branca_pequena,
                                                 peão_branco_pequeno,
                                                 tam_tabuleiro,
                                                 tam_tela,
                                                 torre_preta_pequena.get_size()[1])

#Inicializar os textos das brancas capturadas na sidebar, com base na posição das brancas capturadas.
textos_brancas = fj._init_textos(brancas_capturadas, tam_real_sidebar)

#Inicializa a posição das peças pretas capturadas na sidebar e insere elas em uma lista, assim como os textos correspondentes às capturas. 
pretas_capturadas = fj._init_pretas_capturadas(torre_preta_pequena,
                                               cavalo_preto_pequeno,
                                               bispo_preto_pequeno,
                                               rainha_preta_pequena,
                                               peão_preto_pequeno,
                                               tam_tabuleiro,
                                               tam_tela,
                                               torre_preta_pequena.get_size()[1])

#Inicializar os textos das brancas capturadas na sidebar, com base na posição das brancas capturadas.
textos_pretas = fj._init_textos(pretas_capturadas, tam_real_sidebar)

#Junta as informações numa estrutura de dados só, para simplificar.
sidebar_contagem = {
    'ícones' : {
        'brancas' : brancas_capturadas,
        'pretas' : pretas_capturadas
    },

    'textos' : {
        'brancas' : textos_brancas,
        'pretas' : textos_pretas
    }
}

#Criando uma associação entre o nome de cada peça e a surface desenhável dela.
dict_icons = {
    'torre_preta' : torre_preta,
    'cavalo_preto' : cavalo_preto,
    'bispo_preto' : bispo_preto,
    'rainha_preta' : rainha_preta,
    'rei_preto' : rei_preto,
    'peão_preto' : peão_preto,

    'torre_branca' : torre_branca,
    'cavalo_branco' : cavalo_branco,
    'bispo_branco' : bispo_branco,
    'rainha_branca' : rainha_branca,
    'rei_branco' : rei_branco,
    'peão_branco' : peão_branco,
}

#Casa de origem e de destino selecionadas. Ambas começam vazias. Ex.: Se o usuário clica na casa a7, e além disso ele havia clicado anteriormente na casa a1, onde há uma torre, a torre deve ser movida de a1 para a7.
casa_origem = ()
casa_destino = ()

#Variável armazenando de quem é a vez no jogo.
vez = 'brancas'

#Loop principal do jogo.
while usr_jogando:

    #Limita o FPS do programa.
    relógio.tick(cfg.FPS)

    #Lidando com os eventos do aplicativo.
    for evento in pygame.event.get():

        #Se o usuário clicou no botão de fechar o programa (da janela do sistema operacional). Isso independe da tela atual.
        if evento.type == pygame.QUIT:
            
            #O pygame é finalizado.
            pygame.quit()

            #Limpa o terminal no final.
            os.system('clear')

            #O programa em si é finalizado.
            exit()

        #Se a tela atual for o menu, lida-se com os eventos interessantes que o menu pode receber.
        elif tela_atual == 'menu':

            #Eventos de menu são resolvidos e a tela atual é atualizada. Além disso, quando o usuário apertar em 'Jogar', as informações sobre as peças são adicionadas na variável info_peças. Para isso, é necessário o uso da biblioteca dict_icons, para associar cada peça ao seu png. O retângulo do botão de jogar é passado para saber se o usuário clicou no botão.
            tela_atual, info_peças, vez, sidebar_contagem = fj.eventos_menu(evento, jogar.get_rect(topleft=pos_jogar), dict_icons, tam_tabuleiro, sidebar_contagem, tam_real_sidebar)

        #Se a tela for do jogo de xadrez e se não for a tela do fim (empate ou ganhar), lida-se com os eventos interessantes que a tela do xadrez pode receber. Por isso o comparativo do == é usado neste caso.
        elif tela_atual == 'xadrez':

            #Eventos da tela do xadrez são resolvidos e a tela atual é atualizada. A casa de destino não é enviada como parâmetro, pois, ela sempre será vazia ao checar novos eventos.
            tela_atual, casa_origem, info_peças, vez = fj.eventos_xadrez(tam_tabuleiro, evento, casa_origem, info_peças, vez, sidebar_contagem)
        
        #Caso a tela atual seja a tela do final do jogo, ou seja, empate ou alguém venceu. Os eventos verificados para essas telas possíveis são os mesmos eventos.
        else:
            
            tela_atual, info_peças, vez, sidebar_contagem = fj.eventos_tela_final(tela_atual, evento, dict_icons, tam_tabuleiro, info_peças, vez, sidebar_contagem, tam_real_sidebar)

    # Gerenciamento da música de fundo
    if tela_atual == 'menu' and not musica_tocando:
        # Inicia a música apenas se estivermos no menu e ela não estiver tocando
        musica_fundo.play(loops=-1)
        musica_tocando = True
    elif tela_atual != 'menu' and musica_tocando:
        # Para a música se saímos do menu e ela estiver tocando
        musica_fundo.stop()
        musica_tocando = False

    #Desenhando as coisas no aplicativo de acordo com a tela do menu.
    if tela_atual == 'menu':

        #Desenha-se o menu com o título principal e o botão de jogar.
        fj.desenhar_menu(tela, capa_menu, jogar, pos_jogar, txt_menu, pos_txt_menu)

    #Desenhando as coisas no aplicativo de acordo com a tela do xadrez. O in é usado, pois é possível que a string seja 'xadrez_fim', quando, além da tela ser do xadrez, também é necessário imprimir as informações sobre o fim do jogo.
    elif 'xadrez' in tela_atual:

        #Desenha-se a tela do xadrez com as peças e todo o resto.
        fj.desenhar_xadrez(tela, tabuleiro, img_sidebar, info_peças)

        #Desenha-se a sidebar do xadrez, no que se diz respeito aos contadoress.
        fj.desenhar_sidebar_contagem(tela, sidebar_contagem)

        #Se a tela atual também for a tela do final do jogo (Ex.: 'xadrez_empate'; 'xadrez_pretas_venceram'; 'xadrez_brancas_venceram'). Para isso, é necessário verificar se for empate ou se alguém venceu.
        if tela_atual != 'xadrez':
            
            venceram = str()

            #Se foi empate, venceram é igual ao grupo das peças que venceram. Caso contrário, permanece vazia, conforme foi feito na inicialização = str().
            if tela_atual != 'xadrez_empate':
                
                venceram = tela_atual.split('_')[1] #O modelo é sempre, por exemplo: 'xadrez_pretas_venceram' ou 'xadrez_brancas_venceram'.
            
            #Chama a função de desenhar a tela final.
            fj.desenhar_tela_final(tela, filtro, venceram)

    #Atualiza a tela desde as últimas alterações.
    pygame.display.update()