tiempo_palabras_segundo = 2

palabras_usuario = input("Ingresa aquí tu texto: ")
numero_palabras = len(palabras_usuario.split())
tiempo_frase = numero_palabras/tiempo_palabras_segundo
print(numero_palabras)
print("-------------------")
print(f"{tiempo_frase} segundos")

print("-------------------")
if tiempo_frase > 60:
    print("mucho texto")
else:
    print("bien resumido")
    
tiempo_mas_rapido = round(tiempo_frase*0.3, 2)

print("-------------------")
print(f"{tiempo_mas_rapido} segundos")