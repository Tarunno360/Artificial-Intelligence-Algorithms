def pacman_game(c):
    outcomes=[3,6,2,3,7,1,2,0] 
    #main alpha beta algo ---------------
    def alpha_beta_pruning(distance,index_number,max_player_value,alpha,beta,dark_magic_var): #adding some extra perks in alpha beta pruning
        if distance==3:
            return outcomes[index_number]
        if max_player_value: #aplha part
            highest_evaluation=-float('inf')
            for i in range(2):
                current_evaluation=alpha_beta_pruning(distance+1,index_number*2+i,dark_magic_var or not max_player_value,alpha,beta,dark_magic_var)
                highest_evaluation=max(highest_evaluation,current_evaluation)
                alpha=max(alpha,current_evaluation)
                if beta <=alpha: #pruning
                    break
            return highest_evaluation #returning highest utility
        else: #beta part
            lowest_evalutation=float('inf')
            for i in range(2):
                current_evaluation=alpha_beta_pruning(distance+1,index_number*2 +i,dark_magic_var or not max_player_value,alpha,beta,dark_magic_var)
                lowest_evalutation=min(lowest_evalutation,current_evaluation)
                beta=min(beta,current_evaluation)
                if beta <=alpha: #pruning
                    break
            return lowest_evalutation #retuning lowest utliity 
    not_using_dark_magic=alpha_beta_pruning(0,0,True,-float('inf'),float('inf'),False) #just the points
    using_dark_magic=alpha_beta_pruning(0,0,True,-float('inf'),float('inf'),True)-c #reducing points
    if using_dark_magic>not_using_dark_magic: #checking 
        for_left_move=alpha_beta_pruning(1,0,True,-float('inf'),float('inf'),True)
        for_right_move=alpha_beta_pruning(1,1,True,-float('inf'),float('inf'),True)
        if for_left_move>=for_right_move: #for better move
            moves='left'
        else:
            moves='right'
        return f"The new minmax value is {using_dark_magic}. Pacman goes {moves} and uses dark magic." #answer for using magic
    else:
        for_left_move=alpha_beta_pruning(1,0,False,-float('inf'),float('inf'),False)
        for_right_move=alpha_beta_pruning(1,1,False,-float('inf'),float('inf'),False)
        if for_left_move>=for_right_move:
            moves='left'
        else:
            moves='right'
        return f"The new minmax value is {not_using_dark_magic}. Pacman goes {moves} and does not use dark magic." #answer for not using magic
#-------------DRIVER CODE-----------------------
input_details=int(input('Please enter a number:')) #input of number asked in the question
print(pacman_game(input_details))  