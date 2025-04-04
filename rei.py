from base_peça import Base

class Rei(Base):

    #O método construtor é herdado da classe Base.

    tipo = 'rei'
    movida = False
    em_xeque = False #No início do jogo, ambos dos reis não estão em xeque.

    def movimentos_possíveis(self, info_peças):
        # Aqui você deve implementar a lógica para determinar os movimentos possíveis do rei
        movimentos = []
        linha, coluna = self.casa

        # O rei pode mover uma casa em qualquer direção
        for d_linha in [-1, 0, 1]:
            for d_coluna in [-1, 0, 1]:
                if d_linha == 0 and d_coluna == 0:
                    continue  # Ignora a posição atual
                nova_casa = (linha + d_linha, coluna + d_coluna)
                if self.casa_valida(nova_casa, info_peças):
                    movimentos.append(nova_casa)

        return movimentos

    def casa_valida(self, nova_casa, info_peças):
        # Verifica se a nova casa está dentro dos limites do tabuleiro
        if 0 <= nova_casa[0] < 8 and 0 <= nova_casa[1] < 8:
            # Verifica se a casa não está ocupada por uma peça da mesma cor
            for grupo_cor in info_peças:
                for peça in info_peças[grupo_cor]:
                    if peça.casa == nova_casa and peça.cor == self.cor:
                        return False
            return True
        return False
