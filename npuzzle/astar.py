##
# astar.py
#
# author : Ramprasad Tamilselvan
#
##

import util

def search(board, rIndex, cIndex, maxIndex):
    """
    Search using A* algorithm

    :param board: 2D list ( board elements )
    :param rIndex: row position of empty tile
    :param cIndex: column position of empty tile
    :param maxIndex: max row or column
    :return: None
    """
    maxDepth = 0
    maxFringe = -1
    nodesExpanded = 0
    # priority queue
    fringe = util.MyPq()
    visitedBoard = []
    node = util.State(board, [rIndex, cIndex], None)
    g = 0
    h = util.calculateHeuristic(node, maxIndex)

    # heuristic function value
    f = g + h
    fringe.put((f, node))

    # loops till queue is empty
    while not fringe.isEmpty():
        maxFringe = max(maxFringe, fringe.size())
        item = fringe.get()
        prevG = item[0]
        node = item[1]

        # reached goal state
        if util.checkGoal(node.board) == True:
            print("path_to_goal : ", node.pathToGoal)
            print("cost_of_path : ", node.costOfPath)
            print("search_depth : ", node.depth)
            print("max_search_depth : ", maxDepth)
            print("fring_size : ", fringe.size())
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
                    # calculating cost of path, path, depth, max depth
                    nextState.pathToGoal.append(nextState.direction)
                    nextState.costOfPath = node.costOfPath+1
                    nextState.depth = node.depth + 1
                    maxDepth = max(maxDepth, nextState.depth)

                    # calculating heuristic value
                    h = util.calculateHeuristic(nextState, maxIndex)
                    f = prevG + h
                    fringe.put((f, nextState))