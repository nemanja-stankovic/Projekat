# 5.Napisati fuknciju koja prolazi kroz listu i proverava da li
# su svi elementi istog tipa unutar liste, ako jesu, funkcija
# vraca True, ako nisu vraca False.

lista_1=[0,1,"2",(1,2),5]
lista_2=[0,1,2,12,13,-16]

def da_li_su_elementi_istog_tipa(lista):
    a=0
    for i in range(len(lista)):
        for j in range(len(lista)):
            if type(lista[i]) != type(lista[j]):
                a+=1
    if a==0:
        return True
    else:
        return False

print(f"Jesu li elementi liste {lista_1} istog tipa ?\n{da_li_su_elementi_istog_tipa(lista_1)}")
print(f"Jesu li elementi liste {lista_2} istog tipa ?\n{da_li_su_elementi_istog_tipa(lista_2)}")