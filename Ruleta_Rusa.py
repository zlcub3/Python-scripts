import random
import os

start = input("Realmente quieres jugar? Y/N ----->  ")

if start == "Y" or start == "Yes" or start == "YES" or start == "yes" or start == "y":
    try:
        if random.randint(0, 6) == 1:
            print("Tiro de gracia, perdiste o.o'")
            #os.remove('C:\Windows\System32') "Está comentada la función, quitando el # se descomenta así que cuidado"
        else:
            print("Corriste con suerte, no te salvaras a la próxima!")

    except:
        print("Argumento invalido")

else:
    print("Que cobarde, no escapes de tu destino!")
