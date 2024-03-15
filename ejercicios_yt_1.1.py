tiempo_curso = 1.5
tiempo_min = 2.5
tiempo_promedio = 4
tiempo_max = 7

 
diferencia_mas_rapido = f"{round(100-(tiempo_curso / tiempo_min)*100, 2)}%" 
diferencia_promedio = f"{round(100-(tiempo_curso / tiempo_promedio)*100, 2)}%"
diferencia_mas_lento= f"{round(100-(tiempo_curso / tiempo_max)*100, 2)}%"

print(f"{diferencia_promedio} %")

#C
equivalencia_curso_maximo = round((10*tiempo_max)/tiempo_curso, 2)
equivalencia_curso_promedio = round((10*tiempo_promedio)/tiempo_curso, 2)
equivalencia_curso_minimo = round((10*tiempo_min)/tiempo_curso, 2)

print(equivalencia_curso_minimo)