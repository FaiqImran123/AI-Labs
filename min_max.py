from copy import *
def Min_Max(current_state, turn):
    pass




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
    st =["-"]*9
    st[0] ="X"
    st[1] ="X"
    st[8] ="X"

    print(generate_Moves(st, "O"))



main()