def main():

    print("Los siguientes son los métodos de búsqueda de obras disponibles:\n" \
            "1- Búsqueda por departamento\n" \
            "2- Búsqueda por Nacionalidad del artista\n" \
            "3- Búsqueda por Nombre del Artista\n")
    busqueda=input("\nIngrese el número asociado al método de búsqueda que desea utilizar: ")

    if busqueda=="1":
        import departamentos
        departamentos.departamentos_fun()
    elif busqueda=="2":
        pass
    elif busqueda=="3":
        pass
    else:
        print("\nEl número ingresado no se corresponde a ningún método, por favor intente otra vez\n")
        main()

main()

