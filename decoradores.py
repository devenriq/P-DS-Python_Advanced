# def decorador(func):

#     def envoltura():
#         print('Esto se añade a mi función original')
#         func()

#     return envoltura()

# @decorador
# def saludo():
#     print("Hola")

# saludo()


def mayusculas(func):

    def envoltura(texto):
        return func(texto).upper()

    return envoltura


@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'


print(mensaje('Cesar'))
