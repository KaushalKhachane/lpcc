def process_macro_definition(lines):
   MNT = []  # Macro Name Table
   MDT = []  # Macro Definition Table
   ALA = {}  # Argument List Array


   macro_name = None
   macro_args = []
   macro_started = False
   macro_start_index = None


   for line_index, line in enumerate(lines):
       tokens = line.strip().split()
       if tokens and tokens[0] == 'MACRO':
           macro_name = tokens[1]
           MNT.append([macro_name, 0, len(MDT) + 1, None])  # Add starting index as None initially
           if len(tokens) > 2:
               macro_args = [arg.rstrip(',') for arg in tokens[2:]]  # Remove trailing commas
               for i, arg in enumerate(macro_args, 1):
                   ALA[arg] = f"#{i}"
               MNT[-1][1] = len(macro_args)
           macro_started = True
           macro_start_index = line_index
           continue
       elif tokens and tokens[0] == 'MEND':
           MDT.append(line.strip())
           MNT[-1][3] = len(MDT) - 1  # Update the starting index in MNT
           macro_started = False
           continue


       if macro_started:
           formatted_line = []
           for token in tokens:
               if token in ALA:
                   token = ALA[token]  # Replace macro arguments with positional parameters
               formatted_line.append(token)
           MDT.append(' '.join(formatted_line))
       else:
           print(line.strip())  # Print intermediate code


   return MNT, MDT, ALA




def expand_nested_macros(MDT, MNT):
   for i, line in enumerate(MDT):
       tokens = line.strip().split()
       if tokens[0] in [entry[0] for entry in MNT]:  # Check if it's a macro call
           macro_index = [entry[0] for entry in MNT].index(tokens[0])
           macro_start_index = MNT[macro_index][2]
           macro_end_index = MNT[macro_index][3]
           if macro_end_index is None:
               print("Error: MEND not found for nested macro")
               continue
           macro_definition = MDT[macro_start_index-1:macro_end_index]
           MDT = MDT[:i] + macro_definition + MDT[i+1:]
   return MDT


def replace_parameters(MDT, ALA):
   for i, line in enumerate(MDT):
       tokens = line.strip().split()
       for j, token in enumerate(tokens):
           if token in ALA:
               tokens[j] = ALA[token]
       MDT[i] = ' '.join(tokens)
   return MDT


def print_mnt(MNT):
   print("\nMNT:")
   print("(Name of macro, No. of parameters, Start index in MDT)")
   for entry in MNT:
       print(entry[:3])


def print_mdt(MDT):
   print("\nMDT:")
   for i, line in enumerate(MDT, start=1):
       print(f"{i}) {line}")


def print_ala(ALA):
   print("\nALA:")
   for key, value in ALA.items():
       print(f"{key}: {value}")


def main():
   with open("input.txt", "r") as file:
       lines = file.readlines()


   MNT, MDT, ALA = process_macro_definition(lines)
   MDT = expand_nested_macros(MDT, MNT)
   MDT = replace_parameters(MDT, ALA)
   print("\n--------------------------------------------------------------------")
   print_mnt(MNT)
   print("\n--------------------------------------------------------------------")
   print_mdt(MDT)
   print("\n--------------------------------------------------------------------")
   # print_ala(ALA)


if __name__ == "__main__":
   main()
