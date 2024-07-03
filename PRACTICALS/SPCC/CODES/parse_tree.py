class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def generate_parse_tree(expression):
    # Break the expression string into a list of tokens
    tokens = expression.split()

    # Create a stack to store the nodes of the parse tree
    stack = []

    # Iterate over the tokens
    for token in tokens:
        # If the token is a left parenthesis, create a new node and push it onto the stack
        if token == '(':
            stack.append(Node(token))

        # If the token is an operator, create a new node with the operator as its value and push it onto the stack
        elif token in ['+', '-', '*', '/']:
            node = Node(token)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)

        # If the token is a number, create a new node with the number as its value and push it onto the stack
        else:
            stack.append(Node(int(token)))

    # The parse tree is the root node of the stack
    return stack.pop()

# Example usage:
expression = "(3 + 4) * 5"
parse_tree = generate_parse_tree(expression)

# Print the parse tree
print(parse_tree)