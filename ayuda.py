#correcion de ejercicio
def mostrar_mensaje(mensaje):
    print("*********************************")
    print(mensaje)
    print("*********************************")

def carga_suma():
    valor1=int(input("ingrese el primer valor "))
    valor2=int(input("ingrese el segundo valor "))
    suma=valor1+valor2
    print("la suma de los dos valores es:", suma)

#programa principal 

mostrar_mensaje("el programa calcula la suma de dos valores ingresados por teclado.")
carga_suma()
mostrar_mensaje("Fin del programa.")