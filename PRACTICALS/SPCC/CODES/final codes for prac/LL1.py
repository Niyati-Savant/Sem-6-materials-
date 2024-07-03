# first_set={'E':['(','a'],'X':['@','+'],'T':['(','a'],'Y':['*','@'],'F':['(','a']}
# follow_set={'E':[')','$'],'X':[')','$'],'T':[')','$','+'],'Y':[')','$','+'],'F':[')','$','+','*']}
# P_D={'E':['TX'],'X':['+TX','@'],'T':['FY'],'Y':['*FY','@'],'F':['a','(E)']}
# NT=['E','X','T','Y','F']
# T=['+','*','a','(',')','$']

first_set={'S':['1','@'],'A':['1','0'],'B':['0'],'C':['1']}
follow_set={'S':['$'],'A':['0','1'],'B':['$'],'C':['0','1']}
P_D={'S':['1AB','@'],'A':['1AC','0C'],'B':['0S'],'C':['1']}
NT=['S','A','B','C']
T=['1','0','$']
table_contents={}
for nt in NT:
    table_contents[nt]={}

for nt in NT:
    rule_list=P_D[nt]
    current_first = first_set[nt]
    for term in current_first:
        if len(rule_list)>1 and '@' not in rule_list:
            for prod in rule_list:
                x = prod[0]
                
                if x==term:
                    table_contents[nt][x]=f'{nt}->{prod}'
                    continue
        else:
            if term != '@':
                rule=P_D[nt][0]
                # print(f"{term}:{nt}->{rule}")
                table_contents[nt][term]=f'{nt}->{rule}'
            else:
                current_follow = follow_set[nt]
                for term in current_follow:
                    rule=P_D[nt][1]
                    # print(f"{term}:{nt}->{rule}")
                    table_contents[nt][term]=f'{nt}->{rule}'

print(table_contents)
print('Term \t',end='')
print("\t".join(T))
for nt in NT:
    print(f"{nt}\t", end='')
    corres_content = table_contents[nt]
    corres_keys=corres_content.keys()
    for term in T:
        if term in corres_keys:
            print(corres_content[term], end='')
        else:
            print(f"--", end='')
        print("\t", end='')
    print("\n")