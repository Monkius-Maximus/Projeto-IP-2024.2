from base_peça import Base

class Rei(Base):
    tipo = 'rei'
    movida = False
    em_xeque = False  # No início do jogo, o rei não está em xeque

    def movimentos_possíveis(self, info_peças, verificar_roque=True):
        movimentos_possíveis = []
        linha, coluna = self.casa

        # Movimentos normais do rei (uma casa em qualquer direção)
        for d_linha in [-1, 0, 1]:
            for d_coluna in [-1, 0, 1]:
                if d_linha == 0 and d_coluna == 0:
                    continue
                nova_casa = (linha + d_linha, coluna + d_coluna)

                if self.casa_valida(nova_casa, info_peças):
                    movimentos_possíveis.append(nova_casa)

        # Verificação de roque (somente se permitido)
        if verificar_roque and not self.movida and not self.em_xeque:
            # print(f'{self.movida} -> {self.tipo}, {self.cor}')
            cor_rei = 'brancas' if self.cor in ['branca', 'branco'] else 'pretas'
            linha_inicial = 0 if cor_rei == 'brancas' else 7
            inimigos = info_peças['pretas'] if cor_rei == 'brancas' else info_peças['brancas']

            # Roque pequeno
            if self.pode_fazer_roque(info_peças, inimigos, linha_inicial, 5, 6, torre_coluna=7):
                movimentos_possíveis.append((linha_inicial, 6))

            # Roque grande
            if self.pode_fazer_roque(info_peças, inimigos, linha_inicial, 3, 2, 1, torre_coluna=0):
                movimentos_possíveis.append((linha_inicial, 2))

        return movimentos_possíveis
    
    def mover_peça(self, nova_casa, info_peças, tam_tabuleiro):
        # Atualiza a casa do rei normalmente
        self.casa = nova_casa
        self.pos = self.descobrir_pos(nova_casa, tam_tabuleiro)

        # Verifica se é um roque
        cor_rei = 'brancas' if self.cor in ['branca', 'branco'] else 'pretas'
        linha = 0 if cor_rei == 'brancas' else 7

        # Roque pequeno (rei foi para coluna 6)
        if nova_casa == (linha, 6) and not self.movida:
            torre = next(
                (p for p in info_peças[cor_rei] if p.tipo == 'torre' and p.casa == (linha, 7)),
                None
            )
            if torre:
                torre.mover_peça((linha, 5), info_peças, tam_tabuleiro)

        # Roque grande (rei foi para coluna 2)
        elif nova_casa == (linha, 2) and not self.movida:
            torre = next(
                (p for p in info_peças[cor_rei] if p.tipo == 'torre' and p.casa == (linha, 0)),
                None
            )
            if torre:
                torre.mover_peça((linha, 3), info_peças, tam_tabuleiro)

        self.movida = True

    def pode_fazer_roque(self, info_peças, inimigos, linha, *colunas_caminho, torre_coluna):
        """
        Verifica se o roque é possível do lado especificado.
        colunas_caminho são as colunas entre o rei e a torre pelas quais o rei passará.
        torre_coluna é a posição onde a torre está (0 para roque grande, 7 para pequeno).
        """
        # Verifica se a torre está no lugar certo e não se moveu
        cor_rei = 'brancas' if self.cor in ['branca', 'branco'] else 'pretas'
        torre = next(
            (p for p in info_peças[cor_rei] if p.tipo == 'torre' and p.casa == (linha, torre_coluna) and not p.movida),
            None
        )
        if torre is None:
            return False

        # Verifica se todas as casas entre o rei e a torre estão vazias
        for coluna in colunas_caminho:
            if self.tem_peca_em((linha, coluna), info_peças):
                return False

        #Verificamos apenas as casas pelas quais o rei passa (casa atual, e as colunas por onde ele passa)
        colunas_sob_ataque = [self.casa[1]] + [col for col in colunas_caminho if col in [3, 2, 5, 6]]
        casas_a_verificar = [(linha, col) for col in colunas_sob_ataque]

        for inimigo in inimigos:
            for casa_alvo in casas_a_verificar:
                if casa_alvo in inimigo.movimentos_possíveis(info_peças, verificar_roque=False):
                    return False

        return True


    def tem_peca_em(self, casa, info_peças):
        for grupo in info_peças.values():
            for peça in grupo:
                if peça.casa == casa:
                    return True
        return False

    def casa_valida(self, nova_casa, info_peças):
        # Dentro dos limites do tabuleiro
        if 0 <= nova_casa[0] < 8 and 0 <= nova_casa[1] < 8:
            # Não pode ser ocupada por uma peça da mesma cor
            for grupo_cor in info_peças:
                for peça in info_peças[grupo_cor]:
                    if peça.casa == nova_casa:
                        
                        cor_rei = 'brancas' if self.cor in ['branca', 'branco'] else 'pretas'
                        cor_peça_esbarrada = 'brancas' if peça.cor in ['branca', 'branco'] else 'pretas'

                        if cor_rei == cor_peça_esbarrada:
                            return False
            return True
        return False
