class generate_TAC:
   temp_count = 1


   @staticmethod
   def precedence(op):
       if op in ['+', '-']:
           return 1
       elif op in ['*', '/']:
           return 2
       return -1


   @staticmethod
   def apply_op(op, a, b):
       result = "t" + str(generate_TAC.temp_count)
       generate_TAC.temp_count += 1
       print(f"{result} = {a} {op} {b}")
       return result


   @staticmethod
   def infix_to_tac(exp):
       operators = []
       values = []


       i = 0
       while i < len(exp):
           c = exp[i]
           if c == ' ':
               i += 1
               continue


           if c.isalnum():
               sbuf = ''
               while i < len(exp) and (exp[i].isalnum() or exp[i] == '_'):
                   sbuf += exp[i]
                   i += 1
               values.append(sbuf)
               i -= 1
           elif c == '(':
               operators.append(c)
           elif c == ')':
               while operators and operators[-1] != '(':
                   val2 = values.pop()
                   val1 = values.pop()
                   op = operators.pop()
                   values.append(generate_TAC.apply_op(op, val1, val2))
               operators.pop()
           else:
               while operators and generate_TAC.precedence(operators[-1]) >= generate_TAC.precedence(c):
                   val2 = values.pop()
                   val1 = values.pop()
                   op = operators.pop()
                   values.append(generate_TAC.apply_op(op, val1, val2))
               operators.append(c)
           i += 1


       while operators:
           val2 = values.pop()
           val1 = values.pop()
           op = operators.pop()
           values.append(generate_TAC.apply_op(op, val1, val2))


       print("Result =", values.pop())


   @staticmethod
   def main():
       exp = input("Enter an infix expression: ")
       print("Infix Expression:", exp)
       print("Generated Three Address Code:")
       generate_TAC.infix_to_tac(exp)




if __name__ == "__main__":
   generate_TAC.main()
