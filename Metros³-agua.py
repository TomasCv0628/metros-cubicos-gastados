# Calcular el gasto de agua de una vivienda dado el numero en metros cubicos gastados, siendo
# el sistema del cobro el suigiente:

X = int(input("Inserte metros cubicos consumidos: "))

if X <= 50:
    print("\nEl gasto del agua es igual a $10.000")
elif X <= 200:
    print(f"\nEl gasto de agua es igual a ${10000+(X-50)*2000}")
elif X > 200:
    print(f"\nEL gasto de agua es igual a ${10000+(X-50)*3000}")
else:
    print("\nEl gasto de agua es igual a $0")