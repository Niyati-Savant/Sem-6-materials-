import ast

class TACGenerator(ast.NodeVisitor):
    def __init__(self):
        self.temp_count = 0
        self.tac = []

    def generate_tac(self, expr):
        tree = ast.parse(expr, mode='eval')
        self.visit(tree)
        return self.tac

    def new_temp(self):
        temp = f"t{self.temp_count}"
        self.temp_count += 1
        return temp

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        temp = self.new_temp()
        self.tac.append((node.op.__class__.__name__, left, right, temp))
        return temp

    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)
        temp = self.new_temp()
        self.tac.append((node.op.__class__.__name__, operand, None, temp))
        return temp

    def visit_Num(self, node):
        return str(node.n)

# Example usage
# expression = "5 + 6 * 7 / 2 + 3 - 10"
expression ="1 * 2 - 3 * 4 / 5 "

tac_generator = TACGenerator()
tac = tac_generator.generate_tac(expression)

for instruction in tac:
    print(instruction)


def print_tac(tac):
    for instruction in tac:
        if instruction[2] is not None:
            # print(f"{instruction[3]} ={instruction[1]} {instruction[0]} {instruction[2]}")
            if instruction[0]=='Mult':
                print(f"{instruction[3]} ={instruction[1]} * {instruction[2]}")
            elif instruction[0]=='Add':
                print(f"{instruction[3]} ={instruction[1]} + {instruction[2]}")
            elif instruction[0]=='Sub':
                print(f"{instruction[3]} ={instruction[1]} - {instruction[2]}")
            elif instruction[0]=='Div':
                print(f"{instruction[3]} ={instruction[1]} / {instruction[2]}")
        else:
            print(f"{instruction[3]} = - {instruction[1]}")

print_tac(tac)
