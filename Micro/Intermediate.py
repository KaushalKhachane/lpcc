class Macro:
    def __init__(self, source) -> None:
        self.mdt = []
        self.mnt = {}
        self.lc = 0
        self.mdt_idx = 0
        self.intermediate_code = []

        self.pass1(source)
        self.pass2(source)

        self.print_mnt()
        self.print_mdt()
        self.print_intermediate_code()

    def print_mnt(self):
        print('\n\nMNT:')
        for macro_name, idx in self.mnt.items():
            print(f'{macro_name}  {idx}')

    def print_mdt(self):
        print('\n\nMDT:')
        for line in self.mdt:
            print(line)

    def print_intermediate_code(self):
        print('\n\nIntermediate Code:')
        for line in self.intermediate_code:
            print(line)

    def pass1(self, source_code):
        n = len(source_code)
        i = 0
        while i < n:
            line = source_code[i].strip()

            tokens = line.split()
            if tokens[0] == 'MACRO':
                macro_name = tokens[1]
                args = []
                for a in range(2, len(tokens)):
                    args.append(tokens[a])
                args = [word.replace(',', '') for word in args]

                self.mnt[macro_name] = [self.mdt_idx, args]

                i += 1

                while i < n:
                    line = source_code[i].strip()
                    self.mdt.append(line)
                    self.mdt_idx += 1
                    if 'MEND' in line:
                        break
                    i += 1
            i += 1

    def utility(self, macro_name, arguments):
        idx = self.mnt[macro_name][0]
        parameters = self.mnt[macro_name][1]
        arg_param = {}
        for i in range(len(parameters)):
            arg_param[parameters[i]] = arguments[i]

        while idx < len(self.mdt) and 'MEND' not in self.mdt[idx]:
            tokens = self.mdt[idx].split()
            if tokens[0] in self.mnt:
                args = [word.replace(',', '') for word in tokens[1:]]
                self.utility(tokens[0], args)
            else:
                line = self.mdt[idx]
                if tokens[1] in parameters:
                    line = line.replace(tokens[1], arg_param[tokens[1]])
                self.intermediate_code.append(line)
            idx += 1

    def pass2(self, source_code):
        i = 0
        n = len(source_code)
        while i < n:
            line = source_code[i].strip()
            tokens = line.split()
            if 'MACRO' in line:
                while i < n and 'MEND' not in source_code[i].strip():
                    i += 1
            elif self.mnt.get(tokens[0]) != None:
                args = [word.replace(',', '') for word in tokens[1:]]
                self.utility(tokens[0], args)
            else:
                self.intermediate_code.append(line)
            i += 1


def main():
    input_code = [
        "LOAD J",
        "STORE M",
        "MACRO EST1",
        "LOAD e",
        "ADD d",
        "MEND",
        "MACRO EST ABC",
        "EST1",
        "STORE ABC",
        "MEND",
        "MACRO ADD7 P4, P5, P6",
        "LOAD P5",
        "EST 8",
        "SUB4 z",
        "STORE P4",
        "STORE P6",
        "MEND",
        "ADD7 C4, C5, C6",
        "END"
    ]

    obj = Macro(input_code)


if __name__ == '__main__':
    main()
