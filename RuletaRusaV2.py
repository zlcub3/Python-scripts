import PySimpleGUI as sg
import random
import time
import os

time_duration = 10
spin = random.randint(0, 6)
start = sg.popup_get_text('¿Quieres jugar? Si o No', 'Ruleta Rusa')
sg.popup('Ruleta Rusa', 'Tu respuesta fue: ', start)

if start == "Si" or start == "SI" or start == "si" or start == "sI" or start == "S" or start == "s":
    try:
        if  spin == 1:
            sg.popup('Perdiste, tienes 10 segundos')
            time.sleep(time_duration)
            os.system("shutdown /s /t 1")
 
        else:
            sg.popup('Bala perdida, te salvaste pero aun así te apago')
            time.sleep(time_duration)
            os.system("shutdown /s /t 1")

    except Exception as error:
        print(error)

else:
    sg.popup('No le saques')
