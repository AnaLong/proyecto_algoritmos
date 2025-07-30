def obras_fun():
    import requests
    id_req= input("\nIngrese el ID de la obra en la que esta interesado: ")
    api="https://collectionapi.metmuseum.org/public/collection/v1/objects/" + id_req
    obj=requests.get(api)
    obj=obj.json()

    def limpiar(valor):
        if valor is None or str(valor).strip() == "":
            return "Desconocido"
        return valor

    class Obra:
            def __init__(self,obj):
                self.titulo=limpiar(obj.get("title"))
                self.artista=limpiar(obj.get("artistDisplayName"))
                self.nacionalidad=limpiar(obj.get("artistNationality"))
                self.nacimiento=limpiar(obj.get("artistBeginDate"))
                self.muerte=limpiar(obj.get("artistEndDate"))
                self.tipo=limpiar(obj.get("classification"))
                self.creacion=limpiar(obj.get("objectDate"))

            def __str__(self):
                return (f"\nTítulo de la Obra: {self.titulo}\n"
                        f"Nombre del Artista: {self.artista}\n"
                        f"Nacionalidad del Artista: {self.nacionalidad}\n"
                        f"Fecha de nacimiento del Artista: {self.nacimiento}\n"
                        f"Fecha de muerte del Artista: {self.muerte}\n"
                        f"Clasificación de la Obra: {self.tipo}\n"
                        f"Fecha de creación de la Obra: {self.creacion}\n")
            
    obra_req = Obra(obj)
    print(obra_req)


    #Hay info que algunas obras no tiene, ver como poner que si esta vacio diga "Desconocido"

    #Aqui Rojo, agregue el metodo limpiar, que lo que hace es agarrar y poner "desconocido" si la informacion esta en None o si esta en blanco. 
    #El strip lo que hace es eliminar los espacios en blanco que hayan de mas en los strings. 
