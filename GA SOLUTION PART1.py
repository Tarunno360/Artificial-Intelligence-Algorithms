#------------Input-----------------
import random
x1= open('InputFile.txt','r')
x2= x1.readline()
x3=x2.split(' ')
course_number=int(x3[0])
time_slots=int(x3[1])
each_chromosome_size=time_slots*course_number
#print(each_chromosome_size)
courses=x1.readlines()
max_size_population=10
#---------------------------xx-----------------------
def population_function(each_choromsome_size,max_size_population):
    course_combination=[]
    for i in range(max_size_population):
        chr=''
        for j in range(each_choromsome_size):
            chr+=random.choice('01')
        course_combination.append(chr)
    return course_combination
#-----------------------------xx--------------------
#print(population_function(each_chromosome_size,max_size_population))
def fitness_function(course,course_number,time_slots):
    p_over=0
    p_con=0
    #pentaly_over
    for i in range (time_slots):
        each_time_slot= course[i*course_number:(i*course_number)+time_slots]
        counting=each_time_slot.count('1')
        if int(counting)> 1 :
            p_over+=(counting-1)
    #penalty_con
    for i in range(course_number):
        current_pen=0
        for j in range(time_slots):
            if course[j*course_number+i]=='1':
                current_pen+=1
        if current_pen!=1:
            p_con+= abs(current_pen-1)
    fitness_utility=-(p_con+p_over)
    return fitness_utility
#---------------------------x----------------------
def selecting_parents_function(course, utility_values):
    min_utility_fitness = min(utility_values)
    temp_fitness = []
    for i in utility_values:
        new_fitness = abs(i - min_utility_fitness) + 1
        temp_fitness.append(new_fitness)
    random_parents = random.choices(course, weights=temp_fitness, k=2)
    return random_parents
#-------------------x-------------------
def crossover(first_parent,second_parent):
    crossover_point=(course_number* time_slots)//2
    str_1=first_parent[:crossover_point]+second_parent[crossover_point:]
    str2=second_parent[:crossover_point]+first_parent[crossover_point:]
    return str_1,str2
#---------------------------x------------------------------
def mutate_function(per_course,mutation_rate):
    mutated_course=[]
    for i in per_course:
        if random.random()>mutation_rate:
            mutated_course.append(i)
        else:
            mutated_course.append(str(1-int(i)))
    return ''.join(mutated_course)
#--------------------------x_--------------------------
def genetic_algo_course(course_number,timeslot,courses):
    size_chr=course_number*timeslot
    max_size=10
    all_courses=population_function(size_chr,max_size)
    max_value=100
    mutation_rate=0.0001
    for i in range (max_value):
        fitness_unitily_values=[]
        for j in all_courses:
            temp= fitness_function(j,course_number,timeslot)
            fitness_unitily_values.append(temp)
        max_utility=max(fitness_unitily_values)
        max_uti_chr= all_courses[fitness_unitily_values.index(max_utility)]
        if max_utility==0:
            break
        #-=---------- CROSSOVER FUNCTION------------
        temp_course=[]
        for k in range(max_size//2):
            first_parent, second_parent=selecting_parents_function(all_courses,fitness_unitily_values)
            first_cut,second_cut=crossover(first_parent,second_parent)
            temp_course.extend([first_cut,second_cut])
        #--------------MUTATION--------------------
        course=[]
        for h in temp_course:
            mutate=mutate_function(h,mutation_rate)
            course.append(mutate)
        resulting_fitness=fitness_function(max_uti_chr,course_number,timeslot)
        if max_uti_chr !=None and resulting_fitness!=None:
            return max_uti_chr, resulting_fitness
#---------------------END--------------------
#----------------_--DRIVER CODE------------------
fittest_choromosome,fittest_utility=genetic_algo_course(course_number,time_slots,courses)
print(f'{fittest_choromosome} \n{fittest_utility}')
#--------------------xxxx---------------------