from models.restaurante import Restaurante
from models.cardapio.prato import Prato
from models.cardapio.bebida import Bebida

restaurante_praca = Restaurante('Praça', 'Brasileira')
restaurante_mexicano = Restaurante('El Caliente', 'Mexicana')
restaurante_japones = Restaurante('Sushi Ja', 'Oriental')

# restaurante_praca.alterar_status()
# restaurante_japones.alterar_status()

# restaurante_praca.receber_avaliacao('Luis',2)
# restaurante_praca.receber_avaliacao('Paula',4)
# restaurante_praca.receber_avaliacao('Michael',4)

bebida_suco = Bebida('Suco de Laranja',5.0, 'M')
prato_bife = Prato('Bife a Cavalo',25.0,'Bife com ovo frito, arroz e fritas')
restaurante_praca.adicionar_cardapio(bebida_suco)
restaurante_praca.adicionar_cardapio(prato_bife)


def main():
    #Restaurante.listar_restaurantes()
    # print(bebida_suco)
    # print(prato_bife)
    restaurante_praca.listar_cardapio

if __name__ == '__main__':
    main() 