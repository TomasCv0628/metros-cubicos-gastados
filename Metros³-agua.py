# Calcular el gasto de agua de una vivienda dado el numero en metros cubicos gastados, siendo
# el sistema del cobro el suigiente:

print("\n⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜")
print("⚜⚜⚜⚜⚜⚜⚜ Valor de la cantidad ⚜⚜⚜⚜⚜⚜⚜⚜")
print("⚜⚜⚜⚜⚜⚜⚜⚜⚜ de metros cubicos ⚜⚜⚜⚜⚜⚜⚜⚜⚜")
print("⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜ consumidos ⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜")
print("⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜")
print("⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜\n")


X = int(input("\nInserte metros cubicos consumidos: "))

if X <= 50:
    print("\nEl gasto del agua es igual a $10.000")
elif X <= 200:
    print(f"\nEl gasto de agua es igual a ${10000+(X-50)*2000}")
elif X > 200:
    print(f"\nEL gasto de agua es igual a ${10000+(150)*2000 + (X-200)*3000}")
else:
    print("\nEl gasto de agua es igual a $0")
