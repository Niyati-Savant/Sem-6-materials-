# CODE FOR LEFT RECURSION REMOVAL
list_of_alt_NT=['W','Y','Z','P','Q']
i=0
P_D= {'E':['E+T','T'],'T':['T*F','F'],'F':['(E)','c']}
LOT=['+','*','(',')','c']
LONT=['E','T','F']

# P_D= {'A':['ABd','Aa','a'],'B':['Be','b']}
# LOT=['a','b','e']
# LONT=['A','B']

P_D= {'S':['(L)','x'],'L':['L,S','S']}
LOT=[')','(','x',',']
LONT=['L','S']

# P_D= {'S':['A'],'A':['Ad','Ae','aB','ac'],'B':['bBc','f']}
# LOT=[')','(','x',',']
# LONT=['A','S','B']

# P_D= {'S':['A'],'A':['aB','ac','Ad','Ae'],'B':['bBc','f']}
# LOT=[')','(','x',',']
# LONT=['A','S','B']

# P_D= {'A':['Ba','Aa','c'],'B':['Bb','Ab','d']}
# LOT=['a','b','c','d']
# LONT=['A','B']

# P_D= {'X':['XSb','Sa','b'],'S':['Sb','Xa','a'],'B':['b','ab']}
# LOT=['a','b','c','d']
# LONT=['X','S','B']

new_rules={}

def remove_indi(nt1,nt2,P_D):
   new_P_D={}
   new_P_D[nt1]=[]
   new_P_D[nt2]=[]

   for rule in P_D[nt1]:
    if rule[0] == nt2:
      temp=rule[1:]
      for x in P_D[nt2]:
        new_rule=x+temp

        new_P_D[nt1].append(new_rule)
        # break
    else:
      new_P_D[nt1].append(rule)
   print(f"for {nt1} the rules are {new_P_D[nt1]}")

   for rule in P_D[nt2]:
    if rule[0] == nt1:
      temp=rule[1:]
      for x in P_D[nt1]:
        new_rule=x+temp
        new_P_D[nt2].append(new_rule)
        # break
    else:
      new_P_D[nt2].append(rule)
   print(f"for {nt2} the rules are {new_P_D[nt2]}")     
   return(new_P_D)   
  
         
def recursion_remove(nt,i):
    loa=[]
    lob=[]
    prod = P_D[nt]
    # print(prod)
    for rule in prod:
      # print(rule)
      if rule[0]==nt:
        alpha=rule[1:]  
        # print(alpha)        
        loa.append(alpha)
      else:
        lob.append(rule)

    print(f"Alphas for {nt} are {loa}")
    print(f"Betas for {nt} are {lob}")

    new_term = list_of_alt_NT[i]
    new_rules={nt:[],new_term:[]}

    for b in lob:
        new_rule = b + new_term
        new_rules[nt].append(new_rule)

    for a in loa:
        new_rule = a +new_term
        new_rules[new_term].append(new_rule)

    new_rules[new_term].append('@')
    return new_rules

is_indirec = input("Enter y if indirect present: ")
# is_indirec ='y'
if is_indirec=='y':
   nt1 = input("Enter NT1: ")
   nt2 = input("Enter NT2: ")
   remove_indi(nt1,nt2,P_D)
   new_P_D=remove_indi(nt1,nt2,P_D)

   for nt in LONT:
      if nt not in new_P_D:
         new_P_D[nt] = P_D[nt]

   P_D=new_P_D

print("The following productions are there")
print(P_D)
for nt in LONT:
    rec_flag = False
    rules = P_D[nt]
    for k in rules:
      if k[0]==nt:
              rec_flag=True
              break;
    
    if rec_flag==True:   
      print('Recursion present in ' + nt)
      print(recursion_remove(nt,i))
      i+=1;      
    else:
      print('Recursion not present '+nt)
      print(P_D[nt])
   
       