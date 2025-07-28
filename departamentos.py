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
    input("\nIngrese el Id del departamento en el que está interesado: ")
    #añadir corrector de que el numero ingresado es un id valido (dep 2 y 20 no existen por ejemplo)