'''El dueño de una empresa desea planificar las decisiones financieras que tomara en el
siguiente año. La manera de planificarlas depende de lo siguiente:
Si actualmente su capital se encuentra con saldo negativo, pedirá un préstamo
bancario para que su nuevo saldo sea de $10 000. Si su capital tiene actualmente un saldo
positivo pedirá un préstamo bancario para tener un nuevo saldo de $20 000, pero si su
capital tiene actualmente un saldo superior a los $20 000 no pedirá ningún préstamo.
Posteriormente repartirá su presupuesto de la siguiente manera.
$5 000 para equipo de computo
$2 000 para mobiliario
y el resto la mitad será para la compra de insumos y la otra para otorgar
incentivos al personal.
Desplegar que cantidades se destinaran para la compra de insumos e incentivos al
personal y, en caso de que fuera necesario, a cuanto ascendería la cantidad que se pediría al
banco.'''

salcap = int(input("Ingrese el saldo de su capital: $"))

if salcap < 0:
    catsal = 1
elif salcap > 0 and salcap < 20000:
    catsal = 2
else: catsal = 3

if catsal == 1:
    salpreban = 10000
    saltot = salcap + salpreban
elif catsal == 2:
    salpreban: int = 20000
    saltot = salcap + salpreban
elif catsal == 3:
    saltot = salcap

commob: int = 7000
resope1 = (saltot - commob)
insinc = (resope1 / 2)

if insinc > 0:
    print(f"La cantidad a destinar para la compra de insumos al personal es de: ${insinc}")
    print(f"La cantidad a destinar para otorgar incentivos al personal es de:   ${insinc}")
else:
    salpag = abs(salcap)
    print(f"Su valor a solicitar al banco para pasar a saldo positivo asciende a: ${salpag} en total")
    print(f"Su valor a solicitar al banco para pasar a saldo positivo y a su vez obtener un prestamo bancario asciende a: ${(salpag+20000)} en total")
