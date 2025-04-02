import pygame
import configuracoes as cfg
from torre import Torre
from peao import Peão
import pprint

#Função feita para inicializar a tela. É chamada no início do jogo para configurar o menu.
def _init_tela():

    #Informações do monitor atual.
    info_monitor = pygame.display.Info()

    #Pega informações sobre a resolução usada pelo monitor, a saber, tamanho x e y.
    x_monitor = info_monitor.current_w
    y_monitor = info_monitor.current_h

    #Assim como em uma tela de 1920x1080 o aplicativo deve ter 1100x800, a mesma proporção deve ser observada para outras resoluções.
    x_proporcional = (x_monitor * cfg.tam_tela_x) / 1920
    y_proporcional = (cfg.tam_tela_y * x_proporcional) / cfg.tam_tela_x

    # Cria a janela com o tamanho ajustado.
    tela = pygame.display.set_mode((x_proporcional, y_proporcional))

    pygame.display.set_caption(cfg.str_janela_menu) #Define título do menu.

    return tela

#Função para inicializar o título que aparece no menu principal.
def _init_tit_menu(tela_x, tela_y):

    #Definindo fonte.
    fonte_título = pygame.font.SysFont(cfg.str_fonte_menu, cfg.tam_fonte_menu)

    #Renderiza o texto em uma superfície. Define-se: string do título, anti-aliasing e cor do título.
    antialais = True
    txt_menu = fonte_título.render(cfg.str_menu, antialais, cfg.cor_menu)
    
    #Redimensionando o texto com base no tamanho x e y da tela. 
    x_menu_redim = (cfg.tam_x_menu * tela_x) / cfg.tam_tela_x
    y_menu_redim = (cfg.tam_y_menu * tela_y) / cfg.tam_tela_y
    txt_menu = pygame.transform.scale(txt_menu, (x_menu_redim, y_menu_redim))

    #Define a posição x e y do título do menu.
    txt_menu_x = (tela_x) / 2 - (x_menu_redim / 2)
    txt_menu_y = 30
    pos_txt_menu = (txt_menu_x, txt_menu_y)

    #Retorna-se a superfície final do título do menu e sua posição.
    return txt_menu, pos_txt_menu

#Função para inicializar o botão de Jogar.
def _init_jogar(tela_x, tela_y):

    #Define tamanho redimensionado da superfície.
    x_jogar_redim = (cfg.tam_jogar_x * tela_x) / cfg.tam_tela_x
    y_jogar_redim = (cfg.tam_jogar_y * tela_y) / cfg.tam_tela_y
    tam_jogar_redim = (x_jogar_redim, y_jogar_redim)

    #Definindo superfície e cor do botão de jogar.
    jogar = pygame.Surface(tam_jogar_redim) #Cria uma surface com o tamanho do botão jogar, criando algo como um retângulo.
    jogar.fill(cfg.cor_jogar) #Pinta a surface de vermelho.

    #Definindo posição do botão segundo o referencial da tela.
    jogar_x = (tela_x) / 2 - (x_jogar_redim / 2)
    jogar_y = (tela_y) / 2 - (y_jogar_redim / 2)
    pos_jogar = (jogar_x, jogar_y)

    #Retorna-se o botão e sua posição.
    return jogar, pos_jogar

#Função para inicializar o texto do botão de Jogar.
def _init_txt_jogar(jogar):

    fonte_jogar = pygame.font.SysFont('Ubuntu', 30)
    str_jogar = 'Jogar'
    cor_txt_jogar = (0, 0, 0) #Define que a cor do texto 'Jogar' no botão será preta.
    antialias = True
    txt_jogar = fonte_jogar.render(str_jogar, antialias, cor_txt_jogar)
    
    #Tamanhos x e y do botão jogar
    jogar_x, jogar_y = jogar.get_size()

    #Redimensionando o texto jogar para ficar proporcional ao tamanho real do botão.
    x_txt_jogar_redim = (cfg.tam_x_txt_jogar * jogar_x) / cfg.tam_jogar_x
    y_txt_jogar_redim = (cfg.tam_y_txt_jogar * jogar_y) / cfg.tam_jogar_y
    txt_jogar = pygame.transform.scale(txt_jogar, (x_txt_jogar_redim, y_txt_jogar_redim))

    #Faz com que o centro do texto 'Jogar' seja idêntico ao centro do botão Jogar.
    x_txt_jogar = (jogar_x / 2) - (x_txt_jogar_redim / 2)
    y_txt_jogar = (jogar_y / 2) - (y_txt_jogar_redim / 2)
    pos_txt_jogar = (x_txt_jogar, y_txt_jogar)

    return txt_jogar, pos_txt_jogar

#Função para inicializar as peças brancas capturadas da sidebar.
def _init_brancas_capturadas(torre_branca_pequena,
                            cavalo_branco_pequeno,
                            bispo_branco_pequeno,
                            rainha_branca_pequena,
                            peão_branco_pequeno,
                            tam_tabuleiro,
                            tam_tela,
                            y_peça_sidebar_redim):

    #Definindo posições.

    #Redimensiona a distância das peças para o tabuleiro segundo o eixo horizontal, considerando o tamanho real x do tabuleiro e o tamanho real x da tela.

    tam_side_bar_redim = tam_tela[0] - tam_tabuleiro
    distancia_tabuleiro_real = (cfg.distancia_tabuleiro * tam_side_bar_redim) / cfg.tam_sidebar
    x_geral = tam_tabuleiro + distancia_tabuleiro_real

    #Redimensiona a distância das peças entre si segundo o eixo vertical, considerando o tamanho real da peça na sidebar.

    distancia_peças_real = (cfg.distancia_peças * y_peça_sidebar_redim) / cfg.tam_peça_sidebar

    y_peão_branco = distancia_peças_real
    y_cavalo_branco = y_peão_branco + y_peça_sidebar_redim + distancia_peças_real
    y_bispo_branco = y_cavalo_branco + y_peça_sidebar_redim + distancia_peças_real
    y_torre_branca = y_bispo_branco + y_peça_sidebar_redim + distancia_peças_real
    y_rainha_branca = y_torre_branca + y_peça_sidebar_redim + distancia_peças_real

    #Associando as posições aos ícones.

    brancas_capturadas = {
        'peão_branco': (peão_branco_pequeno, (x_geral, y_peão_branco)),
        'cavalo_branco': (cavalo_branco_pequeno, (x_geral, y_cavalo_branco)),
        'bispo_branco': (bispo_branco_pequeno, (x_geral, y_bispo_branco)),
        'torre_branca': (torre_branca_pequena, (x_geral, y_torre_branca)),
        'rainha_branca': (rainha_branca_pequena, (x_geral, y_rainha_branca)),
    }

    return brancas_capturadas

#Função para inicializar os textos das peças na sidebar. Pode ser usado para brancas ou pretas.
def _init_textos(peças_capturadas):
    
    textos = {}

    for peça, (icon, (x, y)) in peças_capturadas.items():

        #Definindo fonte.
        fonte_título = pygame.font.SysFont(cfg.str_fonte_sidebar, cfg.tam_fonte_sidebar)

        #Renderiza o texto em uma superfície. Define-se: string do título, anti-aliasing e cor do título.
        antialais = True
        texto_atual = ' -> 0'
        txt_sidebar = fonte_título.render(texto_atual, antialais, cfg.cor_txt_sidebar)

        pos_txt_sidebar = (x + cfg.tam_peça_sidebar + 5, y)

        textos[peça] = [txt_sidebar, pos_txt_sidebar, texto_atual]
    
    return textos

#Função para inicializar as peças pretas capturadas na sidebar.
def _init_pretas_capturadas(torre_preta_pequena,
                            cavalo_preto_pequeno,
                            bispo_preto_pequeno,
                            rainha_preta_pequena,
                            peão_preto_pequeno,
                            tam_tabuleiro,
                            tam_tela,
                            y_peça_sidebar_redim):
    
    #Definindo posições.

    #Redimensiona a distância das peças para o tabuleiro segundo o eixo vertical, considerando o tamanho real do tabuleiro e o tamanho real da tela.

    tam_side_bar_redim = tam_tela[0] - tam_tabuleiro
    distancia_tabuleiro_real = (cfg.distancia_tabuleiro * tam_side_bar_redim) / cfg.tam_sidebar
    x_geral = tam_tabuleiro + distancia_tabuleiro_real

    #Redimensiona a distância das peças entre si segundo o eixo vertical, considerando o tamanho real da peça na sidebar.
    
    distancia_peças_real = (cfg.distancia_peças * y_peça_sidebar_redim) / cfg.tam_peça_sidebar

    y_rainha_preta = tam_tabuleiro - y_peça_sidebar_redim - distancia_peças_real
    y_torre_preta = y_rainha_preta - y_peça_sidebar_redim - distancia_peças_real
    y_bispo_preto = y_torre_preta - y_peça_sidebar_redim - distancia_peças_real
    y_cavalo_preto = y_bispo_preto - y_peça_sidebar_redim - distancia_peças_real
    y_peão_preto = y_cavalo_preto - y_peça_sidebar_redim - distancia_peças_real

    #Associando as posições aos ícones.

    pretas_capturadas = {
        'peão_preto': (peão_preto_pequeno, (x_geral, y_peão_preto)),
        'cavalo_preto': (cavalo_preto_pequeno, (x_geral, y_cavalo_preto)),
        'bispo_preto': (bispo_preto_pequeno, (x_geral, y_bispo_preto)),
        'torre_preta': (torre_preta_pequena, (x_geral, y_torre_preta)),
        'rainha_preta': (rainha_preta_pequena, (x_geral, y_rainha_preta)),
    }

    return pretas_capturadas

#Função para importar e redimensionar o tabuleiro do xadrez.
def importar_tabuleiro(tela_x):

    tabuleiro = pygame.image.load('imagens/tabuleiro.png')
    tam_tabuleiro_redim = (cfg.tam_tabuleiro * tela_x) / cfg.tam_tela_x
    tabuleiro = pygame.transform.scale(tabuleiro, (tam_tabuleiro_redim, tam_tabuleiro_redim))
    
    return tabuleiro

#Função para importar os pngs das peças do xadrez. Essa função retorna dois valores: 1) a peça transformada para ter um tamanho no tabuleiro de fato; 2) a peça transformada em uma versão menor, para aparecer no quadro ao lado do tabuleiro, de peças capturadas.
def importar_peças(peça_png, tabuleiro):

    caminho = 'imagens/peças/'

    #Transforma o png de cada peça em uma superfície para desenhar no programa.
    peça = pygame.image.load(f'{caminho}{peça_png}')

    #Redimensiona a superfície para um tamanho razoável da peça normal considerando o tamanho real de cada casa.
    
    tam_real_casa = tabuleiro.get_size()[0]/8 #Cada casa possui o tamanho de uma linha do tabuleiro dividido por 8, pois uma linha tem 8 casas.
    tam_peça_redim = (cfg.tam_peça * tam_real_casa) / cfg.tam_casa

    peça = pygame.transform.scale(peça, (tam_peça_redim, tam_peça_redim))
    
    #Cria uma versão menor da peça para ser usada na sidebar. Redimensiona seu tamanho com base no tamanho real da peça, conforme a resolução do monitor.
    tam_peça_sidebar_redim = (cfg.tam_peça_sidebar * tam_peça_redim) / cfg.tam_peça

    peça_pequena = pygame.transform.scale(peça, (tam_peça_sidebar_redim, tam_peça_sidebar_redim))

    return peça, peça_pequena

#Função para lidar com os eventos do menu. Info_peças começa sendo um dicionário vazio, pois ainda estamos no menu e o usuário ainda não escolheu jogar.
def eventos_menu(evento, jogar_rect, dict_icons, tam_tabuleiro, info_peças = {}):

    #Quando se verifica um evento da tela menu, a tela atual é o menu. Mas, poderá mudar, caso o usuário tenha decidido mudar de tela. Exemplo: decidindo jogar o xadrez
    tela_atual = 'menu'

    #Se o usuário clicou no Mouse.
    if evento.type == pygame.MOUSEBUTTONDOWN:

        #Se o usuário clicou no botão de Jogar.
        if jogar_rect.collidepoint(evento.pos):

            #Caso o usuário tenha apertado em Jogar, a tela atual deve se tornar a do xadrez.
            tela_atual = 'xadrez'

            #Como o usuário está começando a jogar agora, é necessário definir as informações iniciais das peças do tabuleiro.
            info_peças = definir_peças(dict_icons, tam_tabuleiro)

    return tela_atual, info_peças

#Função para lidar com os eventos da tela de xadrez. Ela recebe o evento que ocorreu, uma variável que armazena se já há uma casa clicada e outra variável armazenando de quem é a vez no jogo.
def eventos_xadrez(tam_tabuleiro, evento, casa_origem, info_peças, vez, sidebar_contagem):

    #Quando se verifica um evento da tela xadrez, a tela atual é o xadrez. Mas, poderá mudar, caso o usuário tenha decidido mudar de tela. Exemplo: voltando para o menu.
    tela_atual = 'xadrez'

    #Cria uma variável para armazenar a casa de destino do lance.
    casa_destino = ()

    #Se o mouse foi clicado.
    if evento.type == pygame.MOUSEBUTTONDOWN:

        #Capta a posição x e y do clique do mouse.
        pos_x, pos_y = evento.pos

        #Função para encontrar a linha e a coluna do clique do jogador.
        def encontrando_linha_coluna(tam_tabuleiro, pos_x, pos_y):
            
            #Resposta da função começa vazia.
            resposta = None

            #Se o clique foi dentro do tabuleiro, identifica e retorna linha e coluna da casa clicada.
            if pos_x <= tam_tabuleiro and pos_y <= tam_tabuleiro:

                #Identificando qual foi a linha da casa selecionada.
                encontrou_linha = False
                pos_teste_y = (tam_tabuleiro / 8)
                linha = 7

                while not(encontrou_linha):

                    if pos_teste_y >= pos_y:

                        encontrou_linha = True

                    else:

                        linha -= 1
                        pos_teste_y += tam_tabuleiro / 8

                #Identificando qual foi a coluna da casa selecionada.
                encontrou_coluna = False
                pos_teste_x = (tam_tabuleiro / 8)
                coluna = 0

                while not(encontrou_coluna):

                    if pos_teste_x >= pos_x:

                        encontrou_coluna = True
                    
                    else:
                        
                        coluna += 1
                        pos_teste_x += tam_tabuleiro / 8

                resposta = (linha, coluna)

            #Se o clique foi fora do tabuleiro, retorne False.
            else:

                resposta = False

            return resposta

        #Função para lidar com cliques do mouse na barra lateral do jogo.
        def cliques_barra_lateral(evento):
            pass
        
        #Função para descobrir se a casa de origem deve ser atualizada. Para isso, são necessárias duas coisas. Primeiro, que a casa clicada seja uma peça. Segundo, que seja uma peça branca na vez das brancas, e uma peça preta na vez das pretas. Terceiro, que seja uma peça distinta da peça atualmente selecionada (caso haja alguma).
        def atualizar_origem(casa_origem, casa_clicada, info_peças, vez):

            #Se a casa de origem for atualizada no meio da função, essa variável será atualizada para True.
            foi_atualizada = False

            #Função para verificar se a casa clicada é a casa de uma peça. Também verifica se a peça clicada é uma peça de origem válida, ou seja, uma peça do jogador atual.
            def é_peça_origem(casa_clicada, info_peças, vez):

                #A booleana começa com False, e, se acharmos uma peça nesta casa, se torna verdadeiro.
                é_peça_origem = False

                #Para cada grupo de cor de peças.
                for grupo_cor in info_peças:
                    
                    #Para cada peça no grupo de cor.
                    for peça in info_peças[grupo_cor]:

                        #Booleana que verifica se esta peça está na casa clicada.
                        é_peça = peça.casa == casa_clicada

                        if é_peça:

                            #Booleana que verifica se a peça é uma peça de origem, isto é, se é uma peça do jogador atual.
                            é_origem = (vez == 'pretas' and (peça.cor == 'preta' or peça.cor == 'preto') or vez == 'brancas' and (peça.cor == 'branca' or peça.cor == 'branco'))

                            #Se a casa clicada for idêntica à casa desta peça, e esta peça for uma peça do jogador atual.
                            if é_origem:
                                
                                #Então há uma peça na casa clicada.
                                é_peça_origem = True
                
                return é_peça_origem

            é_peça_origem = é_peça_origem(casa_clicada, info_peças, vez)
            
            #Se o jogador clicou numa peça dele, e, além disso, se essa peça não estiver atualmente selecionada, então ela é selecionada e a casa de origem é atualizada.
            if é_peça_origem and casa_origem != casa_clicada:

                casa_origem = casa_clicada
                foi_atualizada = True

            return casa_origem, foi_atualizada

        #Função para descobrir se a casa de destino deve ser atualizada. Para isso, são necessárias duas coisas. Primeiro, uma casa de origem válida, que é uma peça do usuário já selecinada. Segundo, que ele tenha selecionado, no clique da casa de destino, um lugar para o qual a peça dele pode, efetivamente, ir. Esta função supõe a primeira condição e verifica a segunda.
        def atualizar_destino(casa_origem, casa_clicada, info_peças, vez, tam_tabuleiro, sidebar_contagem):

            #Função para encontrar a peça atualmente selecionada.
            def encontrar_peça_selecionada(casa_origem, info_peças, vez):
                
                peça_selecionada = None

                #Para cada peça na lista das peças do grupo de cor da peça selecionada. Ex.: Na vez das brancas, para cada peça branca.    
                for peça in info_peças[vez]:
                    
                    #Se a peça estiver na casa clicada de origem.
                    if peça.casa == casa_origem:
                        
                        #Achou-se a peça selecionada
                        peça_selecionada = peça

                return peça_selecionada

            #Encontrando a peça atualmente selecionada.
            peça_selecionada = encontrar_peça_selecionada(casa_origem, info_peças, vez)

            #Se ela pode ir para onde o usuário clicou.
            if casa_clicada in peça_selecionada.movimentos_possíveis(info_peças):
                
                #Move a peça.
                peça_selecionada.mover_peça(casa_clicada, info_peças, tam_tabuleiro)
                
                #Checa se alguma peça do time oposto foi capturada e deleta ela com base nisso.
                grupo_cor_oposta = 'pretas' if vez == 'brancas' else 'brancas'

                for peça_oposta in info_peças[grupo_cor_oposta]:
                    
                    #Se há uma peça da cor oposta na casa para a qual a peça foi.
                    if peça_oposta.casa == casa_clicada:
                        
                        #Remove a peça oposta, pois ela foi capturada.
                        info_peças[grupo_cor_oposta].remove(peça_oposta)

                        #Atualiza a sidebar passando como parâmetro o tipo da peça oposta, e sua cor.

                        for tipo_peça, elementos_texto in sidebar_contagem['textos'][grupo_cor_oposta].items():

                            if tipo_peça == peça_oposta.tipo + '_' + peça_oposta.cor:

                                texto_atual = elementos_texto[2] #Texto atual que está sendo desenhado, que representa a quantidade de vezes que a peça foi capturada.
                                num_atual = int(texto_atual.split(' -> ')[1]) #Pega só o número.
                                num_atual += 1 #Soma em 1, pois uma peça desse tipo foi capturada.
                                texto_atual = ' -> ' + str(num_atual) #Troca o texto atual.

                                #Gera uma nova fonte e superfície com base no novo texto.
                                fonte_título = pygame.font.SysFont(cfg.str_fonte_sidebar, cfg.tam_fonte_sidebar)
                                txt_sidebar = fonte_título.render(texto_atual, True, cfg.cor_txt_sidebar)

                                #Atualiza a superfície para comportar o texto com o novo valor de captura.
                                sidebar_contagem['textos'][grupo_cor_oposta][tipo_peça][0] = txt_sidebar

                                #Atualiza o texto com a quantidade de peças deste tipo capturadas.
                                sidebar_contagem['textos'][grupo_cor_oposta][tipo_peça][2] = texto_atual

                #Troca a vez do jogador.
                vez = 'pretas' if vez == 'brancas' else 'brancas'

            return vez

        casa_clicada = encontrando_linha_coluna(tam_tabuleiro, pos_x, pos_y)

        #Se não houve casa clicada, ou seja, se o clique do usuário foi na barra lateral do jogo.
        if casa_clicada == False:

            cliques_barra_lateral(evento)

        #Se alguma casa foi clicada.
        else:

            #Atualizando a casa de origem, se isso for necessário.
            casa_origem, foi_atualizada = atualizar_origem(casa_origem, casa_clicada, info_peças, vez)

            #Se não foi escolhida uma nova casa de origem neste clique, e, além disso, a casa de origem não está atualmente vazia, então isso significa que houve a tentativa de uma casa de destino.
            if not(foi_atualizada) and casa_origem != ():
                
                #Atualizando a casa de destino, se isso for necessário. Se uma casa de destino válida foi selecionada, então a peça será movida.
                vez = atualizar_destino(casa_origem, casa_clicada, info_peças, vez, tam_tabuleiro, sidebar_contagem)
            
                #Seja a peça movida (tentativa válida) ou não (tentativa inválida), a casa de origem é zerada para uma nova seleção.
                casa_origem = ()

    return tela_atual, casa_origem, info_peças, vez

#Função para fazer os desenhos da tela menu.
def desenhar_menu(tela, jogar, pos_jogar, txt_menu, pos_txt_menu):

    #Pinta-se o fundo da tela de roxo, eliminando objetos antigos.
    tela.fill('purple')

    #Desenha-se as coisas na tela.

    #Desenhando o botão jogar na tela.
    tela.blit(jogar, pos_jogar)

    #Desenhando o título do menu na tela.
    tela.blit(txt_menu, pos_txt_menu)

#Função para fazer os desenhos da tela do xadrez.
def desenhar_xadrez(tela, tabuleiro, info_peças):

    #Pinta-se o fundo da tela de roxo, eliminando objetos antigos.
    tela.fill('blue')

    #Desenha-se as coisas na tela.

    #Desenha-se o tabuleiro.
    tela.blit(tabuleiro, (0, 0))

    #Desenham-se as peças em cima do tabuleiro.
    desenhar_peças(tela, info_peças)

#Função para fazer os desenhos da sidebar da contagem de peças.
def desenhar_sidebar_contagem(tela, sidebar_contagem):

    #As chaves podem ser 'ícones' e 'textos', de forma que os ícones e os textos são ambos desenhados. Os subdicionários são as listas dos ícones e textos das brancas ou pretas na sidebar.
    for chave, subdicionário in sidebar_contagem.items():
        
        for grupo_cor in subdicionário.keys():
            
            peças_cor = subdicionário[grupo_cor]

            if chave == 'ícones':

                for peça, (icon, posição) in peças_cor.items():

                    tela.blit(icon, posição)

            elif chave == 'textos':

                for peça, (icon, posição, texto_atual) in peças_cor.items():

                    tela.blit(icon, posição)

#Função que define as informações iniciais sobre as peças em cada casa. O dicionário é passado porque, para cada peça, é necessário saber qual é o png associado a ela de acordo com seu tipo.
def definir_peças(dict_icons, tam_tabuleiro):

    #Dicionário que irá armazenar informações sobre as peças (objetos das classes). 
    info_peças = {
        'pretas' : [],
        'brancas' : []
    }

    #Dicionário que mapeia a cor da peça individual ('preto', 'preta', 'branco', 'branca') para a string que representa o grupo a que pertence 'pretas' ou 'brancas'.
    cor_info = {
        'preta' : 'pretas',
        'preto' : 'pretas',

        'branca' : 'brancas',
        'branco' : 'brancas'
    }

    #Para cada tipo de peça, também haverá uma lista com as casas iniciais que as peças desse tipo irão ocupar.
    for tipo_peça, casas_iniciais in cfg.tabuleiro_inicial.items():

        #O tipo de peça é definido pela peça e por sua cor. Exemplo: torre_preta.
        peça = tipo_peça.split('_')[0]
        cor = tipo_peça.split('_')[1]

        #Criando as torres do tabuleiro inicial.
        if peça == 'torre':
            
            for casa in casas_iniciais:
                    
                torre = Torre(cor, casa, tam_tabuleiro, info_peças) #Cria o objeto da torre.
                torre.criar_imagem(dict_icons[tipo_peça]) #Cria a sua imagem desenhável de acordo com seu tipo e cor.
                grupo = cor_info[cor] #Associa ela ao grupo que pertence conforme sua cor.
                info_peças[grupo].append(torre) #Adiciona ela no dicionário de todas as peças de acordo com seu grupo de cor.

        elif peça == 'peão':

            for casa in casas_iniciais:
                    
                peão = Peão(cor, casa, tam_tabuleiro, info_peças) #Cria o objeto do peão.
                peão.criar_imagem(dict_icons[tipo_peça])
                grupo = cor_info[cor]
                info_peças[grupo].append(peão)

    return info_peças

#Função para desenhar todas as peças no tabuleiro.
def desenhar_peças(tela, info_peças):

    #Queremos desenhar as peças de todas as cores, sejam elas pretas ou brancas.
    for grupo_cor in info_peças:

        #Para cada peça de cada grupo.
        for peça in info_peças[grupo_cor]:

            #Desenha a peça na tela.
            peça.desenhar(tela)
