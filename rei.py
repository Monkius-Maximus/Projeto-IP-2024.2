from base_peça import Base

class Rei(Base):
    tipo = 'rei'
    movida = False
    em_xeque = False  # No início do jogo, o rei não está em xeque

    def movimentos_possíveis(self, info_peças):
        movimentos_possíveis = []
        linha, coluna = self.casa

        # O rei pode mover uma casa em qualquer direção
        for d_linha in [-1, 0, 1]:
            for d_coluna in [-1, 0, 1]:
                if d_linha == 0 and d_coluna == 0:
                    continue  # Posição atual
                nova_casa = (linha + d_linha, coluna + d_coluna)
                if self.casa_valida(nova_casa, info_peças):
                    movimentos_possíveis.append(nova_casa)

        return movimentos_possíveis

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
