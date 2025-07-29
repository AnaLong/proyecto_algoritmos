def obras_fun():
    import requests
    id_req= input("Ingrese el ID de la obra en la que esta interesado: ")
    api="https://collectionapi.metmuseum.org/public/collection/v1/objects/" + id_req
    obj=requests.get(api)
    obj=obj.json()

    class Obra:
            def __init__(self,obj):
                self.titulo=obj["title"]
                self.artista=obj["artistDisplayName"]
                self.nacionalidad=obj["artistNationality"]
                self.nacimiento=obj["artistBeginDate"]
                self.muerte=obj["artistEndDate"]
                self.tipo=obj["classification"]
                self.creacion=obj["objectDate"]

            def __str__(self):
                return (f"Título de la Obra: {self.titulo}\n"
                        f"Nombre del Artista: {self.artista}\n"
                        f"Nacionalidad del Artista: {self.nacionalidad}\n"
                        f"Fecha de nacimiento del Artista: {self.nacimiento}\n"
                        f"Fecha de muerte del Artista: {self.muerte}\n"
                        f"Clasificación de la Obra: {self.tipo}\n"
                        f"Fecha de creación de la Obra: {self.creacion}\n")
            
    obra_req = Obra(obj)
    print(obra_req)


    #Hay info que algunas obras no tiene, ver como poner que si esta vacio diga "Desconocido"