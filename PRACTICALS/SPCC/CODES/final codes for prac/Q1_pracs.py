import re
# prog_file = open("prog.txt", "r")
# file_content = prog_file.read()
# print(file_content)
with open("prog.txt", "r") as file:
    prog = file.read()
print(prog)

key_word = ['for', 'in', 'range','if','else','print']
operator =['+','-','/','*','%','==','=','!=','>','<','^']
seperator = ['\n','\t']
identifier = re.compile(r'^[a-zA-Z]\w*$')
digit = re.compile(r'^\d*[.,]?\d*$')

for x in prog.split():
    # if not x.strip():
    #     continue
    if x in key_word:
        print(f"{x} is keyword")
    elif x in operator:
        print(f"{x} is operator")
    elif x in seperator:
        print(f"{x} is seperator")
    elif re.match(identifier,x):
        print(f"{x} is identifier")
    elif re.match(digit,x):
        print(f"{x} is digit")
