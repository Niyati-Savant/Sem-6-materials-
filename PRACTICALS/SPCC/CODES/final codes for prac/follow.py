# Grammar and FIRST sets provided
grammar = {
    "E": ["TA"],
    "A": ["+TA", "@"],
    "T": ["FB"],
    "B": ["*FB", "@"],
    "F": ["(E)", "i"]
}

first = {
    'E': ['(', 'i'],
    'A': ['+', '@'],
    'T': ['(', 'i'],
    'B': ['*', '@'],
    'F': ['(', 'i']
}

non_terminals = ['E', 'A', 'T', 'B', 'F']
terminals = ['(', ')', 'i','+', '*','$']
start_symbol = non_terminals[0]


# grammar = {
#     "S": ["(L)","a"],
#     "L": [ "SX"],
#     "X" : [")SX","@"]
# }

# first = {
#     "S": ["(","a"],
#     "L": [ "(","a"],
#     "X" : [")","e"]
# }

# Non-terminals, terminals, and start symbol
# non_terminals = ['S', 'L', 'X']
# terminals = ['(', ')', 'a', '$']
# start_symbol = non_terminals[0]

# Convert FIRST sets from lists to sets
first_sets = {key: set(value) for key, value in first.items()}
print(first_sets)

# Function to compute FOLLOW sets
def compute_follow(nt, grammar, firsts, follows, visited):
    if nt in visited:
        return follows[nt]
    visited.add(nt)

    if nt == start_symbol:
        follows[nt].add('$')

    for lhs, productions in grammar.items():
        for prod in productions:
            if nt in prod:
                nt_index = prod.index(nt)
                if nt_index + 1 < len(prod):
                    next_symbol = prod[nt_index + 1]
                    if next_symbol in non_terminals:
                        follows[nt].update(firsts[next_symbol] - {'@'})
                    else:
                        follows[nt].add(next_symbol)

                    if '@' in firsts.get(next_symbol, set()):
                        follows[nt].update(compute_follow(lhs, grammar, firsts, follows, visited))
                else:
                    follows[nt].update(compute_follow(lhs, grammar, firsts, follows, visited))
    return follows[nt]

# Initialize FOLLOW sets
follows = {nt: set() for nt in non_terminals}

# Compute FOLLOW sets for each non-terminal
for nt in non_terminals:
    compute_follow(nt, grammar, first_sets, follows, set())

# Print the FOLLOW sets
# for nt in non_terminals:
#     print(f"Follow({nt}): {follows[nt]}")
print("{: ^20}{: ^20}".format('Non Terminals','Follow'))
for non_terminal in non_terminals:
    print("{: ^20}{: ^20}".format(non_terminal,str(follows[non_terminal])))