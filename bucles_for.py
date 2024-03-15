#valores = []
#for numero_ciclo in range(1,6):
#   valor = float(input(f"Ingresa el número {numero_ciclo} a promediar "))
#   valores.append(valor)
#print(sum(valores)/len(valores))


promedio = sum([int(input(f"Ingresa el número {valor} a promediar ")) for valor in range(1,6)])/5
print(promedio)