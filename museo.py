from Departamento import Departamento
# from Nacionalidad import Nacionalidad
from Obra import Obra,ObraDetallada
import requests
from time import sleep

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
                self.busqueda_departamento()

            elif menu=="2":
                pass
            elif menu=="3":
                self.busqueda_por_autor()
                    
            elif menu=="4":
                print("\nHa salido del sistema\n")
                break

            else:
                print("\nEl número ingresado no se corresponde a ningún método, por favor intente otra vez\n")
    
    def busqueda_por_autor(self):
        self.obras = []
        nombre_autor = input("\nIngrese el nombre del autor que desea buscar: ")

        api = f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nombre_autor}"
        respuesta = requests.get(api)
        datos = respuesta.json()

        total = datos["total"]
        if total == 0:
            print("\nNo se encontraron obras para ese artista.")
            return

        print(f"\nSe encontraron {total} obras. Se muestran las primeras 25:\n")

        muestreo = 25
        contador = 1

        while True:
            inicio = (contador * muestreo) - muestreo
            fin = contador * muestreo

            for obj_id in datos["objectIDs"][inicio:fin]:
                for intento in range(3):
                    obra_req = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}")
                    if obra_req.status_code == 200:
                        try:
                            datos2=obra_req.json()
                            self.obras.append(Obra(datos2["objectID"],datos2["title"],datos2["artistDisplayName"]))
                            break
            
                        except ValueError:
                            print("Error")
                            break
                    else:
                        print("\nNo se pudo conectar con la api. Reintentando...")
                        sleep(20)

            for obra in self.obras[inicio:fin]:
                obra.show_resumen()

            eleccion = input("\n1- Ver las siguientes 25 obras.\n" \
                               "2- Seleccionar una obra en específico y ver su informacion detallada.\n" \
                               "3- Volver al menu principal\n"
                               "\n---> ")

            if eleccion == "1":
                contador += 1
            elif eleccion == "2":
                self.mostrar_obra_detallada()
                break
            elif eleccion == "3":
                print("\nVolviendo al menu principal\n")
                break
            else:
                print("\nPor favor seleccione una de las opciones anteriores\n")   

    def busqueda_departamento(self):
        self.obras=[]
        print("\nLa siguiente es la lista de los departamentos del museo con sus respectivos Ids:\n")
        for departamento in self.departamentos:
            departamento.show_lista()

        menu2=input("\nIndique el id del departamento que en el cual desea buscar: ")
        api= "https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId=" + menu2 + "&q=%22%22"
        obras=requests.get(api)
        obras=obras.json()
        total=obras["total"]
        muestreo= 25
        contador= 1
        print(f"\nEl total de obras del departamento es {total}, se muestran las primeras {muestreo}: \n")
        while True:
            inicio=(contador*muestreo)-muestreo
            fin=contador*muestreo
            for obra in obras["objectIDs"][inicio:fin]:
                for intento in range(3):
                    aux=requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(obra))
                    if aux.status_code==200:
                        try:
                            datos=aux.json()
                            self.obras.append(Obra(datos["objectID"],datos["title"],datos["artistDisplayName"]))
                            break
                        except ValueError: 
                            print("Error")
                            break
                    else:
                        print("\nNo se pudo conectar con la api. Reintentando...")
                        sleep(20)

            for obra2 in self.obras[inicio:fin]:
                obra2.show_resumen()

            eleccion=input("\n1- Ver las siguientes 25 obras.\n" \
            "2- Seleccionar una obra en específico y ver su informacion detallada.\n" \
            "3- Volver al menu principal\n"
            "\n---> ")

            if eleccion=="1":
                contador += 1

            elif eleccion=="2":
                self.mostrar_obra_detallada()
                break

            elif eleccion=="3":
                print("\nVolviendo al menu principal\n")
                break
            else: 
                print("\nPor favor seleccione una de las opciones anteriores\n")

    def mostrar_obra_detallada(self):
        self.obra_detallada=[]
        eleccion=input("\n Ingrese el ID de la obra la cual desea ver sus detalles: ")
        aux=requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(eleccion))
        aux=aux.json()
        self.obra_detallada.append(ObraDetallada(aux["objectID"],aux["title"],aux["artistDisplayName"],aux["artistNationality"],aux["artistBeginDate"],aux["artistEndDate"],aux["classification"],aux["objectDate"],aux["primaryImage"]))
        for obra in self.obra_detallada:
            obra.show_detalles()

    def cargar_datos(self):
        dep_dic=requests.get("https://collectionapi.metmuseum.org/public/collection/v1/departments")
        dep_dic=dep_dic.json()
        obras_dic=requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects")
        obras_dic=obras_dic.json()
    
        self.departamentos=[]

        for departamento in dep_dic["departments"]:
            self.departamentos.append(Departamento(departamento["departmentId"],departamento["displayName"]))
