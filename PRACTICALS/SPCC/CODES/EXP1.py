import re

prog_file = open("prog.txt", mode='r')
file_content = prog_file.read()


print("NIYATI's CODE FOR LEXICAL ANALYZER")
print("The program is -- ")
print(file_content)

keyword_list = ['for', 'in', 'range', 'if', 'else', 'int', 'float', 'print', 'open']
identifier_list = re.compile(r'^[a-zA-Z]\w*$')
operator_list = ['+', '-', '*', '/', '=', '==', '!=', '%', '^', '!']
constant_list = re.compile(r"^\d*[.,]?\d*$")
separator_list = [';', '\n', '\t']

op_key = []
op_iden = []
op_opera = []
op_const = []
op_sep = []

for x in file_content.split():
    if x.lower() in map(str.lower, keyword_list) and x.lower() not in op_key:
        op_key.append(x)
    elif x in operator_list and x not in op_opera:
        op_opera.append(x)
    elif x in separator_list and x not in op_sep:
        op_sep.append(x)
    elif re.match(identifier_list, x) and x not in op_iden:
        op_iden.append(x)
    elif re.match(constant_list, x) and x not in op_const:
        op_const.append(x)

print(f"The keywords are {op_key}")
print(f"The operators are {op_opera}")
print(f"The identifiers are {op_iden}")
print(f"The constants are {op_const}")
print(f"The separators are {op_sep}")
