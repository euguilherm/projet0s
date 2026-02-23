from random import randint
vel= randint(0, 200)
print("Voce esta dirigindo a ",vel, "Km")
print('=++='*20)
if vel < 80:
    print("Voce esta dentro do limite. Siga seu caminho e Boa Viagem!!")
else:
    print("Voce esta acima do limite de velocidade! Acaba de receber uma multa.")
    print('=++='*20)
    if vel>80:
        print(" Sua multa e no valor de {} R$".format((vel-80)*7))