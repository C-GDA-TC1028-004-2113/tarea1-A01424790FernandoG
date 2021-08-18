def main():
    #escribe tu código abajo de esta línea
    añonacimiento = int(input("Dame el año de nacimiento: "))
    añoactual = int(input("Dame el año actual: "))
    lustrosvida = (añoactual-añonacimiento)/5
    print("Los lustros que has vivido son:", str(lustrosvida))


if __name__ == '__main__':
    main()
