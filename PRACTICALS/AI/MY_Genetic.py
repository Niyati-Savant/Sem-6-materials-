import random
# Step 1. INITIALIZATION
f_x  = "(a + 2b + 3c + 4d) - 30"
coefficiants = [1,2,3,4]
print(("The objective function is (a + 2b + 3c + 4d) - 30"))
var= 4
n_o_c = 6
dict_of_chromo = {}
for i in range(1,n_o_c+1):
    list_of_chromo = []
    for nos in range(var):
        list_of_chromo.append(random.randint(0,30))
    dict_of_chromo[f"chromosome[ {i} ]"] = list_of_chromo
print(dict_of_chromo)


#Step 2. Evaluation
#We compute the objective function value for each chromosome produced in initialization step:

dict_of_obj = {}

for i in range(1,n_o_c+1):
    list_of_func_val = []
    current_chromo = dict_of_chromo[f"chromosome[ {i} ]"]
    func = 0
    k=0
    for nos in coefficiants:
        func = func + (nos*current_chromo[k])
        k+=1
    func = func -30
    dict_of_obj[f'F_obj[{i}]'] = abs(func)
print(dict_of_obj)



