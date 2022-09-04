#CALCULADORA SIMPLE EN PYTHON BY ZLCUBE
#Puedes apoyarme en mi redes sociales, ZLCube en todas ellas TIKTOK, YOUTUBE, TWITTER, IG Y TWITCH

titulo = """

==============================================================================================================================================
_________        .__               .__              .___                    ___.           __________.____   _________      ___.           
\_   ___ \_____  |  |   ____  __ __|  | _____     __| _/________________    \_ |__ ___.__. \____    /|    |  \_   ___ \ __ _\_ |__   ____  
/    \  \/\__  \ |  | _/ ___\|  |  \  | \__  \   / __ |/  _ \_  __ \__  \    | __ <   |  |   /     / |    |  /    \  \/|  |  \ __ \_/ __ \ 
\     \____/ __ \|  |_\  \___|  |  /  |__/ __ \_/ /_/ (  <_> )  | \// __ \_  | \_\ \___  |  /     /_ |    |__\     \___|  |  / \_\ \  ___/ 
 \______  (____  /____/\___  >____/|____(____  /\____ |\____/|__|  (____  /  |___  / ____| /_______ \|_______ \______  /____/|___  /\___  >
        \/     \/          \/                \/      \/                 \/       \/\/              \/        \/      \/          \/     \/ 
        
==============================================================================================================================================

"""                                                                                                                     
        
print (titulo)

print("""
   ___                                       _               _                                 _ _            ___  
  / _ \ _  _ ___   ___ _ __  ___ _ _ __ _ __(_)___ _ _    __| |___ ___ ___ __ _   _ _ ___ __ _| (_)_____ _ _ |__ \ 
 | (_) | || / -_) / _ \ '_ \/ -_) '_/ _` / _| / _ \ ' \  / _` / -_|_-</ -_) _` | | '_/ -_) _` | | |_ / _` | '_|/_/ 
  \__\_\\_,_\___| \___/ .__/\___|_| \__,_\__|_\___/_||_| \__,_\___/__/\___\__,_| |_| \___\__,_|_|_/__\__,_|_| (_)  
                      |_|                                                                                          
""")
print("==============================================================================================================================================")
print("Suma + / resta - / multiplicacion * / division %  ")
print("==============================================================================================================================================")

operacion = input("Digite la ooeracion: ")

if operacion == "+":
	n1 = int(input("Digite el primer numero: "))
	n2 = int(input("Digite el segundo numero: "))
	suma = n1 + n2
	print("La suma es: ")
	print(suma)
	
elif operacion == "-":
	n1 = int(input("Digite el primer numero: "))
	n2 = int(input("Digite el segundo numero: "))
	resta = n1 - n2
	print("La resta es: ")
	print(resta) 

elif operacion == "*":
	n1 = int(input("Digite el primer numero: "))
	n2 = int(input("Digite el segundo numero: "))
	multiplicar = n1 * n2
	print("La multiplicacion es: ")
	print(multiplicar)

elif operacion == "%":
	n1 = int(input("Digite el primer numero: "))
	n2 = int(input("Digite el segundo numero: "))
	dividir = n1 % n2
	print("La division es: ")
	print(dividir)

else: 
	print("Valor invalido")
