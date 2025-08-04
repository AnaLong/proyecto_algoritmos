class Departamento:
    """
    Clase: Departamento.

    Objetivo: Ordenar la información suministrada por la API de la lista de departamentos.

    La información requerida (atributos) es:
    Id del departamento. (int)
    Nombre del departamento. (string)

    Métodos:
    El método show_lista muestra al usuario una lista de los departamentos con sus respectivos ids al seleccionar dicho método de búsqueda
    """
    def __init__(self,id,nombre):
        self.id=id
        self.nombre=nombre
         
    def show_lista(self):
        print(f"{self.id} - {self.nombre}")
