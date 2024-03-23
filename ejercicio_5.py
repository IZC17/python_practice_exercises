entry = """    [D]    
[N] [C]    
[Z] [M] [P]"""
entry = entry.replace("[", "")
entry = entry.replace("]", "")
entry = entry.split("\n")
entry[0] = entry[0].replace("   ", " 0")


print(len(entry[0]))
print(len(entry[1]))
print(len(entry[2]))
print(entry)