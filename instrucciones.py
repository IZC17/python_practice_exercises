instructions_entry = """move 1 from 3 to 9
move 2 from 2 to 1
move 3 from 5 to 4
move 1 from 1 to 8
move 1 from 3 to 9
move 1 from 5 to 7
move 1 from 5 to 3"""

instructions_entry = instructions_entry.replace("move ", "")
instructions_entry = instructions_entry.replace("from ", "")
instructions_entry = instructions_entry.replace("to ", "")
instructions_entry = instructions_entry.split("\n")

for instructions in instructions_entry:
    instructions = instructions.split(" ")
    print(instructions)
