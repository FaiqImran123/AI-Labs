from priority_queue_one import *
from copy import *
def iterative_depending_search(initial_state, goal_state):
    threshold =calculateHeuristic(initial_state, goal_state)
    while True:
        result =depth_limiting_search(initial_state, goal_state, threshold)
        if result=="FOUND":
            return "Solution Found"
        if result=="NO_SOLUTION":
            return "No Solution Found"
        threshold =result


def depth_limiting_search(state, goal_state, threshold):
    obj =Priority_Queue()
    obj.enqueue(calculateHeuristic(state, goal_state), state, 0)
    visited =[]
    while obj.is_empty()!=True:
        new_obj =obj.dequeue()
        d =new_obj.depth
        visited.append(new_obj.obj)
        

        if new_obj.obj==goal_state:
            return "FOUND"
        if new_obj.priority>threshold:
            return new_obj.priority
        ind=index_of(new_obj.obj, 0)
        i =ind[0]
        j =ind[1]
        for pos in [(0,1),(0,-1),(1,0),(-1,0)]:
            li =deepcopy(new_obj.obj)
            
           
            
        
        
        
            new_pos =(i+pos[0], j + pos[1])
        
            if 0<=new_pos[0]<=2 and 0<=new_pos[1]<=2:
                li[i][j] =li[new_pos[0]][new_pos[1]]
                li[new_pos[0]][new_pos[1]] =0
         
                if li not in visited:
                
                    new_prio =calculateHeuristic(li, goal_state)+d
                   
                    v =obj.search(li)
                    if v!=False:
                        if new_prio<v:
                            obj.update(new_prio, li, d)
                              
                    else:
                        
                        obj.enqueue(new_prio, li, d) 
        
    return "NO_SOLUTION"
def calculateHeuristic(current_state, goal_state):
    #implementing using manhattan heuristic
    heuristic =0
    for i in range(3):
        for j in range(3):
            if goal_state[i][j]!=0:
                v =index_of(current_state, goal_state[i][j])
                
                a =v[0]
                b =v[1]
                heuristic +=(abs(a-i) + abs(b-j))
        
    return heuristic
def index_of(li, x):
    for i in range(3):
        for j in range(3):
            if li[i][j]==x:
               
                return (i, j)
            
def main():
    initial_state =[[2,8,1],
                    [4,6,3],
                    [0, 5,7]]
    goal_state =[[1,2,3],
                 [4,5,6],
                 [7,8,0]]
    print(iterative_depending_search(initial_state, goal_state))
    
main()