
import random
# Step 1. INITIALIZATION

f_x  = "(a + 2b + 3c + 4d) - 30"
coefficiants = [1,2,3,4]
print(("The objective function is (a + 2b + 3c + 4d) - 30"))
var= 4
n_o_c = 6
crossover_rate=0.25
mutation_rate=0.1
dict_of_chromo = {}
dict_of_obj_func = {}
dict_of_fitness = {}
dict_of_probability = {}
dict_of_cumilative_probability = {}
random_no_roulette=[]
dict_of_new_chromo={}

for c in range(n_o_c):
    dict_of_chromo[f'Chromosome [{c}]']=[]
    dict_of_new_chromo[f'Chromosome [{c}]']=[]
    dict_of_obj_func[f'F_obj[{c}]']= 0
    dict_of_fitness[c]=0
    dict_of_probability[c]=0
    dict_of_cumilative_probability[c]=0

    for v in range(var):
        dict_of_chromo[f'Chromosome [{c}]'].append(random.randint(0,30)) 
# print(dict_of_chromo)
for chromo in dict_of_chromo:
    print(f'{chromo} = {dict_of_chromo[chromo]}')


# Step 2. Evaluation
# We compute the objective function value for each chromosome produced in initialization step:

for c in range(n_o_c):
    result=0
    current_chromosome = dict_of_chromo[f'Chromosome [{c}]']
    # print(current_chromosome)
    i=0
    for var in current_chromosome:
        result = result + (coefficiants[i]*var)
        i+=1
    result = abs(result - 30)
    dict_of_obj_func[f'F_obj[{c}]']=result    


for of in dict_of_obj_func:
    print(f'{of} = {dict_of_obj_func[of]}')

# Step 3. Selection 

# 1. The fittest chromosomes have higher probability to be selected for the next 
# generation. To compute fitness probability we must compute the fitness of each 
# chromosome.

for c in range(n_o_c):
    temp = 1/(dict_of_obj_func[f'F_obj[{c}]']+1)
    dict_of_fitness[c] = round(temp,4)

total=0
for fit in dict_of_fitness:
    total += dict_of_fitness[fit]
    print(f'Fitness[{fit}] = {dict_of_fitness[fit]}')

total = round(total,4)
print(f"The total is {total}")

#The probability for each chromosomes is formulated by: P[i] = Fitness[i] / Total
for prob in dict_of_probability:
    temp = dict_of_fitness[prob]/total
    dict_of_probability[prob] = round(temp,4)
    
for p in dict_of_probability:
    print(f'P[{p}] = {dict_of_probability[p]}')

#The highest probability to be selected for next generation chromosomes. For the selection process we use roulette wheel, for that we should compute the cumulative probability values:
dict_of_cumilative_probability[0]=dict_of_probability[0]
for key,val in dict_of_probability.items():
    if key == 0:
        continue
    else:
        temp = dict_of_probability[key] + dict_of_cumilative_probability[key-1]
        dict_of_cumilative_probability[key] = round(temp,4)
for cp in dict_of_cumilative_probability:
    print(f'C[{cp}] = {dict_of_cumilative_probability[cp]}')


for i in range(n_o_c):
    random_no_roulette.append(round(random.random(), 3))

print(random_no_roulette)

def find_new(i):
    if random_no_roulette[i]>dict_of_cumilative_probability[i] and random_no_roulette[i]<dict_of_cumilative_probability[i+1]:
        # dict_of_new_chromo[f'Chromosome [{i}]'] = dict_of_chromo[f'Chromosome [{i+1}]']
        return (i+1)
    else:
        for k in range(n_o_c-2):
            if random_no_roulette[i]>dict_of_cumilative_probability[k] and random_no_roulette[i]<dict_of_cumilative_probability[k+1]:
                # dict_of_new_chromo[f'Chromosome [{i}]'] = dict_of_chromo[f'Chromosome [{k+1}]']
                 return (k+1)
        return (0)



for i in range(n_o_c):
    index= find_new(i)
    dict_of_new_chromo[f'Chromosome [{i}]'] = dict_of_chromo[f'Chromosome [{index}]']
    print(f'New_chromosome[{i}]=Chromosome [{index}]')

for chromo in dict_of_new_chromo:
    print(f'{chromo} = {dict_of_new_chromo[chromo]}')

#  Chromosomes selection is controlled using crossover_rate (ρc) parameters. 
flag=True
random_no_roulette=[]
while flag:
    for i in range(n_o_c):
        random_no_roulette.append(round(random.random(), 3))
    selected_parents=[]
    for r in range(n_o_c):
        if random_no_roulette[r]<crossover_rate:
            selected_parents.append(f'Chromosome [{r}]')
    if len(selected_parents) > 1:
        flag=False
print(random_no_roulette)
print(selected_parents)

# After chromosome selection, the next process is determining the position of the crossover 
# point. This is done by generating random numbers between 1 to (length of Chromosome – 1). 
# In this case, generated random numbers should be between 1 and 3. After we get the 
# crossover point, parents Chromosome will be cut at crossover point and its gens will be 
# interchanged.
selected_parents.append(selected_parents[0])
print(selected_parents)
for no in range(len(selected_parents)):
    crossover_point = random.randint(0,len(selected_parents)-1)
    new_chromo = dict_of_new_chromo[f'Chromosome [{no}]'][:crossover_point]+dict_of_new_chromo[f'Chromosome [{no+1}]'][crossover_point:]
    print(new_chromo)

    print(crossover_point)