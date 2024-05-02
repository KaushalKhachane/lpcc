assembly_code = [
    "START 180",
    "READ M",
    "READ N",
    "LOOP MOVER AREG, M",
    "MOVER BREG, N",
    "COMP BREG, ='200'",
    "BC GT, LOOP",
    "BACK SUB AREG, M",
    "COMP AREG, ='500'",
    "BC LT, BACK",
    "STOP",
    "M DS 1",
    "N DS 1",
    "END",
]

assembly_code1 = [
    "START 100",
    "READ A",
    "READ B",
    "LOOP    MOVER AREG, A  ",
    "        MOVER BREG, B  ",
    "        COMP BREG, ='2' ",
    "        BC GT, LOOP",
    "BACK    SUB AREG, B",
    "        COMP AREG, ='5'",
    "        BC  LT, BACK ",
    "STOP",
    "A       DS  1",
    "B       DS  1",
    "END"
]

assembly_code2 = [
    "START 150",
    "READ D",
    "READ E",
    "LOOP    MOVER AREG, D",
    "        MOVER BREG, E",
    "        COMP BREG, ='20'",
    "        BC GT, LOOP",
    "BACK    SUB AREG, E",
    "        COMP AREG, ='50'",
    "        BC LT, BACK",
    "STOP",
    "D       DS 1",
    "E       DS 1",
    "END"
]



symbol_table = {}

lc = 180

for line in assembly_code2:
    parts = line.split()
    if len(parts) == 0:
        continue    
    
    first_word = parts[0]

    if first_word == "START":
        if len(parts) > 1:
            lc = int(parts[1])
        
    if len(parts) > 2 and parts[1] == "DS":
        symbol_table[parts[0]] = lc
        lc = lc + int(parts[2])
        continue

    if first_word in ["READ", "MOVER", "COMP", "BC", "SUB", "STOP", "END", "START"]:
        lc += 1
        continue

    if first_word not in symbol_table:
        symbol_table[first_word] = lc

    lc += 1


print("Symbol Table: ")
print("Symbol \t Location Counter: ")
for symbol, location_counter in symbol_table.items():
    print(f"{symbol}\t{location_counter}")