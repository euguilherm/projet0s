frase=str(input("escreva uma frase ")).upper().strip()
print("sua frase tem {} letra(s) A".format(frase.count("A")))
print("A primeira letra A aparece na posicao {}".format(frase.find("A")+1))
print("A ultima letra A aparece na posicao {}".format(frase.rfind("A")+1))