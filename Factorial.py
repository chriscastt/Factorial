def calculate_factorial(num):
    if num < 0:
        return "El factorial no está definido para números negativos."
    elif num == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return factorial

num = int(input("Ingrese un número: "))

factorial = calculate_factorial(num)
print(f"El factorial de {num} es {factorial}")