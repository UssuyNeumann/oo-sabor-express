from models.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('El Caliente', 'Mexicana')
restaurante_japones = Restaurante('Sushi Ja', 'Oriental')

restaurante_mexicano.alterar_status()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()