def departamentos_fun():
    import requests
    id_dep=requests.get("https://collectionapi.metmuseum.org/public/collection/v1/departments")
    id_dep=id_dep.json()

    id=[]
    nombre_dep=[]
    for i in id_dep["departments"]:
        id.append(i["departmentId"])
        nombre_dep.append(i["displayName"])

    print("\nLa siguiente es la lista de los departamentos del museo con sus respectivos Ids:\n")
    for i in range(len(id)):
        print(str(id[i]) + "- " + nombre_dep[i])
    dep_req=input("\nIngrese el Id del departamento en el que está interesado: ")

    api= "https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId=" + dep_req + "&q=%22%22"
    obras=requests.get(api)
    obras=obras.json()
    total=obras["total"]
    limite=int(input("\nEscriba el número de obras que desea visualizar: "))
    print(f"\nEl total de obras es {total}, se muestran las primeras {limite}\n")

    i=0
    if i<limite:
        for i in range(limite):
            print(obras["objectIDs"][i])
            i+=1
    next=input(f"\nPara ver las siguientes {limite}, ingrese 1, si no, ingrese cualquier cosa: ")
    if next=="1":
                i=limite
                for i in range(limite,limite*2):
                    print(obras["objectIDs"][i])
                    i+=1
    else:
        import obras
        id_req= input("Ingrese el ID de la obra en la que esta interesado: ")
        api="https://collectionapi.metmuseum.org/public/collection/v1/objects/" + id_req
        obj=requests.get(api)
        obj=obj.json()
        obras.obras_fun(obj)



    #añadir corrector de que el numero ingresado es un id valido (dep 2 y 20 no existen por ejemplo)