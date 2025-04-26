print("Lista de Invitados")

inv = input("Por favor, ingrese su nombre:  ")

lst = ["Juan", "Mateo", "Samuel"]

if inv in lst:
    print("Esta en la lista")
elif inv not in lst:
    print("No está en la lista")