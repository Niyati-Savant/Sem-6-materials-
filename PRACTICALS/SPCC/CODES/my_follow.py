P_D = {'S':['iEtSX','a'],
       'X':['eS','@'],
       'E':['b']}
first_set = {'S':['i','a'],
             'X':['e','@'],
             'E':['b']}
NT=['S','X','E']

follow_set={}
for x in NT:
    follow_set[x] = []

def deal_with_epsilon(x):
    pass

for c_nt in NT:
    for x in P_D:
        rules=P_D[x]
        for rule in rules:
            rule_len = len(rule)

            if c_nt in rule:
                pos  = rule.rfind(c_nt)+1
                if pos < rule_len:#nt is not at last position
                    nt_follower = rule[pos]
                    print(nt_follower)
                    if nt_follower in NT:
                        k = first_set[nt_follower]
                        print(f"k is {k}")
                        for x in k:
                            if x != '@':
                                follow_set.append(x)
                            else:
                                k = deal_with_epsilon()
                        # print(first_set[nt_follower])
                    else: #terminal goes directly 
                        follow_set.append(nt_follower)
    print(follow_set)
               