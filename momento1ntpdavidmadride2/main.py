'''En una llantera se ha establecido una promoción de las llantas marca “Ponchadas”, dicha
promoción consiste en lo siguiente:
Si se compran menos de cinco llantas el precio es de $300 cada una, de $250 si se
compran de cinco a 10 y de $200 si se compran mas de 10.
Obtener la cantidad de dinero que una persona tiene que pagar por cada una de las
llantas que compra y la que tiene que pagar por el total de la compra.'''

canlla = int(input("Ingrese la cantidad de llantas que desea comprar: "))

if canlla<5:
    preunilla = 300
elif canlla>=5 and canlla<=10:
    preunilla = 250
else: preunilla = 200
if canlla<5:
    print(f"El precio unitario de sus llantas a comprar es de: ${preunilla} debido a la cantidad que compró ({canlla})")
elif canlla>=5 and canlla<=10:
    print(f"El precio unitario de sus llantas a comprar es de: ${preunilla} debido a la cantidad que compró ({canlla})")
else:
    print(f"El precio unitario de sus llantas a comprar es de: ${preunilla} debido a la cantidad que compró ({canlla})")

valtotpag = (canlla * preunilla)
print(f"Su valor total a pagar es de: ${valtotpag}")
