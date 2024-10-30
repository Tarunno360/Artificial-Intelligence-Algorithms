import random
#-------creating random population from part1-----------------
def population_function(each_choromsome_size,max_size_population):
    course_combination=[]
    for i in range(max_size_population):
        chr=''
        for j in range(each_choromsome_size):
            chr+=random.choice('01')
        course_combination.append(chr)
    return course_combination
#------------- crossover using two pointer--------------
def crossover_parents(first_parent,second_parent):
    size_of_chr=len(first_parent)
    pointer_one= random.randint(0,size_of_chr-2)
    pointer_two=random.randint(pointer_one+1,size_of_chr-1)
    print(f'Random first index:{pointer_one}\nRandom second index :{pointer_two}')
    str1=first_parent[:pointer_one]+second_parent[pointer_one:pointer_two]+first_parent[pointer_two:]
    str2=second_parent[:pointer_one]+first_parent[pointer_one:pointer_two]+second_parent[pointer_two:]
    return str1,str2
#------------ selecting parents randomly--------------
def selecting_parents_function(course):
    return random.sample(course,2)
#------------DRIVER CODE---------------------
each_choromosome_size=9
max_size_popualtion=10
creating_population=population_function(each_choromosome_size,max_size_popualtion)
first_parent,second_parent=selecting_parents_function(creating_population)
print(f'First Parent :{first_parent}\nSecond parent:{second_parent}')
cross_result=crossover_parents(first_parent,second_parent)
print(f'First offstpring :{cross_result[0]}\nSecond offspring:{cross_result[1]}')
#------------------END-----------------------


