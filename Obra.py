class Obra:
    """
    Clase: Obra.

    Objetivo: Ordenar la información suministrada por la API de una obra.

    La información requerida (atributos) es:
    Id de la obra. (int)
    Titulo o nombre de la obra. (string)
    Artista de la obra. (string)
    Fecha de nacimiento del artista. (string)
    Fecha de muerte del artista. (string)
    Tipo o clasificación de la obra. (string)
    Año de creacion (o período) de la obra. (string)
    Imagen referencial de la obra. ()

    Métodos:
    El método show_resumen muestra al usuario la información primordial de la obra al buscar un departamento, nacionalidad o artista específico.
    El método show_detalles muestra al usuario información más detallada de la obra al indicar un id a una obra específica.
    """
    def __init__(self,id,titulo,autor,nacionalidad,fecha_nacimiento,fecha_muerte,tipo,anio_creacion,imagen):
        self.id=id
        self.titulo=titulo
        self.autor=autor
        self.nacionalidad=nacionalidad
        self.fecha_nacimiento=fecha_nacimiento
        self.fecha_muerte=fecha_muerte
        self.tipo=tipo
        self.anio_creacion=anio_creacion
        self.imagen=imagen

    def show_resumen(self):
        print(f"    Id: {self.id} - Título: {self.titulo} (Artista: {self.autor})")

    def show_detalles(self):
        print(f"\nTítulo de la Obra: {self.titulo}\n"
            f"Nombre del Artista: {self.autor} \n"
            f"Nacionalidad del Artista: {self.nacionalidad}\n"
            f"Fecha de nacimiento del Artista: {self.fecha_nacimiento}\n"
            f"Fecha de muerte del Artista: {self.fecha_muerte}\n"
            f"Clasificación de la Obra: {self.tipo}\n"
            f"Fecha de creación de la Obra: {self.anio_creacion}\n")