"""
$= comandos que ejecuto
cd significa cambiar de directorio
    cd x se mueve en un nivel: busca en el directorio actual el directorio nombrado x y lo convierte en el directorio actual.
    cd .. sale un nivel : encuentra el directorio que contiene el directorio actual y luego convierte ese directorio en el directorio actual .
    cd /cambia el directorio actual al directorio más externo, /.
lssignifica lista . Imprime todos los archivos y directorios contenidos inmediatamente en el directorio actual:
    123 abc significa que el directorio actual contiene un archivo cuyo nombre abc tiene tamaño 123.
    dir xyz significa que el directorio actual contiene un directorio llamado xyz.
"""

input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

input_list = input.split("\n")
#print(input_list)

input_dirs_slice = []
for create_list in input_list:
    if create_list.__contains__("dir"):
        create_list = create_list.replace("dir ","")
        create_list = list(create_list)
    input_dirs_slice.append(create_list)


index = 0
filtered_list = []
for elements_in_dirs in input_dirs_slice:
    
    if elements_in_dirs.__contains__("ls"):
        continue
    else:
    
        if type(elements_in_dirs) == str:
            if elements_in_dirs[0].isalnum() == True:
                elements_in_dirs = elements_in_dirs.split(" ")
                elements_in_dirs.pop(1)
                elements_in_dirs = "".join(elements_in_dirs)
                elements_in_dirs = int(elements_in_dirs)
    filtered_list.append(elements_in_dirs)
    index = index+1


print(filtered_list)   