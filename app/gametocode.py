import numpy as np


#def main():

    #sneks = [[(0,0),(0,1)],[(9,3),(9,4)]]
    #snack = [(5,4)(3,3)]

    #tonumpy(snack,sneks,10,10)

def tonumpy (enemies ,food, width, height):

    code_board = np.zeros((height,width), dtype=int)
    #print(code_board)

    for block in enemies:
        for coord in block:
            code_board[coord[0]][coord[1]] = 1

    return code_board,food[0],enemies[0][0]
    #print(code_board)

#if __name__=="__main__":
    #main()