from models.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
# restaurante_mexicano = Restaurante('El Caliente', 'Mexicana')
# restaurante_japones = Restaurante('Sushi Ja', 'Oriental')

# restaurante_mexicano.alterar_status()

restaurante_praca.receber_avaliacao('Luis',1)
restaurante_praca.receber_avaliacao('Paula',8)
restaurante_praca.receber_avaliacao('Michael',5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()