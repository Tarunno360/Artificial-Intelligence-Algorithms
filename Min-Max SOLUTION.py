import random
#------------------creating a game tree----------------
class Node:
    def __init__(self,game_utility=None):
        self.game_utility=game_utility
        self.node_of_childrens=[]
    def terminal(self):
        return self.game_utility !=None
    def adding_childrens(self,child):
        self.node_of_childrens.append(child)
#-----------function of tree-------------
def building_game_tree(depth):
    if depth==0:
        return Node(random.choice([-1,1])) #assigning choices of scorpion or subzero random choice
    temp_node=Node()
    temp_node.adding_childrens(building_game_tree(depth-1))
    temp_node.adding_childrens(building_game_tree(depth-1))
    return temp_node
 #----------- main algo of alpha beda pruning-------
def alpha_beta_pruning_algo(node,depth,alpha,beta,maximizing_function):
    if depth==0 or node.terminal():
        return node.game_utility
    if maximizing_function:
        max_evaluation_function=float('-inf')
        for i in node.node_of_childrens:
            evalutaion_func=alpha_beta_pruning_algo(i,depth-1,alpha,beta,False)
            max_evaluation_function=max(max_evaluation_function,evalutaion_func)
            alpha=max(alpha,evalutaion_func)
            if alpha>=beta: #pruning
                break
        return max_evaluation_function
    else:
        min_evaluation_function=float('inf')
        for j in node.node_of_childrens:
            evalutaion_func=alpha_beta_pruning_algo(j,depth-1,alpha,beta,True)
            min_evaluation_function=min(min_evaluation_function,evalutaion_func)
            beta=min(beta,evalutaion_func)
            if alpha>=beta: #pruning
                break
        return min_evaluation_function
#------------- game for 3 round and winner function------------------
def conducting_game(first_attempt,round_played):
    if first_attempt==-1:
        print(f"First Attempt:Scoripion")
    else:
        print('First Attempt:Sub-zero')
    game_space=building_game_tree(5)
    scorpion_win=0
    subzero_win=0  
    print(f'Total Round Played:{round_played}')
    for k in range(round_played): #total round capped to 3
        value_winner=alpha_beta_pruning_algo(game_space,5,float('-inf'),float('inf'),first_attempt==0)
        if value_winner==-1:
            round_winner='Scorpion'
            scorpion_win+=1
        else:
            round_winner='Sub-zero'
            subzero_win+=1
        print(f"Round Number: {k+1} --- Round_winner:{round_winner}")
        if first_attempt==0:
            first_attempt=1
        else:
            first_attempt=0
    if scorpion_win>subzero_win:
        print('Game Winner:Scorpion')
    elif scorpion_win==subzero_win:
        print('Game Draw both win the same number of times')
    else:
        print('Game Winner:Sub-zero')
#-------------DRIVER CODE------------
round_played=int(input('Please enter how many rounds you want to play between Scorpion and Sub-zero:'))
conducting_game(random.choice([0,1]),round_played)