def departamentos_fun():
    import requests
    id_dep=requests.get("https://collectionapi.metmuseum.org/public/collection/v1/departments")
    id_dep=id_dep.json()
    class Departamento:
            def __init__(self,id_dep):
                self.id=[]
                self.nombre=[]
                for i in id_dep["departments"]:
                    self.id.append(i["departmentId"])
                    self.nombre.append(i["displayName"])
        
            def __str__(self):
                print("\nLa siguiente es la lista de los departamentos del museo con sus respectivos Ids:\n")
                for i in range(len(self.id)):
                    print(str(self.id[i]) + "- " + self.nombre[i])
                return ""
            def auxiliar(obras):
                total=obras["total"]
                limite=int(input(f"\nEl total de obras es {total}. Escriba el número de obras que desea visualizar: "))
                print(f"\nSe muestran las primeras {limite} obras\n")
                i=0
                if i<limite:
                     for i in range(limite):
                        print(obras["objectIDs"][i])
                        i+=1
                import obras
                return obras.obras_fun()
                 
    dep_bus= Departamento(id_dep)
    print(dep_bus)
    dep_req=input("\nIngrese el Id del departamento en el que está interesado: ")
    api= "https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId=" + dep_req + "&q=%22%22"
    obras=requests.get(api)
    obras=obras.json()
    dep_req=Departamento.auxiliar(obras)


    # next=input(f"\nPara ver las siguientes {limite}, ingrese 1, si no, ingrese cualquier cosa: ")
    # if next=="1":
    #             i=limite
    #             for i in range(limite,limite*2):
    #                 print(obras["objectIDs"][i])
    #                 i+=1
    # else:




    #añadir corrector de que el numero ingresado es un id valido (dep 2 y 20 no existen por ejemplo)