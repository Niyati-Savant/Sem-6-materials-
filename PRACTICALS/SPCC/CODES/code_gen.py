op1, op2, op3, op4 = "", "", "", ""
print("Niyati Savant")
k = int(input("Enter no of lines"))
print("Enter operation and operands (e.g., + o1 o2): ")
loaded_var= ['a','b','c']
i=0
while k:
    TAC = input().split()
    k -=1
    op1=TAC[0]
    op2=TAC[1]
    op3=TAC[2]

    if op1 == "+" :
        if op2 not in loaded_var:
            print(f"MOV {op2},R{i}")
        print(f"ADD R{i}, R{i+1}")

    elif op1 == "-":
        print(f"MOV {op2},R{i+1}")
        print(f"SUB {op3},R{i+1}")

    elif op1 == "*":
        print(f"MOV {op2},R{i}")
        print(f"MUL R{i}, R{i+1}")

    elif op1 == "/":
        print(f"MOV {op2},R{i}")
        print(f"DIV R{i}, R{i+1}")
    elif op1 == "=":
        print(f"MOV {op2}, {op3}")


