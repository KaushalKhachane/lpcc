# Assembly source code
assembly_code = [
    "START 100",
    "READ A",
    "MOVER AREG, ='1'",
    "MOVEM AREG, B",
    "MOVER BREG, ='6'",
    "ADD AREG, BREG",
    "COMP AREG, A",
    "BC GT, LAST",
    "LTORG",
    "NEXT SUB AREG, ='1'",
    "MOVER CREG, B",
    "ADD CREG, ='8'",
    "MOVEM CREG, B",
    "PRINT B",
    "LAST STOP",
    "A DS 1",
    "B DS 1",
    "END",
]

# List to track where each literal pool starts
pool_table = []

# List to track the literals
literal_pool = []

# Current location counter
current_location_counter = 100

# Step 1: Identify literals and pool start points
for line in assembly_code:
    parts = line.split()
    
    if len(parts) == 0:
        continue
    
    # Increment location counter if it's not a directive
    if parts[0] not in ["START", "LTORG", "END"]:
        current_location_counter += 1
    
    # Check for literals in the line
    for part in parts:
        if part.startswith("='") and part.endswith("'"):
            if part not in literal_pool:
                literal_pool.append(part)

    # When encountering LTORG, mark the pool's start point
    if parts[0] == "LTORG":
        pool_table.append(current_location_counter)
        # After LTORG, literals are "written" into memory
        current_location_counter += len(literal_pool)
        
        # Clear the literal pool as they have been placed
        literal_pool.clear()

# If END is encountered, mark the last pool's start point
if "END" in [line.split()[0] for line in assembly_code]:
    if literal_pool:
        pool_table.append(current_location_counter)

# Display the pool table
print("Pool Table:")
print("Pool Start Address")
for address in pool_table:
    print(address)

