def main():
    #escribe tu código abajo de esta línea
    nmensajes = int(input("Dame el número de mensajes: "))
    nmegas = float(input("Dame el número de megas: "))
    nminutos = int(input("Dame el número de minutos: "))
    costo = ((nmegas+nmensajes+nminutos)*0.80)
    print("El costo mensual es:", costo)




if __name__ == '__main__':
    main()
