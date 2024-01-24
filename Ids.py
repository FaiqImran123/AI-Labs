from copy import *
from time import *
from priority_queue import *
def ids(initial_state, goal_state, visited,d,  depth):
   
  
    if initial_state==goal_state:
        print("Solution Found")
    
        return goal_state
    if d==depth:
        
        return None
   

 
        
    ind=index_empty(initial_state)
    i =ind[0]
    j =ind[1]
    current_state =Priority_Queue()
    for pos in [(1, 0), (-1, 0),(0,1), (0,-1)]:
      
        li =deepcopy(initial_state)
       
    
        new_pos =(i+pos[0], j + pos[1])
        
       
        if 0<=new_pos[0]<=2 and 0<=new_pos[1]<=2:
            
            li[i][j] =li[new_pos[0]][new_pos[1]]
            li[new_pos[0]][new_pos[1]] =0
           
           
            if li not in visited:
          
                
                current_state.enqueue(calculateHeuristic(li, goal_state), li)
   
  
    while current_state.is_empty()!=True:
    
        l =current_state.dequeue()
        
        
        if l not in visited:
            visited.append(l)
        
 

      

            v =ids(l, goal_state, visited, d+1, depth)
        
            if v!=None:
                return initial_state +v

          
                
def calculateHeuristic(current_state, goal_state):
    #implementing using manhattan heuridtic
    heuristic =0
    for i in range(3):
        for j in range(3):
            if current_state[i][j] !=0:
                v =index_of(current_state, goal_state[i][j])
                
                a =v[0]
                b =v[1]
                heuristic +=(abs(a-i) + abs(b-j))
            
    return heuristic
def index_of(li, x):
    for i in range(len(li)):
        for j in range(3):
            if li[i][j]==x:
               
                return (i, j)

def display_puzzle(li):
    count =0
    for i in li:
        if count==3:
            count=0
            print()
            print()

        print(i)
        count +=1

def index_empty(li):
    for i in range(len(li)):
        for j in range(3):
            if li[i][j]==0:
               
                return (i, j)

def main():

    initial_state =[[1,2,3],
                    [4,5,6],
                    [0,7,8]]
    goal_state =[[1,2,3],
                 [4,5,6],
                 [7,8,0]]
    visited =[initial_state]
    l =1
    v =ids(initial_state, goal_state, visited, 0, l)

    while v ==None:
      
        visited =[initial_state]
        
        v =ids(initial_state, goal_state, visited, 0, l)
        l +=1
    
       
    
        

    display_puzzle(v)

            

    




main()