#Desarrollar un programa que permita ingresar los lados de un rectangulo y muestre su superficie

def superficie(valor1, valor2):
    multiplicacion = valor1*valor2
    superficie = multiplicacion 
    return superficie


numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))


superficie = superficie(numero1, numero2)

print("la superficie del rectangulo es:", superficie)
print("Fin del programa.")
