'''En una fabrica de computadoras se planea ofrecer a los clientes un descuento que
dependerá del numero de computadoras que compre. Si las computadoras son menos de
cinco se les dará un 10% de descuento sobre el total de la compra; si el numero de
computadoras es mayor o igual a cinco pero menos de diez se le otorga un 20% de
descuento; y si son 10 o mas se les da un 40% de descuento. El precio de cada computadora
es de $11,000'''

cancom = float(input("Ingrese la cantidad de computadores que desea comprar: "))
valtotpag = (cancom * 11000)
print(f"Su valor total a pagar es de: {valtotpag}")
if cancom<5:
    descuento = (valtotpag * 0.10)
elif cancom>=5 and cancom<10:
    descuento = (valtotpag * 0.20)
else: descuento = (valtotpag * 0.40)
if cancom<5:
    print(f"Su descuento de {descuento} sobre el valor total a pagar fue del 10%")
elif cancom>=5 and cancom<10:
    print(f"Su descuento de {descuento} sobre el valor total a pagar fue del 20%")
else:
    print(f"Su descuento de {descuento} sobre el valor total a pagar fue del 40%")

valtotpagdes = (valtotpag - descuento)
print(f"Su valor total a pagar con descuento es de: ${valtotpagdes}")
