archivo=open("CH_Nationality_List_20171130_v1.csv","r")
nacionalidades=archivo.read()
archivo.close()
print(nacionalidades)
# for i in nacionalidades:
#     print(nacionalidades.index([i])+ "- " + [i])