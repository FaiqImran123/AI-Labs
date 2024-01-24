from copy import *
from time import sleep
def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("----------")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("----------")
    print(f" {board[6]} | {board[7]} | {board[8]}")

def is_won(board, value):
    if board[0]==value and board[1]==value and board[2]==value:
        return True
    elif board[0]==value and board[4]==value and board[8]==value:
        return True
    elif board[0]==value and board[3]==value and board[6]==value:
        return True
    elif board[2]==value and board[4]==value and board[6]==value:
        return True
    elif board[6]==value and board[7]==value and board[8]==value:
        return True
    elif board[1]==value and board[4]==value and board[7]==value:
        return True
    elif board[3]==value and board[4]==value and board[5]==value:
        return True
    elif board[2]==value and board[5]==value and board[8]==value:
        return True
    else:
        flag =0
        for i in range(9):
            if board[i]=="-":
                flag =1
                break
        if flag==0:
            return False
        
def playGame(board, visitedPositions):
    turn =0
    print_board(board)
    for i in range(9):

        if turn==1:
            turn =0
            board =CompTurn(board, visitedPositions)
    
            val =is_won(board, "X")
            if val==True:
                print("Comp Won")
                print()
                break
            elif val==False:
                print("Tie")
                print()
                break
            



        else:
            turn =1
            UserTurn(board, visitedPositions)
    
            val =is_won(board, "O")
          
            if val==True:
                print("User Won")
                print()
                break
            elif val==False:
                print("Tie")
                print()
                break
        print_board(board)
    print_board(board)
def UserTurn(board, visitedPositions):
    print("***User Turn***")
    position =int(input("Enter Position: "))
    while (position<1 or position>9):
        
        position =int(input("Enter Valid Position: "))
    while position in visitedPositions:
        position =int(input("Enter Valid Position: "))
        

    board[position-1] ="O"
    visitedPositions.append(position)

    


    
def CompTurn(board, visitedpostions):
    print("***Comp Turn***")
    max =-100
    st =[]
  


    moves =generate_Moves(board, "X")
  
    


   
    for i in moves:
        val =Min_Max(i, False, -100000, 1000000)
       
        if val>=max:
           
            max =val
            st =i
   
    v =board
    board =st
    for i in range(9):
        if v[i]!=board[i]:
        
            visitedpostions.append(i+1)
            break



    return board
    

def Min_Max(current_state, turn, alpha, beta):  #turn True when maximizer else minimizer
   
      
  
    if is_won(current_state, "O")== True:
        return -10
    if is_won(current_state, "X")==True:
        return 10
    if is_won(current_state, "O")==False:
        return 0
        
        
    

 
        
    
    if turn==True:
        moves =generate_Moves(current_state, "X")
        turn =not turn
        l =[]
        for i in moves:
            v =Min_Max(i, turn, alpha, beta)
            l.append(v)
            alpha =max(alpha, v)
            if beta<=alpha:
                break
        return max(l)
    else:
        moves =generate_Moves(current_state, "O")
        
        turn =not turn
        l =[]
        for i in moves:
            v =Min_Max(i, turn, alpha, beta)
            

            l.append(v)
            beta =min(beta, v)
            if beta<=alpha:
                break
        return min(l)




def generate_Moves(state, val):
    moves =possible_moves(state, val)
    return moves


    
def possible_moves(state, val):
  
    li =copy(state)
    moves =[]
   
    for i in range(9):
        if state[i]=="-":
            li[i] =val
            moves.append(li)
            li =copy(state)

    
    return moves
def main():
    board =["-"]*9

    visited_positions =[]
    playGame(board,  visited_positions)
    
    

  

main()