from models.cardapio.item_cardapio import ItemCardapio
#herdando nome e preco da classe ItemCardapio
class Bebida(ItemCardapio):
    def __init__(self,nome,preco,tamanho):
        super().__init__(nome,preco)
        self._tamanho = tamanho

    def __str__(self):
        return f'{self._nome} | {self._preco} | {self._tamanho}'