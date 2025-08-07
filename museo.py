from Departamento import Departamento
from Nacionalidad import Nacionalidad
from Obra import Obra,ObraDetallada
import requests
from time import sleep
from PIL import Image

class Museo:
    """
    Clase: Museo

    Necesita las clases Obra, Obra Detallada, Departamento y Nacionalidad
    Necesita las librerías requests, time (función sleep), y Pillow (función image)
        Las librerias requests y pillow deben ser instaladas en el equipo previamente al ser librerias externas

    Métodos:
    El método start inicia al usuario en un menú que permite escojer el método de búsqueda de obras, despues ejecuta diferentes métodos dependiendo de la elección.
    El método cargar_datos recauda la información de los departamentos y nacionalidades disponibles y los almacena como listas de los respectivos tipos de objetos.
    El metodo busqueda_departamento permite al usuario ver la lista de departamentos disponibles, seleccionar el departamento de su interes, para encontrar las obras almacenadas en el mismo.
    El metodo busqueda_por_autor permite al usuario buscar obras de un autor en especifico a traves de su nombre.
    El metodo busqueda_nacionalidad presenta al usuario una lista de nacionalidades, y le permite buscar la obra de su interes a traves de la nacionalidad de su autor.
    El metodo mostrar_obra_detallada permite al usuario acceder a informacion detallada de una obra seleccionada por su ID. (Se incluye dentro de los metodos de busqueda si el usuario asi lo desea)
    El metodo guardar_imagen_desde_url permite al usuario descargar una imagen de la obra en la que este interesado y la guarda en un archivo. (Se encuentra incluido dentro del metodo mostrar_obra_detallada)
    El metodo muestreo_obras depende de los datos total (total de obras segun el metodo de busqueda y criterios utilizados), muestreo (cantidad de obras a mostrar por tanta) y datos (lista de ids de las obras extraidas segun el metodo y criterio de busqueda)
        Permite mostrar al usuario un numero limitado de obras (con su resumen) por tanda debido a las limitaciones de la api, despues abre un nuevo menu donde el usuario puede elegir si ver la siguiente tanda de obras,
        introducir el id de una obra especifica y ver su informacion detallada, o regresar al menu principal. El metodo se encuentra contenido dentro de los metodos de busqueda, y reintenta conectar con la api esperando un pequeño plazo de tiempo hasta que la
        conexion sea exitosa
    """
    
    def start(self):
        print('\nCargando... Espere un momento.\n')
        self.cargar_datos()
        print('\nCarga Finalizada!\n')
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
                self.busqueda_nacionalidad()

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
        nombre_autor = nombre_autor.split()
        nombre_autor = " ".join(nombre_autor)

        api = f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nombre_autor}"
        respuesta = requests.get(api)
        datos = respuesta.json()

        total = datos["total"]
        muestreo=25
        if total == 0:
            print(f"\nNo se encontraron obras para el artista ({nombre_autor}).")
            return

        else: 
            self.muestreo_obras(datos,total,muestreo)

    def muestreo_obras(self,datos,total,muestreo):
        print(f"\nSe encontraron {total} obras. Se muestran las primeras {muestreo}:\n")

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
        if not menu2.isnumeric(): 
            print('\n Por favor ingrese un numero entero.')
        else:
            menu2=int(menu2)
            if menu2<= 0 or menu2== 2 or menu2== 20 or menu2> 21:
                print('\nDepartamento inexistente, por favor ingrese un id preteneciente a un departamento.')
            else:
                api= "https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId=" + str(menu2) + "&q=%22%22"
                obras=requests.get(api)
                obras=obras.json()
                total=obras["total"]
                muestreo=25
                self.muestreo_obras(obras,total,muestreo)
    
    def busqueda_nacionalidad(self):
        print('\nLista de nacionalidades en')
        for nacionalidad in self.nacionalidades:
            nacionalidad.show()

        micro_menu=input('Escriba la nacionalidad la cual quiera buscar:\n---->')
        seleccion_textual=micro_menu
        micro_menu=micro_menu.split()
        micro_menu=" ".join(micro_menu)
        micro_menu=micro_menu.replace(' ','20%')
        micro_menu=micro_menu.lower()
        api_n='https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q='+ micro_menu
        obras=requests.get(api_n)
        obras=obras.json() 
        total=obras["total"]
        self.obras=[]
        muestreo=25

        if total>0:
            if total<=muestreo:
                muestreo=total
                self.muestreo_obras(obras,total,muestreo)
        else:
            
            print(f'Elemento {seleccion_textual}, no obtuvo resultados.')

    def mostrar_obra_detallada(self):
        self.obra_detallada=[]
        eleccion=input("\n Ingrese el ID de la obra la cual desea ver sus detalles: ")
        aux=requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(eleccion))
        if eleccion.isnumeric():
            aux=aux.json()
            if aux=={"message":"could not parse objectID"}:
                print('error no existe esa id')
            else:
                self.obra_detallada.append(ObraDetallada(aux["objectID"],aux["title"],aux["artistDisplayName"],aux["artistNationality"],aux["artistBeginDate"],aux["artistEndDate"],aux["classification"],aux["objectDate"],aux["primaryImage"]))
                for obra in self.obra_detallada:
                    obra.show_detalles()
                    if obra.imagen:
                        opcion_img = input("\n¿Desea ver y guardar la imagen de la obra? (s/n): ")
                        if opcion_img.lower() == "s":
                            nombre_archivo = f"obra_{obra.id}"
                            archivo_img = self.guardar_imagen_desde_url(obra.imagen, nombre_archivo)
                            if archivo_img:
                                try:
                                    img = Image.open(archivo_img)
                                    img.show()
                                except Exception as e:
                                    print(f"Error al abrir la imagen: {e}")
                    else:
                        print("No hay imagen disponible para esta obra.")
        else:
            print('Por favor ingrese un numero')

    def guardar_imagen_desde_url(self, url, nombre_archivo):
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            content_type = response.headers.get('Content-Type')
            extension = '.png'
            if content_type:
                if 'image/png' in content_type:
                    extension = '.png'
                elif 'image/jpeg' in content_type:
                    extension = '.jpg'
                elif 'image/svg+xml' in content_type:
                    extension = '.svg'
            nombre_archivo_final = f"{nombre_archivo}{extension}"
            with open(nombre_archivo_final, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"Imagen guardada exitosamente como '{nombre_archivo_final}'")
            return nombre_archivo_final
        except requests.exceptions.RequestException as e:
            print(f"Error al hacer el request: {e}")
        except IOError as e:
            print(f"Error al escribir el archivo: {e}")
        return None

    def cargar_datos(self):
        dep_dic=requests.get("https://collectionapi.metmuseum.org/public/collection/v1/departments")
        dep_dic=dep_dic.json()

        archivo=open("CH_Nationality_List_20171130_v1.csv","r")
        lista_provisional=list(archivo)
        lista_provisional.remove("Nationality\n")
        lista_nac=[]
        for i in lista_provisional:
            i=i.replace('\n','')
            lista_nac.append(i)
        archivo.close()

    
        self.departamentos=[]
        self.nacionalidades=[]

        for departamento in dep_dic["departments"]:
            self.departamentos.append(Departamento(departamento["departmentId"],departamento["displayName"]))
        
        for nacionalidad in lista_nac:
            self.nacionalidades.append(Nacionalidad(nacionalidad))