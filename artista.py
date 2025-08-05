class Artista:
  """
  Clase: Artista

  Objetivo: Representar la informacion relevante de un artista.

  Atributos:
  Nombre (string)
  Nacionalidad (string)
  Nacimiento (string)
  Muerte (string)

  """

  def __init__(self, nombre, nacionalidad, nacimiento, muerte):
      self.nombre = nombre
      self.nacionalidad = nacionalidad
      self.nacimiento = nacimiento
      self.muerte = muerte

  def show_info(self):
      print(f"Nombre: {self.nombre}")
      print(f"Nacionalidad: {self.nacionalidad}")
      print(f"Nacimiento: {self.nacimiento}")
      print(f"Muerte: {self.muerte}")
