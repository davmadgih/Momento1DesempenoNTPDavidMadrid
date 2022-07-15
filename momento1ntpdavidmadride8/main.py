'''Una institución educativa estableció un programa para estimular a los alumnos con buen
rendimiento académico y que consiste en lo siguiente:
Si el promedio es de 9.5 o mas y el alumno es de preparatoria, entonces este podrá
cursar 55 unidades y se le hará un 25% de descuento.
-
Si el promedio es mayor o igual a 9 pero menor que 9.5 y el alumno es de
preparatoria, entonces este podrá cursar 50 unidades y se le hará un 10% de descuento.
-
Si el promedio es mayor que 7 y menor que 9 y el alumno es de preparatoria, este
podrá cursar 50 unidades y no tendrá ningún descuento.
-
Si el promedio es de 7 o menor, el numero de materias reprobadas es de 0 a 3 y el
alumno es de preparatoria, entonces podrá cursar 45 unidades y no tendrá descuento.
-
Si el promedio es de 7 o menor, el numero de materias reprobadas es de 4 o mas y el
alumno es de preparatoria, entonces podrá cursar 40 unidades y no tendrá ningún
descuento.
-
Si el promedio es mayor o igual a 9.5 y el alumno es de profesional, entonces podrá
cursar 55 unidades y se le hará un 20% de descuento.
-
Si el promedio es menor de 9.5 y el alumno es de profesional, entonces podrá cursar
55 unidades y no tendrá descuento.
-
Obtener el total que tendrá que pagar un alumno si la colegiatura para alumnos de
profesional es de $300 por cada cinco unidades y para alumnos de preparatoria es de $180
por cada cinco unidades.'''

promedio = float(input("Ingrese su promedio academico: "))
tipalu = int(input('''Ingrese a que categoría de estudiante pertenece, si es de preparatoria ingrese 1,
de lo contrario ingrese cualquier numero: '''))

if promedio <= 7:
    matrep = int(input("Ingrese la cantidad de materias reprobadas: "))

if promedio >= 9.5 and tipalu == 1:
    valounid = 11
    descuento = 0.25
elif (promedio >= 9) and (promedio < 9.5) and (tipalu == 1):
    valounid = 10
    descuento = 0.10
elif (promedio > 7) and (promedio < 9) and (tipalu == 1):
    valounid = 10
    descuento = 0
elif (promedio <= 7) and (matrep >= 0) and (matrep <= 3) and (tipalu == 1):
    valounid = 9
    descuento = 0
elif (promedio <= 7) and (matrep >= 4) and (tipalu == 1):
    valounid = 8
    descuento = 0
elif promedio >= 9.5 and tipalu != 1:
    valounid = 11
    descuento = 0.20
elif promedio < 9.5 and tipalu != 1:
    valounid = 11
    descuento = 0

if tipalu == 1:
    valcol = 180
else:
    valcol = 300

valbrupagalu = (valounid * valcol)
desvalbru = (valbrupagalu * descuento)
valtotpagalu = (valbrupagalu - desvalbru)

print(f"El valor total a pagar por el alumno es de: ${valtotpagalu}")
