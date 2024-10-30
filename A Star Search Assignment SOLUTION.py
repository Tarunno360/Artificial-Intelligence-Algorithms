x1=open('file','r')
x2=x1.readlines()    
graph={}
dic_hf={}
for i in x2:
    x3=i.split()
    dic_hf[x3[0]]=x3[1]
    new=[]
    for j in range (2,len(x3),2):
        xx=[x3[j],x3[j+1]]
        new.append(xx)
        graph[x3[0]]=new
#print(graph)
#'------------------------------------------------')
def sorting_algo(l1):
    for i in range (len(l1)):
        min_i=i
        for j in range (i+1,len(l1)):
            if int(l1[min_i][1])>int(l1[j][1]):
                min_i=j
        l1[i],l1[min_i]=l1[min_i],l1[i]    
    return l1
#print(sorting_algo([['A',3],['B',2],['C',4]]))
#-----------------------------------------
star_node=input('Starting destination:')
end_node=input('Ending destiantion or Goal node:')
def A_star_algo(star_node,end_node,graph,dic_hf):
    search_queue=[]
    visited_nodes=[]
    search_queue.append([star_node,dic_hf[star_node]])
    parent={}
    while search_queue:
        sorting_algo(search_queue)
        lowest_f=search_queue.pop(0) #[arad,366]
        visited_nodes.append(lowest_f[0]) #For visiting a node 
        #print(lowest_f,'########')
        if lowest_f[0]==end_node: #get the goal node
            path_list=[end_node]
            current_node=lowest_f[0]
            while current_node!=star_node:
                path_list.append(parent[current_node])
                current_node=parent[current_node]
            path_list.reverse()
            return (lowest_f[1],path_list)
        else:
            child_nodes=graph[lowest_f[0]]
            parent_current_g=int(lowest_f[1])-int(dic_hf[lowest_f[0]])
            for i in range (len(child_nodes)):
                if child_nodes[i][0] not in visited_nodes:
                    parent[child_nodes[i][0]]=lowest_f[0]
                    #print(parent)
                    f1=int(dic_hf[child_nodes[i][0]])+parent_current_g+int(child_nodes[i][1]) 
                    new=[child_nodes[i][0],f1]
                    #print(new,'-----------')
                    search_queue.append(new)
    return []
distance,path=A_star_algo(star_node,end_node,graph,dic_hf)
x_output=open('file.txt','w')
#------------------------------------
if len(path)>0:
    for i in range (len(path)):
        x_output.write(f'{path[i]} -->')
    x_output.write('\n')    
    x_output.write(f'Total Distance:{distance}')
else:
    x_output.write('No Path Found')
