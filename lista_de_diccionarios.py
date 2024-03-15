lista = [
    {
        'nombre': 'irving',
        'edad': '24'
    },
    {
        'nombre': 'pedro',
        'edad': '21'
    },
    {
        'nombre': 'pablo',
        'edad': '24'
    },
    {
        'nombre': 'jose',
        'edad': '22'
    },
    {
        'nombre': 'juan',
        'edad': '21'
    }
]

if len(lista) > 3 and lista[0].get('edad') == '24':
    lista.pop(-1)
    print(lista)
else:
    print("no se encontro el valor quitar o el largo no es el deseado")

