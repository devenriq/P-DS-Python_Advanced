def decorador(func):

    def envoltura():
        print('Esto se añade a mi función original')
        func()

    return envoltura()


@decorador
def saludo():
    print("Hola")


saludo()
