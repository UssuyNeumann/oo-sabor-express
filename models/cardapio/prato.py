from models.cardapio.item_cardapio import ItemCardapio
#herdando nome e preco da classe ItemCardapio
class Prato(ItemCardapio):
    def __init__(self,nome,preco,descricao):
        super().__init__(nome,preco)
        self._descricao = descricao
    
    def __str__(self):
        return f'{self._nome} - {self._descricao} | {self._preco}'
