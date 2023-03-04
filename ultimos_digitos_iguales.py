
n = int(input("Digite un número entero: "))
if n > 9 or n < -9:
    n1 = n % 10
    n2 = int((n % 100) / 10)
    if n1 == n2:
        r = "Los últimos dos dígitos son iguales"
    else:
        r = "Los últimos dos dígitos no son iguales"
else:
    r = "El número entero no tiene más de dos dígitos"
print(r)