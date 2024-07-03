def optimize_code(code):
    expressions = {}
    optimized_code = []
    line_replacements = {}

    for line in code:
        # Assume lines are in the form "tX = operation"
        # print(line)
        left_side, expression = line.split(' = ')
        if expression in expressions:
            # If expression has been computed before, replace the current line with a reference to the first computation
            line_replacements[left_side] = expressions[expression]
            # print(line_replacements[left_side])
        else:
            # Store new computation and keep the line in the optimized code
            expressions[expression] = left_side
            # print(expressions[expression])
            optimized_code.append(line)
        # print(expressions)
            print(line_replacements)
            
    print(optimized_code)
    # Replace all occurrences of temp variables that have redundant computations with their first computed counterparts
    final_code = []
    for line in optimized_code:
        left_side, expression = line.split(' = ')
        for old, new in line_replacements.items():
            expression = expression.replace(old, new)
        final_code.append(f"{left_side} = {expression}")

    return final_code

# Example input
input_code = [
    "t1 = -c",
    "t2 = a + b",
    "t3 = a + b",
    "t4 = a + b",
    "t5 = d + e",
    "t6 = a + b",
    "t7 = -c",
    "t8 = d + e",
    "t9 = 4 * t4"
]

# Perform optimization
optimized_code = optimize_code(input_code)

# Output optimized code
for line in optimized_code:
    print(line)
