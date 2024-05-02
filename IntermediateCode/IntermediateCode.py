class IntermediateCodeGenerator:
    def __init__(self):
        self.source_code = [
            "START 100",
            "READ A",
            "READ B",
            "MOVER AREG, A",
            "SUB AREG, B",
            "STOP",
            "A DS 1",
            "B DS 1",
            "END"
        ]
        self.intermediate_code = []
      
    def generate_intermediate_code(self):
        for line in self.source_code:
            tokens = line.split()
            opcode = tokens[0]
            operand = ""
            if len(tokens) > 1:
                operand = tokens[1]
            if opcode.upper() == "START":
                self.intermediate_code.append("AD " + opcode + ", " + operand)
            elif opcode.upper() == "READ":
                self.intermediate_code.append("IS 1, " + operand)
            elif opcode.upper() == "MOVER":
                self.intermediate_code.append("IS 4, " + operand + " AREG")
            elif opcode.upper() == "SUB":
                self.intermediate_code.append("IS 2, " + operand + " BREG")
            elif opcode.upper() == "STOP":
                self.intermediate_code.append("IS 0")
            elif opcode.upper() == "DS":
                self.intermediate_code.append("DL 1, " + operand)
            elif opcode.upper() == "END":
                self.intermediate_code.append("AD " + opcode)


    def print_intermediate_code(self):
        print("Intermediate Code:")
        for code in self.intermediate_code:
            print(code)




# Create an instance of IntermediateCodeGenerator
generator = IntermediateCodeGenerator()
# Generate intermediate code
generator.generate_intermediate_code()
# Print intermediate code
generator.print_intermediate_code()
