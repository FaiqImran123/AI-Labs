from copy import *
def bfs(initial_state, goal_state, visited):

    queue =[initial_state]
    
    trace ={}
    
    trace[tuple(map(tuple, initial_state))] =None

    
  
    while len(queue)>0:
        state =queue[0]
        queue.remove(queue[0])
        visited.append(state)
        ind=index_empty(state)
        i =ind[0]
        j =ind[1]
        

        for pos in [(0,1), (0,-1),(1, 0), (-1, 0)]:
            
           
            li =deepcopy(state)
            
        
        
        
            new_pos =(i+pos[0], j + pos[1])
        
            if 0<=new_pos[0]<=2 and 0<=new_pos[1]<=2:
                li[i][j] =li[new_pos[0]][new_pos[1]]
                li[new_pos[0]][new_pos[1]] =0

               
                if li==goal_state:
                    print("Solution Found")
                    path =[]
                    path.append(tuple(map(tuple, li)))
                    path.append(tuple(map(tuple, state)))
                    val =trace[tuple(map(tuple, state))]
                    while val!=None:
                        path.append(val)
                        val =trace[val]
                    display_path(path)
                    return
                if li not in visited:
                    trace[tuple(map(tuple, li))] =tuple(map(tuple, state))
                    queue.append(li)
            
        




def index_empty(li):
    for i in range(len(li)):
        for j in range(3):
            if li[i][j]==0:
               
                return (i, j)
def display_path(path):
    path.reverse()
    for i in path:
        for j in i:
            print(j)
        print()
        print()

def main():
    initial_state =[[2,8,1],
                    [4,6,3],
                    [0, 5,7]]
    goal_state =[[1,2,3],
                 [4,5,6],
                 [7,8,0]]
    visited =[]
    bfs(initial_state, goal_state, visited)

   




main()