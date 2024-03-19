class Restaurante: 
    restaurantes = [] 
    # _nome atributo protegido e não totalmente privado
    def __init__(self, nome, categoria): 
        self._nome = nome 
        self._categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self): 
        return f'{self.nome} | {self.categoria}'
    
    @classmethod #medo da classe
    def listar_restaurantes(cls):
        print(f"{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property 
    def ativo(self):
        return '☒' if self._ativo else '☐'
    
    def alterar_status(self):
        self._ativo = not self._ativo

restaurante_pizza = Restaurante('Pizza','Pizzaria')
restaurante_pizza.alterar_status()
restaurante_sushi = Restaurante('Sushi','Oriental')

Restaurante.listar_restaurantes()
