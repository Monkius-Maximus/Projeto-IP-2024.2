import pygame
import configuracoes as cfg
from torre import Torre

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

    return peça

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
def eventos_xadrez(tam_tabuleiro, evento, casa_origem, info_peças, vez):

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
        
        #Função para descobrir se a casa de origem deve ser atualizada. Para isso, é necessário três coisas. Primeiro, que seja uma peça. Segundo, que seja uma peça branca na vez das brancas, e uma peça preta na vez das pretas.
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
                            é_origem = (vez == 0 and (peça.cor == 'preta' or peça.cor == 'preto') or vez == 1 and (peça.cor == 'branca' or peça.cor == 'branco'))

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

        casa_clicada = encontrando_linha_coluna(tam_tabuleiro, pos_x, pos_y)
        print(casa_clicada)

        #Se não houve casa clicada, ou seja, se o clique do usuário foi na barra lateral do jogo.
        if casa_clicada == False:

            cliques_barra_lateral(evento)

        #Se alguma casa foi clicada.
        else:

            #Atualizando a casa de origem, se isso for necessário.
            casa_origem, foi_atualizada = atualizar_origem(casa_origem, casa_clicada, info_peças, vez)

            #Se não foi escolhida uma nova casa de origem neste clique, e, além disso, a casa de origem não está vazia, então significa que houve a tentativa de uma casa de destino.
                        
            #Se já há uma casa de origem e uma casa de destino, limpa-se ambas para receber a próxima casa de origem e destino.
            # Se já existe uma casa de origem selecionada e uma nova casa foi clicada
        if casa_origem != () and not foi_atualizada and casa_clicada:
            casa_destino = casa_clicada
    
            # Função para verificar se o lance é válido
            def é_lance_válido(casa_origem, casa_destino, info_peças):
                # A booleana começa como False
                é_válido = False
                peça_origem = None
        
                # Buscar a peça que está na casa de origem
                for grupo_cor in info_peças:
                    for peça in info_peças[grupo_cor]:
                        if peça.casa == casa_origem:
                            peça_origem = peça
                            break
                    if peça_origem:
                        break
        
                # Se encontrou uma peça na casa de origem
                if peça_origem:
                    # Se a peça for uma torre, usa sua função específica
                    if peça_origem.tipo == 'torre':
                        lances_possíveis = peça_origem.definir_lances_torre(info_peças)
                        if casa_destino in lances_possíveis:
                            é_válido = True
        
                return é_válido, peça_origem
    
            # Verificar se o lance é válido
            é_válido, peça_origem = é_lance_válido(casa_origem, casa_destino, info_peças)
    
            # Se o lance for válido, move a peça
            # Se o lance for válido, move a peça
            if é_válido:
                # Verificar se há alguma peça na casa de destino para capturar
                peça_capturada = None
                for grupo_cor in info_peças:
                    for i, peça in enumerate(info_peças[grupo_cor]):
                        if peça.casa == casa_destino:
                            # Armazena a peça capturada
                            peça_capturada = peça
                            # Remove a peça capturada
                            info_peças[grupo_cor].pop(i)
                            break
                    if peça_capturada:
                        break
                
                # Registrar que o peão fez seu primeiro movimento
                if peça_origem.tipo == 'peao' and peça_origem.primeiro_movimento:
                    peça_origem.primeiro_movimento = False
                
                # Registrar que o rei ou a torre foram movidos (para controle do roque)
                if peça_origem.tipo in ['rei', 'torre']:
                    peça_origem.movido = True
                
                # Movendo a peça da casa de origem para a casa de destino
                peça_origem.casa = casa_destino
                peça_origem.pos = peça_origem.descobrir_pos(casa_destino, tam_tabuleiro)
                
                # Verificar promoção de peão (se um peão chegar à última linha)
                if peça_origem.tipo == 'peao':
                    última_linha = 0 if peça_origem.cor in ['preta', 'preto'] else 7
                    if peça_origem.casa[0] == última_linha:
                        # Promover o peão para rainha (simplificação)
                        from rainha import Rainha
                        grupo = 'pretas' if peça_origem.cor in ['preta', 'preto'] else 'brancas'
                        # Remover o peão
                        for i, peça in enumerate(info_peças[grupo]):
                            if peça == peça_origem:
                                info_peças[grupo].pop(i)
                                break
                        # Adicionar uma rainha no lugar
                        nova_rainha = Rainha(peça_origem.cor, casa_destino, tam_tabuleiro)
                        tipo_rainha = 'rainha_preta' if peça_origem.cor in ['preta', 'preto'] else 'rainha_branca'
                        nova_rainha.criar_imagem(dict_icons[tipo_rainha])
                        info_peças[grupo].append(nova_rainha)
                
                # Alternar o turno após um movimento válido
                vez = 1 - vez  # Alterna entre 0 e 1
                
                # Limpar casa de origem e destino após o movimento
                casa_origem = ()
                casa_destino = ()
            else:
                # Se o lance não for válido, apenas limpa a casa de origem
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
def desenhar_xadrez(tela, tabuleiro, info_peças, casa_origem=None, vez=None):
    # Pinta-se o fundo da tela de roxo, eliminando objetos antigos.
    tela.fill('purple')
    
    # Desenha-se o tabuleiro.
    tela.blit(tabuleiro, (0, 0))
    
    # Se há uma casa de origem selecionada, destaca ela
    if casa_origem:
        tam_casa = tabuleiro.get_size()[0] / 8
        linha, coluna = casa_origem
        # Converter coordenadas do tabuleiro para coordenadas da tela
        x = coluna * tam_casa
        y = tabuleiro.get_size()[0] - (linha + 1) * tam_casa
        # Desenhar retângulo de destaque
        pygame.draw.rect(tela, (255, 255, 0, 128), (x, y, tam_casa, tam_casa), 3)
    
    # Desenhar indicador de turno
    fonte = pygame.font.SysFont('Arial', 20)
    cor_turno = "Brancas" if vez == 1 else "Pretas"
    texto_turno = fonte.render(f"Turno: {cor_turno}", True, (255, 255, 255))
    tela.blit(texto_turno, (tabuleiro.get_size()[0] + 10, 30))

    # Desenhar mensagem, se houver
    if mensagem:
        texto_mensagem = fonte.render(mensagem, True, (255, 255, 0))
        tela.blit(texto_mensagem, (tabuleiro.get_size()[0] + 10, 60))
    
    # Desenham-se as peças em cima do tabuleiro.
    desenhar_peças(tela, info_peças, casa_origem)

#Função que define as informações iniciais sobre as peças em cada casa. O dicionário é passado porque, para cada peça, é necessário saber qual é o png associado a ela de acordo com seu tipo.
def definir_peças(dict_icons, tam_tabuleiro):
    # Importando as classes das peças
    from torre import Torre
    from cavalo import Cavalo
    from bispo import Bispo
    from rainha import Rainha
    from rei import Rei
    from peao import Peao
    
    # Dicionário que irá armazenar informações sobre as peças (objetos das classes). 
    info_peças = {
        'pretas' : [],
        'brancas' : []
    }

    # Dicionário que mapeia a cor da peça individual para o grupo
    cor_info = {
        'preta': 'pretas', 'preto': 'pretas',
        'branca': 'brancas', 'branco': 'brancas'
    }

    # Para cada tipo de peça, criar instâncias
    for tipo_peça, casas_iniciais in cfg.tabuleiro_inicial.items():
        peça = tipo_peça.split('_')[0]
        cor = tipo_peça.split('_')[1]
        grupo = cor_info[cor]
        
        for casa in casas_iniciais:
            if peça == 'torre':
                nova_peça = Torre(cor, casa, tam_tabuleiro)
            elif peça == 'cavalo':
                nova_peça = Cavalo(cor, casa, tam_tabuleiro)
            elif peça == 'bispo':
                nova_peça = Bispo(cor, casa, tam_tabuleiro)
            elif peça == 'rainha':
                nova_peça = Rainha(cor, casa, tam_tabuleiro)
            elif peça == 'rei':
                nova_peça = Rei(cor, casa, tam_tabuleiro)
            elif peça == 'peao':
                nova_peça = Peao(cor, casa, tam_tabuleiro)
            
            nova_peça.criar_imagem(dict_icons[tipo_peça])
            info_peças[grupo].append(nova_peça)

    return info_peças

def desenhar_peças(tela, info_peças, casa_origem=None):
    # Queremos desenhar as peças de todas as cores, sejam elas pretas ou brancas.
    for grupo_cor in info_peças:
        # Para cada peça de cada grupo.
        for peça in info_peças[grupo_cor]:
            # Desenha a peça na tela.
            peça.desenhar(tela)
            
            # Se esta peça está na casa de origem, destaca seus lances possíveis
            if casa_origem and peça.casa == casa_origem:
                if peça.tipo == 'torre':
                    peça.destacar_lances_possíveis(tela, info_peças, 800)
                elif peça.tipo == 'cavalo':
                    peça.destacar_lances_possíveis(tela, info_peças, 800)
                elif peça.tipo == 'bispo':
                    peça.destacar_lances_possíveis(tela, info_peças, 800)
                elif peça.tipo == 'rainha':
                    peça.destacar_lances_possíveis(tela, info_peças, 800)
                elif peça.tipo == 'rei':
                    peça.destacar_lances_possíveis(tela, info_peças, 800)
                elif peça.tipo == 'peao':
                    peça.destacar_lances_possíveis(tela, info_peças, 800)