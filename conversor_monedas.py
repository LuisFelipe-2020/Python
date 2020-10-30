menu = """
Bienvenido al conversor de monedas

1 - Dolares
2 - Euros

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    soles = input("¿Qué cantidad de soles desea convertir?: ")
    soles = float(soles)
    valor_dolar = 3.50
    dolares = soles / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Corresponde: " + dolares + " dolares.")
elif opcion == 2:
    soles = input("¿Qué cantidad de soles desea convertir?: ")
    soles = float(soles)
    valor_euro = 4.20
    euros = soles / valor_euro
    euros = round(euros, 2)
    euros = str(euros)
    print("Corresponde: " + euros + " euros.")
else:
    print("Ingresa una opción")



