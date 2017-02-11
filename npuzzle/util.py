##
# util.py
#
# author : Ramprasad Tamilselvan
#
##

# goal states of n-puzzle
gs1 = []
gs2 = []

class State:

    def __init__(self, board, currPos, direction):
        self.board = board
        self.currPos = currPos
        self.pathToGoal = []
        self.prevPos = []
        self.direction = direction
        self.costOfPath = 0
        self.depth = 0

    def getCurrPos(self):
        """
        gets current position
        :return: int
        """
        return self.currPos

    def getBoard(self):
        """
        gets board
        :return: 2D list
        """
        return self.board

def updateGoalState(maxIndex):
    """
    updates goal state based on n in n-puzzle

    :param maxIndex: max rows or columns
    :return: None
    """
    index = 0
    for i in range(maxIndex):
        temp = []
        for j in range(maxIndex):
            temp.append(index)
            index += 1
        gs1.append(temp)

    index = 1
    for i in range(maxIndex):
        temp = []
        for j in range(maxIndex):
            temp.append(index)
            index += 1
            if index > 8:
                index = 0
        gs2.append(temp)

class MyPq:

    def __init__(self):
        self.__prioQueue = []
        self.__size = 0

    def put(self, item):
        """
        adds element into priority queue.

        item = ( priority_number, data )
        data is inserted into queue based on priority number

        :param item: tuple (priority_number, data)
        :return: None
        """
        if self.__size == 0:
            self.__prioQueue.append(item)
        else:
            index = -1
            for val in range(self.__size):
                tup = self.__prioQueue[val]
                if item[0] < tup[0]:
                    index = val
                    break

            if index == -1:
                self.__prioQueue.append(item)
            else:
                self.__prioQueue.insert(index, item)

        self.__size += 1

    def get(self):
        """
        pops first element from the priority queue
        least priority value
        :return: data inserted
        """
        item = self.__prioQueue.pop(0)
        self.__size -= 1
        return item

    def isEmpty(self):
        """
        Checks whether queue is empty
        :return: True or False
        """
        if self.__size == 0:
            return True
        else:
            return False

    def size(self):
        """

        :return: int number of elements in list
        """
        return self.__size

def getNextStates(board, emptySpace, maxIndex):
    """
    Calculates next possible states
    :param board: 2D list ( board elements )
    :param emptySpace: position of empty tile
    :param maxIndex:  max row or column
    :return: list of next possible states
    """
    nextStates = []

    rIndex = emptySpace[0]
    cIndex = emptySpace[1]

    # get up position
    if rIndex > 0:
        up = [rIndex-1, cIndex]
        newBoard = getUpdatedBoard(board, emptySpace, up, maxIndex)
        newState = State(newBoard, up, "Up")
        nextStates.append(newState)

    # get down position
    if rIndex < maxIndex-1:
        down = [rIndex+1, cIndex]
        newBoard = getUpdatedBoard(board, emptySpace, down, maxIndex)
        newState = State(newBoard, down, "Down")
        nextStates.append(newState)

    # get left position
    if cIndex > 0:
        left = [rIndex, cIndex-1]
        newBoard = getUpdatedBoard(board, emptySpace, left, maxIndex)
        newState = State(newBoard, left, "Left")
        nextStates.append(newState)

    # get right position
    if cIndex < maxIndex-1:
        right = [rIndex, cIndex+1]
        newBoard = getUpdatedBoard(board, emptySpace, right, maxIndex)
        newState = State(newBoard, right, "Right")
        nextStates.append(newState)

    return nextStates

def checkGoal(board):
    """
    Checks whether goal states is reached or not
    :param board: 2D list ( board elements )
    :return: True or False
    """
    if board == gs1 or board == gs2:
        return True
    else:
        return False

def getUpdatedBoard(oldBoard, emptySpace, pos, maxIndex):
    """
    Swaps empty tile with the pos in the board
    :param oldBoard: 2D list
    :param emptySpace: position of empty tile
    :param pos: position to be swapped
    :param maxIndex: max row or column
    :return: update board 2D list
    """
    board = []

    for i in range(maxIndex):
        temp = list(oldBoard[i])
        board.append(temp)

    board[emptySpace[0]][emptySpace[1]] = board[pos[0]][pos[1]]
    board[pos[0]][pos[1]] = 0
    return board

def checkBoard(board, visitedBoard):
    """
    Checks whether board is in visited list

    :param board: 2D list ( board elements )
    :param visitedBoard: list of boards
    :return: True or False
    """
    if board in visitedBoard:
        return True
    else:
        return False

def calculateHeuristic(node, maxIndex):
    """
    Calculates heuristic value,
    heuristic value = sum of distances of tiles to its goal position ( excluding zero tile )
    :param node: State object
    :param maxIndex: max row or column
    :return: int heuristic value
    """
    board = node.board
    h = 0
    index = 0
    for i in range(maxIndex):
        for j in range(maxIndex):
            if board[i][j] == 0:
                index += 1
                continue
            else:
                value = board[i][j] - index
                if value < 0:
                    value = -1 * value
                h += value
            index+= 1
    return h