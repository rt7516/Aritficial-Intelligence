##
# searchagent.py
#
# author : Ramprasad Tamilselvan
#
##

import bfs
import dfs
import astar
import math
import sys
import time
import util

def constructBoard(data, maxIndex):
    """
    converts list of elements into two dimensional list to represent a board
    :param data: list of elements
    :param maxIndex: max rows or columns
    :return: 2D list
    """
    board = []
    index = 0
    for i in range(maxIndex):
        temp = []
        for j in range(maxIndex):
            temp.append(int(data[index]))
            index = index + 1
        board.append(temp)

    return board

def findEmptySpace(board, maxIndex):
    """
    Finds the position of empty space in board
    :param board: 2D list
    :param maxIndex: max row or column
    :return: int, int  row, column
    """
    for i in range(maxIndex):
        for j in range(maxIndex):
            if board[i][j] == 0:
                return i, j

    return -1, -1

# main function of the program
def main():
    if len(sys.argv) != 3:
        print("Enter <search algo> <board tiles> in command line")

    # parses command line argument
    data = sys.argv[2]
    algo = sys.argv[1]
    data = data.split(',')
    maxIndex = int(math.sqrt(len(data)))
    board = constructBoard(data, maxIndex)
    rIndex, cIndex = findEmptySpace(board, maxIndex)
    util.updateGoalState(maxIndex)

    if algo == 'bfs':
        startTime = time.time()
        bfs.search(board, rIndex, cIndex, maxIndex)
        print("Execution time : %s seconds" % (time.time() - startTime))
    elif algo == 'dfs':
        startTime = time.time()
        dfs.search(board, rIndex, cIndex, maxIndex)
        print("Execution time : %s seconds" % (time.time() - startTime))
    elif algo == 'astar':
        startTime = time.time()
        astar.search(board, rIndex, cIndex, maxIndex)
        print("Execution time : %s seconds" % (time.time() - startTime))
    else:
        print("Unknown algorithm type : ", algo)


if __name__ == '__main__':
    main()
