archivo=open("CH_Nationality_List_20171130_v1.csv","r")
lista_nac=list(archivo)
lista_nac.remove('Nationality\n')
lista_nac = [i.replace('\n','') for i in lista_nac]
archivo.close()
def nac():
    x=0
    for i in lista_nac:
        print(f'{x}-{i}')
        x+=1
    nac_selec=int(input('Ingrese el numero de la nacionalidad escogida'))
    if nac_selec>=225:
        print('No es valido, ingrese un numero natural que este dentro del intervalo')
        nac()
    elif nac_selec>1 or nac_selec<224:
        print(lista_nac[nac_selec])      
        pass 
nac()
    
