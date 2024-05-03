class Assembler:
    IS = {
        "STOP": 0,
        "ADD": 1,
        "SUB": 2,
        "MUL": 3,
        "MOVER": 4,
        "MOVEM": 5,
        "COMP": 6,
        "BC": 7,
        "DIV": 8,
        "READ": 9,
        "PRINT": 10
    }

    AD = {
        "STOP": 0,
        "ADD": 1,
        "SUB": 2,
        "MUL": 3,
        "MOVER": 4,
        "MOVEM": 5,
        "COMP": 6,
        "BC": 7,
        "DIV": 8,
        "READ": 9,
        "PRINT": 10,
        "START": 11,
        "END": 12,
        "ORIGIN": 13,
        "EQU": 14,
        "LTORG": 15
    }

    DL = {
        'DS': 0,
        'DC': 1
    }

    RG = {
        "AREG": 0,
        "BREG": 1,
        "CREG": 2
    }

    def process_symbol_table(self, line) -> None:
        line = line.strip()
        parts = line.split()
        self.symbol_table[parts[0]] = self.lc

    def process_ltorg(self, line):
        tokens = line.split('=')
        literal = tokens[1]
        self.literal_table[literal] = None

    def process_ltorg_or_end(self):
        for key in self.literal_table.keys():
            if self.literal_table.get(key) == None:
                self.literal_table[key] = self.lc
                self.lc += 1

    def pass1(self) -> None:
        for line in self.source_code:
            if line.startswith("START"):
                self.lc = int(line.split()[1])
            elif line.startswith("LTORG"):
                self.process_ltorg_or_end()
            elif line.startswith("END"):
                self.process_ltorg_or_end()
            else:
                parts = line.split()
                if parts[0] not in self.IS:
                    self.process_symbol_table(line)
                elif '=' in line:
                    self.process_ltorg(line)
                elif len(parts) > 1 and parts[1] == 'DS':
                    self.lc += int(parts[2]) - 1
                self.lc += 1

    def pass2(self) -> None:
        for line in self.source_code:
            line = line.strip()
            tokens = line.split()
            tokens = [t.replace(',', '') for t in tokens]

            inter_line = ""
            for token in tokens:
                token = token.strip('=')
                if token in self.IS:
                    inter_line += f' (IS, {self.IS[token]}) '
                elif token in self.AD:
                    inter_line += f' (AD, {self.AD[token]}) '
                elif token in self.DL:
                    inter_line += f' (DL, {self.DL[token]}) '
                elif token in self.RG:
                    inter_line += f' (RG, {self.RG[token]}) '
                elif token in self.symbol_table:
                    inter_line += f' (S, {self.symbol_table[token]}) '
                elif token in self.literal_table:
                    inter_line += f' (L, {self.literal_table[token]}) '
                else:
                    inter_line += f' (C, {token}) '

            self.intermediate_code.append(inter_line)

    def print_intermediate_code(self):
        print('\n\nIntermediate Code')

        for line in self.intermediate_code:
            print(line)

    def __init__(self, source_code):
        self.source_code = source_code
        self.intermediate_code = []
        self.symbol_table = {}
        self.literal_count = 0
        self.literal_table = {}
        self.lc = 0

        self.pass1()
        self.pass2()

        self.print_intermediate_code()


def main():
    source_code = [
        "START 180",
        "READ M",
        "READ N",
        "LOOP MOVER AREG, M",
        "MOVER BREG, N",
        "COMP BREG, ='200'",
        "BC GT, LOOP",
        "BACK SUB AREG, M",
        "COMP AREG, ='500'",
        "BC  LT, BACK",
        "STOP",
        "M DS 1",
        "N DS 1",
        "END"
    ]

    obj = Assembler(source_code)


if __name__ == '__main__':
    main()
# //
