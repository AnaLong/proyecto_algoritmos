from Departamento import Departamento
# from Nacionalidad import Nacionalidad
from Obra import Obra,ObraDetallada
from artista import Artista
import requests

class Museo:
    """
    Clase: Museo

    Necesita las clases Obra, Departamento, Nacionalidad y Artista

    Métodos:
    El método start inicia al usuario en un menú que permite escojer el método de búqueda de obras, despues ejecuta diferentes métodos dependiendo de la elección
    El método cargar_datos recauda la información de los departamentos y nacionalidades disponibles y los almacena como listas de los respectivos tipos de objetos
    """
    
    def start(self):
        self.cargar_datos()
        while True:
            menu=input("\nBienvenido al Museo. Los siguientes son los métodos de búsqueda de obras disponibles:\n" \
            "\n1- Búsqueda por departamento\n" \
            "2- Búsqueda por Nacionalidad del artista\n" \
            "3- Búsqueda por Nombre del Artista\n" \
            "4- Salir del sistema\n" \
            "\nIngrese el número asociado al método de búsqueda que desea utilizar: ")
        
            if menu=="1":
                self.obras=[]
                print("\nLa siguiente es la lista de los departamentos del museo con sus respectivos Ids:\n")
                for departamento in self.departamentos:
                    departamento.show_lista()

                menu2=input("\nIndique el id del departamento que en el cual desea buscar: ")
                api= "https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId=" + menu2 + "&q=%22%22"
                obras=requests.get(api)
                obras=obras.json()
                total=obras["total"]
                print(f"\nEl total de obras del departamento es {total}, se muestran las primeras 25: \n")

                for obra in obras["objectIDs"][:25]:
                    aux=requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(obra))
                    aux=aux.json()
                    self.obras.append(Obra(aux["objectID"],aux["title"],aux["artistDisplayName"]))
                for obra2 in self.obras:
                    obra2.show_resumen()
                
                # while True:
                #     elec=input("Si desea ver las siguientes 10, escriba 1")

            elif menu=="2":
                pass
            elif menu=="3":
                self.obras = []
                nombre_autor = input("\nIngrese el nombre del autor que desea buscar: ")

                api = f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nombre_autor}"
                respuesta = requests.get(api)
                datos = respuesta.json()

                total = datos["total"]
                if total == 0:
                    print("\nNo se encontraron obras para ese artista.")
                    continue

                print(f"\nSe encontraron {total} obras. Se muestran las primeras 25:\n")

                for obj_id in datos["objectIDs"][:25]:
                    obra_req = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}")
                    obra_json = obra_req.json()

                    id_obra = obra_json.get("objectID", "Desconocido")
                    titulo = obra_json.get("title", "Desconocido")
                    autor = obra_json.get("artistDisplayName", "Desconocido")

                    self.obras.append(Obra(id_obra, titulo, autor))

                for obra in self.obras:
                    obra.show_resumen()
                    
            elif menu=="4":
                print("\nHa salido del sistema\n")
                break
            else:
                print("\nEl número ingresado no se corresponde a ningún método, por favor intente otra vez\n")
        
    def cargar_datos(self):
        dep_dic=requests.get("https://collectionapi.metmuseum.org/public/collection/v1/departments")
        dep_dic=dep_dic.json()
        obras_dic=requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects")
        obras_dic=obras_dic.json()
    
        self.departamentos=[]

        # for obra in obras_dic["objectIDs"]:
        #     aux=requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(obra))
        #     aux=aux.json()
        #     self.obras.append(Obra(obra,aux["title"],aux["artistDisplayName"],aux["artistNationality"],aux["artistBeginDate"],aux["artistEndDate"],aux["classification"],aux["objectDate"],aux["primaryImage"]))


        for departamento in dep_dic["departments"]:
            self.departamentos.append(Departamento(departamento["departmentId"],departamento["displayName"]))
