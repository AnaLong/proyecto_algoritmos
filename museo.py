class Museo:
    def __init__(self,id_dep,nacionalidades,artistas):
        import requests
        self.id_dep=id_dep
        id_dep=requests.get("https://collectionapi.metmuseum.org/public/collection/v1/departments")
        id_dep=id_dep.json()

        self.nacionalidades=nacionalidades
        archivo=open("CH_Nationality_List_20171130_v1.csv","r")
        nacionalidades=archivo.read()
        archivo.close()

        self.artistas=artistas
        artistas=
