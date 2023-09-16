#primer ejercicio del parcial 
def promedio(valor1, valor2, valor3):
    suma = valor1 + valor2 + valor3
    promedio = suma / 3
    return promedio


numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

promedio = promedio(numero1, numero2, numero3)

print("El promedio de los dos números es:", promedio)
print("Fin del programa.")