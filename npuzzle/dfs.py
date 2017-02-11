##
# dfs.py
#
# author : Ramprasad Tamilselvan
#
##

import util

def search(board, rIndex, cIndex, maxIndex):
    """
    Search using depth first search algorithm
    :param board: 2D list ( board elements )
    :param rIndex: row position of empty tile
    :param cIndex: column position of empty tile
    :param maxIndex: max row or column
    :return: None
    """
    maxDepth = 0
    maxFringe = -1
    nodesExpanded = 0
    queue = []
    visitedBoard = []

    # initial state
    node = util.State(board, [rIndex, cIndex], None)
    queue.append(node)

    # loops till queue is empty
    while queue:

        maxFringe = max(maxFringe, len(queue))
        node = queue.pop(-1)

        # reaches goal state
        if util.checkGoal(node.board) == True:
            print("path_to_goal : ", node.pathToGoal)
            print("cost_of_path : ", node.costOfPath)
            print("search_depth : ", node.depth)
            print("max_search_depth : ", maxDepth)
            print("fring_size : ", len(queue))
            print("max_fringe_size : ", maxFringe)
            print("nodes_expanded : ", nodesExpanded)
            return

        # checks whether board is already visited
        if util.checkBoard(node.board, visitedBoard) == False:
            visitedBoard.append(node.board)
            nodesExpanded += 1
            # next possible states
            nextStates = util.getNextStates(node.board, node.getCurrPos(), maxIndex)
            for nextState in nextStates:
                if nextState.currPos != node.prevPos:
                    nextState.pathToGoal = list(node.pathToGoal)
                    nextState.pathToGoal.append(nextState.direction)
                    nextState.costOfPath = node.costOfPath+1
                    nextState.depth = node.depth + 1
                    maxDepth = max(maxDepth, nextState.depth)
                    queue.append(nextState)