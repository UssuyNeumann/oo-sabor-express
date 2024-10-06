


from models.avaliacao import Avaliacao


class Restaurante: 
    restaurantes = [] 
    # _nome atributo protegido e não totalmente privado
    def __init__(self, nome, categoria): 
        self._nome = nome 
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = [] 
        Restaurante.restaurantes.append(self)

    def __str__(self): 
        return f'{self.nome} | {self.categoria}'
    
    @classmethod #medo da classe
    def listar_restaurantes(cls):
        print(f"{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property 
    def ativo(self):
        return '☒' if self._ativo else '☐'
    
    def alterar_status(self):
        self._ativo = not self._ativo

    #método da avaliação e objeto avaliação que recebe os valores
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-' 
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas/quantidade_notas, 1)
        return media
