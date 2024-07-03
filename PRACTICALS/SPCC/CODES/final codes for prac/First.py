import sys
sys.setrecursionlimit(60)
def first(string):
    first_ = set()
    if string in non_terminals:
        alternatives = productions_dict[string]

        for alternative in alternatives:
            first_2 = first(alternative)
            first_ = first_ |first_2

    elif string in terminals:
        first_ = {string}

    elif string=='' or string=='@':
        first_ = {'@'}

    else:
        first_2 = first(string[0])
        if '@' in first_2:
            i = 1
            while '@' in first_2:
                #print("inside while")

                first_ = first_ | first_2 - {'@'}
                #print('string[i:]=', string[i:])
                if string[i:] in terminals:
                    first_ = first_ | {string[i:]}
                    break
                elif string[i:] == '':
                    first_ = first_ | {'@'}
                    break
                first_2 = first(string[i:])
                first_ = first_ | first_2 - {'@'}
                i += 1
        else:
            first_ = first_ | first_2


    #print("returning for first({})".format(string),first_)
    return  first_


productions_dict = {'E':['TX'],
                    'X':['+TX','@'],
                    'T':['FY'],
                    'Y':['*FY','@'],
                    'F':['a','(E)']}
no_of_terminals=5
terminals = ['+','*','a','(',')']
no_of_non_terminals=5
non_terminals = ['E','X','T','Y','F']
starting_symbol = 'E'

# productions_dict = {'S':['AaB','Bb'],'A':['bA','@'],'B':['cB','@']}
# no_of_terminals=3
# terminals = ['a','b','c']
# no_of_non_terminals=3
# non_terminals = ['S','A','B']
# starting_symbol = 'S'

print(productions_dict)


FIRST = {}

for non_terminal in non_terminals:
    FIRST[non_terminal] = set()

for non_terminal in non_terminals:
    FIRST[non_terminal] = FIRST[non_terminal] | first(non_terminal)

print("{: ^20}{: ^20}".format('Non Terminals','First'))
for non_terminal in non_terminals:
    print("{: ^20}{: ^20}".format(non_terminal,str(FIRST[non_terminal])))