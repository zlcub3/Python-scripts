
total = []

def inicio():
    menu = input("""
|================================|
|        RESTAURANTE S.A         |
|              MENÚ              |
|================================|
| A | DESAYUNO                   |
| B | ALMUERZO                   |
| C | CENA                       |
|--------------------------------|
| D |         SALIR              |
|================================|
""")
    if menu == "A" or "a":
        desayuno_ = desayuno()
    elif menu == "B" or "b":
        almuerzo_ = almuerzo()
    elif menu == "C" or "c":
        cena_ = cena()
    elif menu == "D" or "d":
        salida_ = salida()
    else: 
        print("Digite un valor valido")
        inicio_ = inicio()

def desayuno():
    menu_desayuno = input("""
|================================|
|            DESAYUNO            |
|================================|
| A | CAFÉ              | S/4.50 |
| B | CHOCOLATE         | S/5.00 |
| C | JUGO DE FRESA     | S/9.00 |
| D | JUGO DE PAPAYA    | S/8.00 |
| E | PAN CON POLLO     | S/7.00 |
| F | PAN CON JAMÓN     | S/7.00 |
| G | PAN CON TORTILLA  | S/7.00 |
|--------------------------------|
| H |         SALIR              |
|================================|""")
    if menu_desayuno == "H" or "h":
        inicio_ = inicio()

def almuerzo(): 
    print("""
|================================|
|            ALMUERZO            |
|================================|
| A | CAFÉ              | S/4.50 |
| B | CHOCOLATE         | S/5.00 |
| C | JUGO DE FRESA     | S/9.00 |
| D | JUGO DE PAPAYA    | S/8.00 |
| E | PAN CON POLLO     | S/7.00 |
| F | PAN CON JAMÓN     | S/7.00 |
| G | PAN CON TORTILLA  | S/7.00 |
|--------------------------------|
| H |         SALIR              |
|================================|""")

def cena():
    print("""
|================================|
|              CENA              |
|================================|
| A | DESAYUNO                   |
| B | ALMUERZO                   |
| C | CENA                       |
|--------------------------------|
| D |         SALIR              |
|================================|""")

def salida():
    print("""
|================================|
|        BOLETA DE VENTAS        |
|================================|
| Subtotal:                      |
| Igv:                           |
| Total a pagar:                 |
|--------------------------------|
|      Gracias por su compra     |
|================================|""")

if __name__ == '__main__':
    inicio()
    
