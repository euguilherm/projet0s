"par ou impar"
num=int(input("digite um numero para saber se ele e impar ou par "))
val=num%2
if val==0:
    print("O {} e par".format(num))
else:
    print("o {} e impar".format(num))