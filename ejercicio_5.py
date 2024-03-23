entry = """[D]                     [N] [F]    
[H] [F]             [L] [J] [H]    
[R] [H]             [F] [V] [G] [H]
[Z] [Q]         [Z] [W] [L] [J] [B]
[S] [W] [H]     [B] [H] [D] [C] [M]
[P] [R] [S] [G] [J] [J] [W] [Z] [V]
[W] [B] [V] [F] [G] [T] [T] [T] [P]
[Q] [V] [C] [H] [P] [Q] [Z] [D] [W]"""
entry = entry.replace("[", "")
entry = entry.replace("]", "")
entry = entry.split("\n")
index = 0
for index_for in entry:
    index = index
    entry[index] = entry[index].replace("    ", " 0")
    entry[index] = entry[index].replace(" ", "")
    index = index+1


print(entry)