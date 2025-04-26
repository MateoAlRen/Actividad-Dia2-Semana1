print("Lista de numeros con indicacion al menor valor")

n1 = int(input("Dame un numero:  "))
n2 = int(input("Dame otro numero:  "))
n3 = int(input("Dame un tercer numero:  "))

ml = [n1, n2, n3]

if n1 < n2 and n1 < n3:
    print("El numero mas pequeño es:  ", n1)
elif n2 < n1 and n2 < n3:
    print("El numero mas pequeño es:  ", n2)
elif n3 < n1 and n3 < n2:
    print("El numero mas pequeño es:  ", n3)