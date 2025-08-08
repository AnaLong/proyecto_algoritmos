class Nacionalidad:
    """
    Clase: Nacionalidad.

    Objetivo: Ordenar la información suministrada por el documento de las nacionalidades disponibles.

    La información requerida (atributos) es:
    Nombre de la nacionalidad (string)

    Métodos:
    El método show muestra al usuario la lista de nacionalidades disponibles para la busqueda
    """
    def __init__(self,nombre):
        self.nombre=nombre
    
    def show(self):
        print(f'- {self.nombre}')