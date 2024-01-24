from copy import *
def biDirectionalSearch(initial_state, goal_state):
    forward_queue =[initial_state]
    backward_queue =[goal_state]
    visited_forward =[]
    visited_backward =[]
    trace_forward ={}
    trace_forward [tuple(map(tuple, initial_state))] =0

    trace_backward ={}
    trace_backward[tuple(map(tuple, goal_state))] =0
    
    
  
    while len(forward_queue)>0 and len(backward_queue)>0:
        forward_state =forward_queue[0]
        forward_queue.remove(forward_queue[0])
        visited_forward.append(forward_state)
        backward_state =backward_queue[0]
        backward_queue.remove(backward_queue[0])
        visited_backward.append(backward_state)

  
        if forward_state==backward_state:
            print("Solution Found")
           
            path =[]
            path.append(forward_state)
            c =trace_forward[tuple(map(tuple, forward_state))]
            while c!=0:
                path.append(c)
                c =trace_forward[tuple(map(tuple, c))]
            path.reverse()
            c =trace_backward[tuple(map(tuple, forward_state))]
            while c !=0:
                path.append(c)
                c =trace_backward[tuple(map(tuple, c))]
            display_path(path)
 
            break
        
        ind=index_empty(forward_state)
        i =ind[0]
        j =ind[1]

        for pos in [(0,1), (0,-1),(1, 0), (-1, 0)]:
            
           
            li =deepcopy(forward_state)
            
        
        
        
            new_pos =(i+pos[0], j + pos[1])
        
            if 0<=new_pos[0]<=2 and 0<=new_pos[1]<=2:
                li[i][j] =li[new_pos[0]][new_pos[1]]
                li[new_pos[0]][new_pos[1]] =0

  
                if li not in visited_forward:
                    visited_forward.append(li)
                    forward_queue.append(li)
                    trace_forward[tuple(map(tuple, li))] =forward_state

            
        ind=index_empty(backward_state)
        i =ind[0]
        j =ind[1]
        
        for pos in [(0,1), (0,-1),(1, 0), (-1, 0)]:
            
           
            li =deepcopy(backward_state)
            
        
        
        
            new_pos =(i+pos[0], j + pos[1])
        
            if 0<=new_pos[0]<=2 and 0<=new_pos[1]<=2:
                li[i][j] =li[new_pos[0]][new_pos[1]]
                li[new_pos[0]][new_pos[1]] =0

  
                if li not in visited_backward:
                    visited_backward.append(li)
                    backward_queue.append(li)
                    trace_backward[tuple(map(tuple, li))] =backward_state
                    
            

def display_path(li):
    for i in li:
        print(i)
       
                

def index_empty(li):
    for i in range(len(li)):
        for j in range(3):
            if li[i][j]==0:
               
                return (i, j)
def main():
    initial_state =[[1,2,3],
                    [4,5,6],
                    [0, 7,8]]
    goal_state =[[1,2,0],
                 [4,5,3],
                 [7,8,6]]
    
    biDirectionalSearch(initial_state, goal_state)


main()