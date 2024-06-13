def area_poligono(poligono, base, altura):
    if poligono == 't':
        area = (base * altura)/2
        return area
    elif poligono == 'c':
        area = base * altura
        return area
    elif poligono == 'r':
        area = base * altura
        return area
def main():
    while True:
        print('------------------------------------------------')
        poligono = input('Ingresa el tipo de poligono (T/t, C/c ó R/r): ').lower()
        if poligono == 't':
            base = int(input('Ingrese la base de su triangulo: '))
            altura = int(input('Ingrese la altura de su triangulo: '))
            print('El area de su triangulo es de: ', area_poligono(poligono, base, altura))
        elif poligono == 'c':
            lado = int(input('Ingrese el lado de su cuadrado: '))
            print('El area de su cuadrado es de: ', area_poligono(poligono, lado, lado))
        elif poligono == 'r':
            base = int(input('Ingrese la base de su rectangulo: '))
            altura = int(input('Ingrese la altura de su rectangulo: '))
            print('El area de su rectangulo es de: ', area_poligono(poligono, base, altura))
        elif poligono == 'salir':
            print('Saliendo del programa...')
            break
        else:
            print('Opcion no valida.')
main()