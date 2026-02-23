from random import choice 
chute=int(input('De seu chute de 1 a 3. '))
list= 1, 2, 3
esc=choice(list)
if chute == esc:
    print(' PARABENS!!! VOCE ACERTOU.')
else:
    print('Talvez na proxima...')
    