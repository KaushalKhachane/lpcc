# Assembly source code
assembly_code1 = [
    "START 100",
    "READ A",
    "READ B",
    "MOVER AREG, ='50'",
    "MOVER BREG, ='60'",
    "ADD AREG, BREG",
    "LOOP MOVER CREG, A",
    "ADD CREG, ='10'",
    "COMP CREG, B",
    "BC LT, LOOP",
    "NEXT SUB AREG, ='10'",
    "COMP AREG, B",
    "BC GT, NEXT",
    "STOP",
    "A DS 1",
    "B DS 1",
    "END",
]

assembly_code2 = [
    "START 200",
    "READ X",
    "READ Y",
    "   MOVER AREG, ='5'",
    "   MOVER BREG, ='6'",
    "       ADD AREG, BREG",
    "LOOP   MOVER CREG, X",
    "       ADD  CREG, ='1'",
    "       COMP CREG, Y",
    "       BC LT, LOOP",
    "NEXT   SUB AREG, ='1'",
    "       COMP AREG, Y",
    "       BC GT, NEXT",
    "STOP",
    "X       DS 1",
    "Y       DS 1",
    "END"
]

assembly_code3 = [
    "START 300",
    "READ M",
    "READ N",
    "   MOVER AREG, ='51'",
    "   MOVER BREG, ='61'",
    "       ADD AREG, BREG",
    "LOOP   MOVER CREG, M",
    "       ADD  CREG, ='11'",
    "       COMP CREG, N",
    "       BC LT, LOOP",
    "NEXT   SUB AREG, ='11'",
    "       COMP AREG, N",
    "       BC GT, NEXT",
    "STOP",
    "M       DS 1",
    "N       DS 1",
    "END"
]


# Step 1: Find all literals in the code
literal_pool = []
literal_addresses = {}

# Set an initial memory address (after "START")
current_location_counter = 100

# Process each line to find literals
for line in assembly_code3:
    parts = line.split()
    if len(parts) == 0:
        continue

    for part in parts:
        # Check if part is a literal
        if part.startswith("='") and part.endswith("'"):
            literal_value = part
            # If not already in the literal pool, add it
            if literal_value not in literal_pool:
                literal_pool.append(literal_value)

for line in assembly_code3:
    # Split the line into components
    parts = line.split()
    
    # Check if it's an instruction or directive
    if parts[0] not in ["START"]:
        current_location_counter += 1
    
    print(parts[0],  " ", current_location_counter)
    if parts[0] == "END":
        # Literals typically start after all other instructions and symbols
        for literal in literal_pool:
            if literal not in literal_addresses:
                literal_addresses[literal] = current_location_counter
                current_location_counter += 1

print("Literal Table:")
print("Literal\tAddress")
for literal, address in literal_addresses.items():
    print(f"{literal}\t{address}")
