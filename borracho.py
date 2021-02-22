import random


class Borracho():

    def __init__(self, nombre):
        self.nombre = nombre


class BorrachoTradicional(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    #Funcion para mover al borracho aleatoriamente, se puede modificar para alterar las probabilidades de movimiento
    def camina(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)])


