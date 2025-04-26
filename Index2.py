print("Lista de numeros")

n = int(input("Dame un numero:  "))

ml = [2,4,6,8,10]

if n in ml:
    print("Esta en la lista")
elif n not in ml:
    print("No esta en la lista")