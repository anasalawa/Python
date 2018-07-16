#
# A one player Connect-4 game with an AI opponent.
#
from SimpleGraphics import *
from random import randint, choice
from pprint import pprint, pformat
from time import sleep

import sys
import copy
import os
import inspect
import traceback

# Constants for each possible state for a location on the board
BLANK = 0
PLAYER_1 = 1
PLAYER_2 = 2

SIZE = 75
BUTTON_HEIGHT = 40
STATUS_HEIGHT = 20

THINK_TIME = 0.5

###############################################################################
##
##  Insert your code for createBoard, columnFull, dropChecker, and gameTied
##  here.  Do not modify any code above this point in the file.
##
###############################################################################

# PART 1: Creating the Board
def createBoard(row, column):
  board = []
  for row1 in range(row):
    board.append([])
    for col in range(column):
      board[row1].append(BLANK)

  return board

# PART 2: CHECKING IF A COLUMN IS FULL
def columnFull(board,column):
  for row in board:
    if row[column]:
      return True
    else:
      return False

# PART 3: DROPPING A CHECKER
def dropChecker(board,column):
  dropLocation = 0
  for row in range(len(board)):
    if board[row][column] == BLANK:
      dropLocation = dropLocation + 1
  return dropLocation - 1


# PART 4: GAME TIED
def gameTied(board):
  for column in range(len(board[0])):
    if board[0][column] == BLANK:
      return False

  return True



###############################################################################
##
##  Modify the provided implementations of wonHorizontal, wonVertical,
##  wonPosSlope, wonNegSlope and canWin so that they perform their required
##  tasks instead of always returning the same value.
##
###############################################################################

#
# Did the last move result in a 4 checker horizontal line?
#
# Parameters:
#   board: The board to check as a 2-D list.
#   column: The column in which the most recent checker was played.
#   row: The row in which the most recent checker was played.
#
# Returns: True if the last move caused a player to win, False otherwise.
#

# PART 5: HORIZONTAL VICTORY
def wonHorizontal(board, row, column):
  string = ""
  
  winCondition = board[row][column]
  
  for i in range(len(board[row])):
    if board[row][i] == winCondition:
      string = string + str(winCondition)
    
    else:
      string = string + str(board[row][i])
  
  if str(winCondition) * 4 in string:
    return True
  
  return False

    

#
# Did the last move result in a 4 checker vertical line?
#
# Parameters:
#   board: The board to check as a 2-D list.
#   column: The column in which the most recent checker was played.
#   row: The row in which the most recent checker was played.
#
# Returns: True if the last move caused a player to win, False otherwise.
#
def wonVertical(board, row, column):
  winCondition = board[row][column]
  c = 1
  for i in range(row + 1, row + 4):
    if i > 0 and i < len(board) and board[i][column] == winCondition:
      c = c + 1
  
  if c == 4:
    return True
    
  return False


# Did the last move result in a 4 checker line with positive slope?
#
# Parameters:
#   board: The board to check as a 2-D list.
#   column: The column in which the most recent checker was played.
#   row: The row in which the most recent checker was played.
#
# Returns: True if the last move caused a player to win, False otherwise.
#
def wonPosSlope(board, row, column):
  x = board[row][column]
  winCondition = 0
  if column + 3 < len(board[row]) and 2 < row < len(board):
    for i in range(4):
      if board[row - i][column + i] == x:
        winCondition = winCondition + 1
      if winCondition == 4:
        return True
  
  winCondition = 0
  if column + 2 < len(board[row]) and 2 < row + 1 < len(board):
    for i in range(-1, 3):
      if board[row - i][column + i] == x:
        winCondition = winCondition + 1
      if winCondition == 4:
        return True

  winCondition = 0
  if column + 1 < len(board[row]) and 2 < row + 2 < len(board):
    for i in range(-2, 2):
      if board[row - i][column + i] == x:
        winCondition = winCondition + 1
      if winCondition == 4:
        return True

  winCondition = 0
  if column < len(board[row]) and 2 < row + 3 < len(board):
    for i in range(-3, 1):
      if board[row - i][column + i] == x:
        winCondition = winCondition + 1
      if winCondition == 4:
        return True


  return False

#
# Did the last move result in a 4 checker line with negative slope?
#
# Parameters:
#   board: The board to check as a 2-D list.
#   column: The column in which the most recent checker was played.
#   row: The row in which the most recent checker was played.
#
# Returns: True if the last move caused a player to win, False otherwise.
#
def wonNegSlope(board, row, column):
  i = board[row][column]
  c = 0
  while row > 0 and c > 0:
    row = row - 1
    column = column - 1
    if board[row][column] == i:
      c = c + 1
    else:
      c = c - 1
    if c == 3:
      return True

  if c != 3:
    c = 0
    while row < len(board) - 1 and c < len(board[0]) - 1:
      row = row + 1
      column = column + 1
      if board[row][column] == i:
        c = c + 1
      else:
        c = c - 1
      if c == 3:
        return True
    if c != 3:
      return False

  return False

#
# Is there a move that the player can make to win the game?
#
# Parameters:
#   board: The board as a 2D list.
#   player: The player that is going to make the move, either PLAYER_1 or
#           PLAYER_2.
#
# Returns:
#   -1 if there is no winning move.  The column number in the board if there
#   is a winning move.
#
def canWin(board, player):

  return -1

###############################################################################
##
##  Do not modift any code below this point in the file.
##
###############################################################################

#
# Did the last move cause a player to win?
#
# Parameters:
#   board: The board to check as a 2-D list.
#   column: The column in which the most recent checker was played.
#   row: The row in which the most recent checker was played.
#
# Returns: True if the last move caused a player to win, False otherwise.
#
def gameWon(board, row, column):
  return wonHorizontal(board, row, column) or wonVertical(board, row, column) or wonPosSlope(board, row, column) or wonNegSlope(board, row, column)

#
# Display information about the command line parameters supported by the
# program and then terminate its execution.
#
# Parameters: None.
#
# Returns: None.
def usage():
  print()
  print("Usage: python %s [<predictable|easy|medium|hard> [<rows> <columns>]]" % sys.argv[0])
  print()
  close()
  quit()

#
# Randomly determine which player is going to make the first move
#
# Parameters: None
#
# Returns: Either PLAYER_1 or PLAYER_2 with equal probability
#
def startingPlayer():
  value = randint(0, 1)
  if value == 0:
    return PLAYER_1
  else:
    return PLAYER_2

#
# Identify the next player who is going to make a move
#
# Parameters:
#   player: The current player
#
# Returns: The next player who gets to move after the current player completes
#          their move.
#
def nextPlayer(player):
  if player == PLAYER_1:
    return PLAYER_2
  return PLAYER_1
    
# 
# Display the board in the graphics window
#
# Parameters:
#   board: The board to display
#   grid: The image to use for generating the grid
# 
# Returns: None
#
def drawBoard(board, grid):
  for r in range(len(board)):
    for c in range(len(board[0])):
      if board[r][c] == PLAYER_1:
        setColor(192, 0, 0)
        ellipse(c * SIZE + 5, r * SIZE + 5 + BUTTON_HEIGHT, SIZE - 10, SIZE - 10)
      elif board[r][c] == PLAYER_2:
        setColor(255, 255, 0)
        ellipse(c * SIZE + 5, r * SIZE + 5 + BUTTON_HEIGHT, SIZE - 10, SIZE - 10)
      drawImage(grid, c * SIZE, r * SIZE + BUTTON_HEIGHT)

#
# Draw the buttons across the top of the board.
#
# Parameters:
#   board: The game board, which is needed to know how many buttons need to
#          be drawn.
#
# Returns: None
#
def drawButtons(board):
  for c in range(len(board[0])):
    setColor(192, 192, 192)
    setWidth(1)
    setArrow(tk.NONE)
    rect(c * SIZE, 0, SIZE, BUTTON_HEIGHT) 
    if columnFull(board, c) == False:
      setColor(0, 0, 0)
      line(c * SIZE, BUTTON_HEIGHT - 1, (c + 1) * SIZE - 1, BUTTON_HEIGHT - 1, (c + 1) * SIZE - 1, 0)
      setColor(255, 255, 255)
      line(c * SIZE, BUTTON_HEIGHT - 2, c * SIZE, 0, (c + 1) * SIZE - 2, 0)
      setColor(192, 0, 0)
      setWidth(3)
      setArrow(tk.LAST)
      line((c + 0.5) * SIZE, BUTTON_HEIGHT / 8, (c + 0.5) * SIZE, BUTTON_HEIGHT * 7 / 8)

#
# Draws the status message at the bottom of the board
#
# Parameters:
#   message: The message to display
#   board: The board below which the message is displayed, needed so that
#          the vertical position can be calculated.
#
# Returns: None
#
def drawStatus(message, board):
  setColor(192, 192, 192)
  rect(0, BUTTON_HEIGHT + len(board) * SIZE, getWidth(), STATUS_HEIGHT)

  setColor(0, 0, 0)
  text(10, BUTTON_HEIGHT + len(board) * SIZE + STATUS_HEIGHT / 2, message, "w")

#
# Animate a checker dropping down in the board.
#
# Parameters:
#   board: The board, before the checker is in place
#   row, col: The position that the checker is going to land in
#   player: The player whose checker is being dropped
#   grid: The image used for drawing the grid
#
# Returns: None
#
def animateDrop(board, row, col, player, grid):
  top = BUTTON_HEIGHT - SIZE
  bottom = row * SIZE + 5 + BUTTON_HEIGHT
  for i in range(100):
    clear()
    drawStatus("", board)
    if player == PLAYER_1:
      drawButtons(board)
      setColor(192, 0, 0)
    else:
      setColor(192, 192, 192)
      rect(0, 0, (len(board) + 1) * SIZE, BUTTON_HEIGHT)
      setColor(255, 255, 0)
    ellipse(col * SIZE + 5, top + (bottom - top) / 99 * i, SIZE - 10, SIZE - 10)
    drawBoard(board, grid)
    update()

#
# A node in a game state tree used by the medium and hard AIs
#
class node:
  def __init__(self, board):
    self._board = board
    self._successors = []

  def __str__(self):
    return pformat(self._board) + "\n" + "Score: " + str(self.getScore()) + "\n" + str(self._successors) + "\n"
  
  def getSuccessors(self):
    return self._successors

  def getBoard(self):
    return self._board

  def getScore(self):
    score = 0
    for r in range(0, len(self._board)):
      for c in range(0, len(self._board[0]) - 3):
        score += self.scoreRow(r, c)
    for r in range(0, len(self._board) - 3):
      for c in range(0, len(self._board[0])):
        score += self.scoreCol(r, c)
    for r in range(0, len(self._board) - 3):
      for c in range(0, len(self._board[0]) - 3):
        score += self.scoreNeg(r, c)
    for r in range(3, len(self._board)):
      for c in range(0, len(self._board[0]) - 3):
        score += self.scorePos(r, c)

    return score

  def scoreRow(self, r, c):
    p1 = 0
    p2 = 0
    b = 0
    for i in range(4):
      if self._board[r][c+i] == PLAYER_1:
        p1 += 1
      if self._board[r][c+i] == PLAYER_2:
        p2 += 1
      if self._board[r][c+i] == BLANK:
        b += 1
    return self.gs(p1, p2, b)
  
  def scoreCol(self, r, c):
    p1 = 0
    p2 = 0
    b = 0
    for i in range(4):
      if self._board[r+i][c] == PLAYER_1:
        p1 += 1
      if self._board[r+i][c] == PLAYER_2:
        p2 += 1
      if self._board[r+i][c] == BLANK:
        b += 1
    return self.gs(p1, p2, b)
  
  def scorePos(self, r, c):
    p1 = 0
    p2 = 0
    b = 0
    for i in range(4):
      if self._board[r-i][c+i] == PLAYER_1:
        p1 += 1
      if self._board[r-i][c+i] == PLAYER_2:
        p2 += 1
      if self._board[r-i][c+i] == BLANK:
        b += 1
    return self.gs(p1, p2, b)
  
  def scoreNeg(self, r, c):
    p1 = 0
    p2 = 0
    b = 0
    for i in range(4):
      if self._board[r+i][c+i] == PLAYER_1:
        p1 += 1
      if self._board[r+i][c+i] == PLAYER_2:
        p2 += 1
      if self._board[r+i][c+i] == BLANK:
        b += 1
    return self.gs(p1, p2, b)

  def appendSuccessor(self, successor):
    self._successors.append(successor)

  def minScore(self):
    if self._successors == []:
      return self.getScore()

    ms = 0
    for child in self._successors:
      if child != None:
        cms = child.minScore()
        if cms < ms:
          ms = cms
    return ms

  def chooseCol(self):
    # Need to add a check that says if there is a winning move, take it
    cw = canWin(self.getBoard(), PLAYER_2)
    if cw != -1:
      return cw

    #for c in range(0, len(self.getBoard()[0])):
    #  if columnFull(self.getBoard(), c) == False:
    #    pos = 0
    #    while self.getSuccessors()[c].getBoard()[pos][c] == BLANK:
    #      pos += 1
    #    if gameWon(self.getSuccessors()[c].getBoard(), pos, c):
    #      return c

    scores = []
    for s in self.getSuccessors():
      if s == None:
        scores.append(0)
      else:
        scores.append(s.minScore())

    # Need to make sure that we don't try and play into a full column
    for i in range(0, len(scores)):
      if columnFull(self.getBoard(), i):
        scores[i] = -1000000 
    mx = max(scores)

    choices = []
    for i in range(0, len(scores)):
      if scores[i] == mx:
        choices.append(i)

    selection = choice(choices) 
    return selection

  #
  # Compute a score based on the number of player 1 checkers, the number of 
  # player 2 checkers and the number of blank spots in a row
  #
  # Parameters:
  #   p1: The number of player 1 checkers
  #   p2: The number of player 2 checkers
  #   b: The number of blank spots
  #
  def gs(self, p1, p2, b):
    if p1 == 4:
      return -10000
    if p2 == 4:
      return +10000
    if p1 == 3 and b == 1:
      return -720
    if p2 == 3 and b == 1:
      return 720
    if p1 == 2 and b == 2:
      return -6
    if p2 == 2 and b == 2:
      return 6
    return 0

#
# Determine where the computer controlled player should drop a checker using
# a predictable algorithm that always plays in the left-most column that
# has space in it.
#
# Parameters:
#   board: The game board immediately before the computer controlled player
#          will make its move.
#
# Returns: The column in which the computer will play
#
def ai_predictable(board):
  for c in range(0, len(board[0])):
    if columnFull(board, c) == False:
      return c

#
# Determine where the computer controlled player should drop a checker using
# an easy to defeat algorithm.
#
# Parameters:
#   board: The game board immediately before the computer controlled player
#          will make its move.
#
# Returns: The column in which the computer will play
#
def ai_easy(board):
  cw = canWin(board, PLAYER_2)
  if cw != -1:
    return cw

  col = randint(0, len(board[0]) - 1)
  while columnFull(board, col):
    col = randint(0, len(board[0]) - 1)

  return col

#
# Determine which column the computer player should chose, providing a moderate
# level of difficulty for human players.
#
# Parameters:
#   board: The current game board as a 2D list
#
# Returns: The column in which the computer will play
#
def ai_medium(board):
  root = node(board)
  genSuccessors(root, 2, PLAYER_2)
  return root.chooseCol()

#
# Determine which column the computer player should chose, providing a high
# level of difficulty for human players.
#
# Parameters:
#   board: The current game board as a 2D list
#
# Returns: The column in which the computer will play
#
def ai_hard(board):
  root = node(board)
  genSuccessors(root, 4, PLAYER_2)
  return root.chooseCol()

#
#  Build a tree of possible future game states
#
#  Parameters:
#    root: The starting state for the board.  This parameter is modified by
#          this function call.
#    level: The number of additional moves to consider
#    player: The player who is going to make the next move
#
#  Returns: The root node for the game state tree
#
def genSuccessors(root, level, player):
  board = root.getBoard()
  for c in range(len(board[0])):
    if board[0][c] == BLANK:
      nextBoard = copy.deepcopy(board)
      row = dropChecker(nextBoard, c)
      nextBoard[row][c] = player
      if level > 1:
        root.appendSuccessor(genSuccessors(node(nextBoard), level - 1, nextPlayer(player)))
      else:
        root.appendSuccessor(node(nextBoard))
    else:
      root.appendSuccessor(None)
  return root

##############################################################################
##
##  Code for testing the functions written by the students
##
##############################################################################

# Determine whether or not a function exists in the namespace at the time
# this function is called
# Parameters:
#   name: The name of the function to check the existence of
# Returns: True if the function exists, False otherwise
def functionExists(name):
  members = inspect.getmembers(sys.modules[__name__])
  for (n, m) in members:
    if n == name and inspect.isfunction(m):
      return True
  return False

# Run a series of tests on the createBoard function
# Parameters: (None)
# Returns: True if all tests passed.  False if any test fails.
def testCreateBoard():
  print("Testing createBoard...")

  # Does the createBoard function exist?
  if functionExists("createBoard"):
    print("  The function seems to exist...")
  else:
    print("  The createBoard function doesn't seem to exist...")
    return False

  for (rows, cols) in [(6, 7), (7, 6), (4, 4), (8, 10)]:
    # Try and call the function
    try:
      print("  Attempting to create a board with %d rows and %d columns... " % (rows, cols), end="")
      b = createBoard(rows, cols)
    except Exception as e:
      print("\n  FAILED: An exception occurred during the attempt.")
      traceback.print_exc(file=sys.stdout)
      return False
  
    # Does it have the correct return type?
    if type(b) is not list:
      print("\n  FAILED: The value returned was a", str(type(b)) + ", not a list.")
      return False
  
    # Does the list have the corret number of elements?
    if len(b) != rows:
      print("\n  FAILED: The board had", len(b), "rows when", rows, "were expected.")
      return False
  
    # Is each row a list?  Does each row have the current length?
    for i in range(len(b)):
      if type(b[i]) is not list:
        print("\n  FAILED: The row at index", i, "is a", str(type(b[i])) + ", not a list.")
        return False
      if len(b[i]) != cols:
        print("\n  FAILED: The row at index", i, "had", len(b[i]), "elements when", cols, "were expected.")
        return False
  
    # Is every element in the board a Blank?
    for r in range(0, len(b)):
      for c in range(0, len(b[r])):
        if type(b[r][c]) is not int:
          print("  FAILED: The value in row", r, "column", c, "is a", str(type(b[r][c])) + ", not an integer")
          return False
        if b[r][c] != BLANK:
          print("\n  FAILED: The integer in row", r, "column", c, "is '%d', which is not a blank space.  All spaces in the initial board must be BLANK." % b[r][c])
          return False
  
    print("Success.")

  print()
  return True

# Run a series of tests on the columnFull function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testColumnFull():
  print("Testing columnFull...")

  # Does the columnFull function exist?
  if functionExists("columnFull"):
    print("  The function seems to exist...")
  else:
    print("  The columnFull function doesn't seem to exist...")
    return False

  # Run a series of test cases
  for (b, c, a) in [([[0, 0], [0, 0]], 0, False), \
      ([[0, 0], [1, 2]], 0, False), \
      ([[1, 0], [1, 2]], 0, True), \
      ([[1, 0], [1, 2]], 1, False), \
      ([[1, 2], [1, 2]], 1, True), \
      ([[0, 0, 1], [0, 0, 2]], 0, False), \
      ([[0, 0, 1], [0, 0, 2]], 1, False), \
      ([[0, 0, 1], [0, 0, 2]], 2, True), \
      ([[0, 2, 0], [0, 1, 0], [0, 2, 0], [0, 1, 0]], 0, False), \
      ([[0, 2, 0], [0, 1, 0], [0, 2, 0], [0, 1, 0]], 1, True), \
      ([[0, 2, 0], [0, 1, 0], [0, 2, 0], [0, 1, 0]], 2, False)]:
    # Attempt the function call
    try:
      print("  Attempting to use columnFull on board:")
      print("    [%s," % str(b[0]))
      for i in range(1, len(b) - 1):
        print("     ", b[i], ",", sep="")
      print("     ", b[-1], "]", sep="")
      print("  at column %d... " % c, end="")
      result = columnFull(b, c)
    except Exception as e:
      print("\n  FAILED: An exception occurred during the attempt.")
      traceback.print_exc(file=sys.stdout)
      return False

    # Does it have the correct return type?
    if type(result) is not bool:
      print("\n  FAILED: The value returned was a", str(type(result)) + ", not a Boolean.")
      return False

    # Did it return the correct value
    if result != a:
      print("\n  FAILED: The value returned was", str(result), "when", str(a), "was expected.")
      return False

    print("Success.")

  print()
  return True

# Run a series of tests on the dropChecker function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testDropChecker():
  print("Testing dropChecker...")

  # Does the dropChecker function exist?
  if functionExists("dropChecker"):
    print("  The function seems to exist...")
  else:
    print("  The dropChecker function doesn't seem to exist...")
    return False

  # Run a series of test cases
  for (b, c, a) in [([[0, 0], [0, 0]], 0, 1), \
      ([[0, 0], [1, 2]], 0, 0), \
      ([[1, 0], [1, 2]], 1, 0), \
      ([[0, 0, 1], [2, 0, 2]], 0, 0), \
      ([[0, 0, 1], [2, 0, 2]], 1, 1), \
      ([[0, 0, 1], [2, 1, 2]], 1, 0), \
      ([[0, 2, 0], [0, 1, 0], [0, 2, 0], [0, 1, 1]], 0, 3), \
      ([[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 1, 2]], 1, 0), \
      ([[0, 2, 0], [0, 1, 0], [0, 2, 0], [0, 1, 1]], 2, 2), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0]], 3, 4), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0]], 4, 5)]:
    # Attempt the function call
    try:
      print("  Attempting to use dropChecker on board:")
      print("    [%s," % str(b[0]))
      for i in range(1, len(b) - 1):
        print("     ", b[i], ",", sep="")
      print("     ", b[-1], "]", sep="")
      print("  at column %d... " % c, end="")
      result = dropChecker(b, c)
    except Exception as e:
      print("\n  FAILED: An exception occurred during the attempt.")
      traceback.print_exc(file=sys.stdout)
      return False

    # Does it have the correct return type?
    if type(result) is not int:
      print("\n  FAILED: The value returned was a", str(type(result)) + ", not an integer.")
      return False

    # Did it return the correct value
    if result != a:
      print("\n  FAILED: The value returned was", str(result), "when", str(a), "was expected.")
      return False

    print("Success.")

  print()
  return True

# Run a series of tests on the gameTied function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testGameTied():
  print("Testing gameTied...")

  # Does the gameTied function exist?
  if functionExists("gameTied"):
    print("  The function seems to exist...")
  else:
    print("  The gameTied function doesn't seem to exist...")
    return False

  # Run a series of test cases
  for (b, a) in [([[0, 0], [0, 0]], False), \
      ([[1, 2], [1, 2]], True), \
      ([[0, 0, 1], [2, 0, 2]], False), \
      ([[0, 0, 1], [2, 0, 2]], False), \
      ([[0, 0, 1], [2, 1, 2]], False), \
      ([[2, 1, 1], [2, 1, 2]], True), \
      ([[0, 2, 0], [0, 1, 0], [0, 2, 0], [0, 1, 1]], False), \
      ([[1, 2, 1], [2, 1, 2], [1, 2, 1], [2, 1, 2]], True), \
      ([[0, 2, 1], [2, 1, 2], [1, 2, 1], [2, 1, 2]], False), \
      ([[1, 0, 1], [2, 1, 2], [1, 2, 1], [2, 1, 2]], False), \
      ([[1, 2, 0], [2, 1, 2], [1, 2, 1], [2, 1, 2]], False), \
      ([[1, 2, 1, 2, 1, 2, 1], \
        [1, 2, 1, 2, 1, 2, 1], \
        [1, 2, 1, 2, 1, 2, 1], \
        [1, 2, 1, 2, 1, 2, 1], \
        [1, 2, 1, 2, 1, 2, 1], \
        [1, 2, 1, 1, 2, 1, 2]], True), \
      ([[1, 0, 1, 2, 1, 2, 1], \
        [1, 2, 1, 2, 1, 2, 1], \
        [1, 2, 1, 2, 1, 2, 1], \
        [1, 2, 1, 2, 1, 2, 1], \
        [1, 2, 1, 2, 1, 2, 1], \
        [1, 2, 1, 1, 2, 1, 2]], False), \
      ([[1, 2, 1, 2, 0, 2, 1], \
        [1, 2, 1, 2, 1, 2, 1], \
        [1, 2, 1, 2, 1, 2, 1], \
        [1, 2, 1, 2, 1, 2, 1], \
        [1, 2, 1, 2, 1, 2, 1], \
        [1, 2, 1, 1, 2, 1, 2]], False)]:
    # Attempt the function call
    try:
      print("  Attempting to use gameTied on board:")
      print("    [%s," % str(b[0]))
      for i in range(1, len(b) - 1):
        print("     ", b[i], ",", sep="")
      print("     ", b[-1], "]... ", sep="", end="")
      result = gameTied(b)
    except Exception as e:
      print("\n  FAILED: An exception occurred during the attempt.")
      traceback.print_exc(file=sys.stdout)
      return False

    # Does it have the correct return type?
    if type(result) is not bool:
      print("\n  FAILED: The value returned was a", str(type(result)) + ", not a Boolean.")
      return False

    # Did it return the correct value
    if result != a:
      print("\n  FAILED: The value returned was", str(result), "when", str(a), "was expected.")
      return False

    print("Success.")

  print()
  return True

#
# Run a series of tests on the wonVertical function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testWonVertical():
  print("Testing wonVertical...")

  # Does the wonVertical function exist?
  if functionExists("wonVertical"):
    print("  The function seems to exist...")
  else:
    print("  The wonVertical function doesn't seem to exist...")
    quit()

  passed = 0
  failed = 0
  # Run a series of test cases
  for (b, r, c, a) in [ \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0]], 5, 3, False), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 2, 1, 2, 0, 0]], 3, 3, False), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [1, 0, 0, 0, 0, 0, 0], \
        [2, 1, 0, 0, 0, 0, 0], \
        [2, 2, 2, 0, 0, 0, 0], \
        [1, 2, 1, 1, 0, 0, 0]], 4, 2, False), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0], \
        [1, 2, 2, 1, 0, 0, 0], \
        [2, 1, 1, 2, 1, 0, 0], \
        [2, 2, 2, 1, 1, 0, 0], \
        [1, 2, 2, 1, 1, 0, 1]], 2, 2, False), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [1, 0, 0, 0, 0, 0, 0]], 5, 0, False), \
      ([[0, 0, 0, 0], \
        [0, 0, 0, 0], \
        [0, 0, 0, 0], \
        [0, 0, 0, 2]], 3, 3, False), \
      ([[2, 1, 2, 1], \
        [2, 1, 2, 1], \
        [1, 2, 1, 2], \
        [1, 2, 1, 2]], 0, 3, False), \

      # True Vertical
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 0, 1, 2, 0, 0], \
        [0, 0, 2, 1, 2, 0, 0]], 2, 3, True), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [1, 0, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0]], 2, 0, True), \
      ([[1, 0, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0], \
        [2, 1, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0]], 0, 0, True), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [1, 0, 0, 0, 0, 0, 2], \
        [2, 1, 0, 0, 0, 1, 2], \
        [1, 2, 0, 0, 0, 1, 2], \
        [1, 2, 0, 0, 0, 1, 2]], 2, 6, True), \
      ([[0, 0, 0, 0, 0, 0, 2], \
        [1, 2, 0, 0, 0, 1, 2], \
        [1, 2, 0, 0, 0, 1, 2], \
        [1, 2, 0, 0, 0, 2, 2], \
        [2, 1, 0, 0, 0, 1, 1], \
        [1, 2, 0, 0, 0, 1, 2]], 0, 6, True), \
]:
    # Attempt the function call
    try:
      print("  Attempting to use wonVertical on board:")
      print("    [%s," % str(b[0]))
      for i in range(1, len(b) - 1):
        print("     ", b[i], ",", sep="")
      print("     ", b[-1], "]... ", sep="", end="")
      result = wonVertical(b, r, c)
    except Exception as e:
      print("\nFAILED: An exception occurred during the attempt.")
      traceback.print_exc(file=sys.stdout)
      failed += 1
      continue

    # Does it have the correct return type?
    if type(result) is not bool:
      print("\nFAILED: The value returned was a", str(type(result)) + ", not a Boolean.")
      failed += 1
      continue

    # Did it return the correct value
    if result != a:
      print("\nFAILED: The value returned was", str(result), "when", str(a), "was expected.")
      failed += 1
      continue

    print("Success.")
    passed += 1

  print()
  return (passed, failed)

#
# Run a series of tests on the wonHorizontal function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testWonHorizontal():
  print("Testing wonHorizontal...")

  # Does the wonHorizontal function exist?
  if functionExists("wonHorizontal"):
    print("  The function seems to exist...")
  else:
    print("  The wonHorizontal function doesn't seem to exist...")
    quit()

  passed = 0
  failed = 0
  # Run a series of test cases
  for (b, r, c, a) in [ \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0]], 5, 3, False), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 2, 1, 2, 0, 0]], 3, 3, False), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [1, 0, 0, 0, 0, 0, 0], \
        [2, 1, 0, 0, 0, 0, 0], \
        [2, 2, 2, 0, 0, 0, 0], \
        [1, 2, 1, 1, 0, 0, 0]], 4, 2, False), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0], \
        [1, 2, 2, 1, 0, 0, 0], \
        [2, 1, 1, 2, 1, 0, 0], \
        [2, 2, 2, 1, 1, 0, 0], \
        [1, 2, 2, 1, 1, 0, 1]], 2, 2, False), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [1, 0, 0, 0, 0, 0, 0]], 5, 0, False), \
      ([[0, 0, 0, 0], \
        [0, 0, 0, 0], \
        [0, 0, 0, 0], \
        [0, 0, 0, 2]], 3, 3, False), \
      ([[2, 1, 2, 1], \
        [2, 1, 2, 1], \
        [1, 2, 1, 2], \
        [1, 2, 1, 2]], 0, 3, False), \

      # True Horizontal
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [1, 1, 1, 1, 2, 2, 2]], 5, 1, True), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [1, 1, 1, 2, 2, 2, 2]], 5, 6, True), \
      ([[1, 1, 1, 1, 0, 0, 0], \
        [1, 2, 1, 2, 0, 0, 0], \
        [2, 1, 2, 1, 0, 0, 0], \
        [2, 1, 2, 2, 0, 0, 0], \
        [1, 2, 2, 2, 0, 0, 0], \
        [1, 2, 1, 2, 0, 0, 0]], 0, 3, True), \
      ([[0, 0, 0, 1, 1, 1, 1], \
        [0, 0, 0, 1, 2, 2, 2], \
        [0, 0, 0, 2, 1, 1, 2], \
        [0, 0, 0, 1, 2, 2, 2], \
        [0, 0, 0, 2, 1, 2, 1], \
        [0, 0, 0, 2, 1, 2, 1]], 0, 6, True), \

]:
    # Attempt the function call
    try:
      print("  Attempting to use wonHorizontal on board:")
      print("    [%s," % str(b[0]))
      for i in range(1, len(b) - 1):
        print("     ", b[i], ",", sep="")
      print("     ", b[-1], "]... ", sep="", end="")
      result = wonHorizontal(b, r, c)
    except Exception as e:
      print("\nFAILED: An exception occurred during the attempt.")
      traceback.print_exc(file=sys.stdout)
      failed += 1
      continue

    # Does it have the correct return type?
    if type(result) is not bool:
      print("\nFAILED: The value returned was a", str(type(result)) + ", not a Boolean.")
      failed += 1
      continue

    # Did it return the correct value
    if result != a:
      print("\nFAILED: The value returned was", str(result), "when", str(a), "was expected.")
      failed += 1
      continue

    print("Success.")
    passed += 1

  print()
  return (passed, failed)

#
# Run a series of tests on the wonPosSlope function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testWonPosSlope():
  print("Testing wonPosSlope...")

  # Does the wonPosSlope function exist?
  if functionExists("wonPosSlope"):
    print("  The function seems to exist...")
  else:
    print("  The wonPosSlope function doesn't seem to exist...")
    quit()

  passed = 0
  failed = 0
  # Run a series of test cases
  for (b, r, c, a) in [ \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0]], 5, 3, False), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 2, 1, 2, 0, 0]], 3, 3, False), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [1, 0, 0, 0, 0, 0, 0], \
        [2, 1, 0, 0, 0, 0, 0], \
        [2, 2, 2, 0, 0, 0, 0], \
        [1, 2, 1, 1, 0, 0, 0]], 4, 2, False), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0], \
        [1, 2, 2, 1, 0, 0, 0], \
        [2, 1, 1, 2, 1, 0, 0], \
        [2, 2, 2, 1, 1, 0, 0], \
        [1, 2, 2, 1, 1, 0, 1]], 2, 2, False), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [1, 0, 0, 0, 0, 0, 0]], 5, 0, False), \
      ([[0, 0, 0, 0], \
        [0, 0, 0, 0], \
        [0, 0, 0, 0], \
        [0, 0, 0, 2]], 3, 3, False), \
      ([[2, 1, 2, 1], \
        [2, 1, 2, 1], \
        [1, 2, 1, 2], \
        [1, 2, 1, 2]], 0, 3, False), \
      # True Pos Slope
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 1, 2, 0, 0, 0], \
        [0, 1, 2, 2, 0, 0, 0], \
        [1, 2, 2, 1, 0, 0, 0]], 3, 2, True), \
      ([[0, 0, 0, 2, 0, 0, 0], \
        [0, 0, 2, 2, 0, 0, 0], \
        [0, 2, 1, 1, 0, 0, 0], \
        [2, 1, 1, 2, 0, 0, 0], \
        [1, 1, 2, 1, 0, 0, 0], \
        [2, 2, 1, 1, 0, 0, 0]], 2, 1, True), \
      ([[0, 0, 0, 0, 0, 0, 1], \
        [0, 0, 0, 0, 0, 1, 2], \
        [0, 0, 0, 0, 1, 1, 1], \
        [0, 0, 0, 1, 2, 2, 2], \
        [0, 0, 0, 2, 1, 2, 1], \
        [0, 0, 0, 2, 1, 2, 2]], 1, 5, True), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 2], \
        [0, 0, 0, 0, 0, 2, 1], \
        [0, 0, 0, 0, 2, 1, 2], \
        [0, 0, 0, 2, 1, 1, 1]], 5, 3, True), \
      ([[0, 0, 0, 1], \
        [0, 0, 1, 2], \
        [0, 1, 2, 1], \
        [1, 2, 2, 2]], 0, 3, True), \

]:
    # Attempt the function call
    try:
      print("  Attempting to use wonPosSlope on board:")
      print("    [%s," % str(b[0]))
      for i in range(1, len(b) - 1):
        print("     ", b[i], ",", sep="")
      print("     ", b[-1], "]... ", sep="", end="")
      result = wonPosSlope(b, r, c)
    except Exception as e:
      print("\nFAILED: An exception occurred during the attempt.")
      traceback.print_exc(file=sys.stdout)
      failed += 1
      continue

    # Does it have the correct return type?
    if type(result) is not bool:
      print("\nFAILED: The value returned was a", str(type(result)) + ", not a Boolean.")
      failed += 1
      continue

    # Did it return the correct value
    if result != a:
      print("\nFAILED: The value returned was", str(result), "when", str(a), "was expected.")
      failed += 1
      continue

    print("Success.")
    passed += 1

  print()
  return (passed, failed)

#
# Run a series of tests on the wonNegSlope function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testWonNegSlope():
  print("Testing wonNegSlope...")

  # Does the wonNegSlope function exist?
  if functionExists("wonNegSlope"):
    print("  The function seems to exist...")
  else:
    print("  The wonNegSlope function doesn't seem to exist...")
    quit()

  passed = 0
  failed = 0
  # Run a series of test cases
  for (b, r, c, a) in [ \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0]], 5, 3, False), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 2, 1, 2, 0, 0]], 3, 3, False), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [1, 0, 0, 0, 0, 0, 0], \
        [2, 1, 0, 0, 0, 0, 0], \
        [2, 2, 2, 0, 0, 0, 0], \
        [1, 2, 1, 1, 0, 0, 0]], 4, 2, False), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0], \
        [1, 2, 2, 1, 0, 0, 0], \
        [2, 1, 1, 2, 1, 0, 0], \
        [2, 2, 2, 1, 1, 0, 0], \
        [1, 2, 2, 1, 1, 0, 1]], 2, 2, False), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [1, 0, 0, 0, 0, 0, 0]], 5, 0, False), \
      ([[0, 0, 0, 0], \
        [0, 0, 0, 0], \
        [0, 0, 0, 0], \
        [0, 0, 0, 2]], 3, 3, False), \
      ([[2, 1, 2, 1], \
        [2, 1, 2, 1], \
        [1, 2, 1, 2], \
        [1, 2, 1, 2]], 0, 3, False), \

      # True Neg Slope
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [1, 0, 0, 0, 0, 0, 0], \
        [2, 1, 0, 0, 0, 0, 0], \
        [2, 2, 1, 0, 0, 0, 0], \
        [1, 2, 2, 1, 0, 0, 0]], 4, 2, True), \
      ([[2, 0, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0], \
        [1, 1, 2, 1, 0, 0, 0], \
        [2, 2, 1, 2, 1, 0, 0], \
        [2, 1, 2, 2, 1, 0, 0], \
        [1, 2, 2, 1, 1, 0, 1]], 2, 2, True), \
      ([[0, 0, 0, 2, 0, 0, 0], \
        [0, 0, 0, 1, 2, 0, 0], \
        [0, 0, 0, 1, 1, 2, 1], \
        [0, 0, 0, 2, 1, 1, 2], \
        [0, 1, 0, 2, 2, 2, 2], \
        [0, 1, 0, 1, 2, 2, 1]], 0, 3, True), \
      ([[0, 0, 0, 2, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 0, 2, 1, 1, 2], \
        [0, 1, 0, 2, 2, 1, 2], \
        [0, 1, 0, 1, 2, 2, 1]], 3, 4, True), \
]:
    # Attempt the function call
    try:
      print("  Attempting to use wonNegSlope on board:")
      print("    [%s," % str(b[0]))
      for i in range(1, len(b) - 1):
        print("     ", b[i], ",", sep="")
      print("     ", b[-1], "]... ", sep="", end="")
      result = wonNegSlope(b, r, c)
    except Exception as e:
      print("\nFAILED: An exception occurred during the attempt.")
      traceback.print_exc(file=sys.stdout)
      failed += 1
      continue

    # Does it have the correct return type?
    if type(result) is not bool:
      print("\nFAILED: The value returned was a", str(type(result)) + ", not a Boolean.")
      failed += 1
      continue

    # Did it return the correct value
    if result != a:
      print("\nFAILED: The value returned was", str(result), "when", str(a), "was expected.")
      failed += 1
      continue

    print("Success.")
    passed += 1

  print()
  return (passed, failed)

#
# Run a series of tests on the canWin function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testCanWin():
  print("Testing canWin...")

  # Does the canWin function exist?
  if functionExists("canWin"):
    print("  The function seems to exist...")
  else:
    print("  The canWin function doesn't seem to exist...")
    quit()

  passed = 0
  failed = 0
  # Run a series of test cases
  for (b, p, a) in [ \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0]], PLAYER_2, -1), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 2, 1, 2, 0, 0]], PLAYER_1, -1), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 0, 1, 2, 0, 0], \
        [0, 0, 2, 1, 2, 0, 0]], PLAYER_1, 3), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [1, 0, 0, 0, 0, 0, 0], \
        [2, 1, 0, 0, 0, 0, 0], \
        [2, 2, 0, 0, 0, 0, 0], \
        [1, 2, 2, 1, 0, 0, 0]], PLAYER_1, 2), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [1, 0, 0, 0, 0, 0, 0], \
        [2, 1, 0, 0, 0, 0, 0], \
        [2, 2, 2, 0, 0, 0, 0], \
        [1, 2, 1, 1, 0, 0, 0]], PLAYER_1, -1), \
      ([[2, 0, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0], \
        [1, 1, 0, 1, 0, 0, 0], \
        [2, 2, 1, 2, 1, 0, 2], \
        [2, 1, 1, 2, 1, 0, 2], \
        [1, 2, 2, 1, 1, 0, 1]], PLAYER_2, 2), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0], \
        [1, 2, 2, 1, 0, 0, 0], \
        [2, 1, 1, 2, 0, 0, 0], \
        [2, 2, 2, 1, 1, 0, 1], \
        [1, 2, 2, 1, 2, 0, 1]], PLAYER_1, -1), \
      ([[0, 0, 0, 2, 0, 0, 0], \
        [0, 0, 0, 1, 2, 0, 0], \
        [0, 0, 0, 1, 1, 0, 1], \
        [0, 0, 0, 2, 1, 1, 2], \
        [0, 1, 0, 2, 2, 2, 2], \
        [0, 1, 0, 1, 2, 2, 1]], PLAYER_2, 5), \
      ([[0, 0, 0, 2, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 0, 2, 0, 1, 2], \
        [0, 1, 0, 2, 2, 1, 2], \
        [0, 1, 0, 1, 2, 2, 1]], PLAYER_1, 4), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0]], PLAYER_1, 0), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0], \
        [2, 1, 0, 0, 0, 0, 0], \
        [1, 2, 0, 0, 0, 0, 0]], PLAYER_1, 0), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [1, 0, 0, 0, 0, 0, 0], \
        [2, 1, 0, 0, 0, 1, 2], \
        [1, 2, 0, 0, 0, 1, 2], \
        [1, 2, 0, 0, 0, 1, 2]], PLAYER_2, 6), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [1, 0, 0, 0, 0, 1, 2], \
        [1, 2, 0, 0, 0, 1, 2], \
        [1, 2, 0, 0, 0, 2, 2], \
        [2, 1, 0, 0, 0, 1, 1], \
        [1, 2, 2, 0, 0, 1, 2]], PLAYER_2, 6), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 0, 2, 0, 0, 0], \
        [0, 1, 2, 2, 0, 0, 0], \
        [1, 2, 2, 1, 0, 0, 0]], PLAYER_1, 2), \
      ([[0, 0, 0, 2, 0, 0, 0], \
        [0, 0, 2, 2, 0, 0, 0], \
        [0, 0, 1, 1, 0, 0, 0], \
        [2, 1, 1, 2, 0, 0, 0], \
        [1, 1, 2, 1, 0, 0, 0], \
        [2, 2, 1, 1, 0, 0, 0]], PLAYER_2, 1), \
      ([[0, 0, 0, 0, 0, 0, 1], \
        [0, 0, 0, 0, 0, 0, 1], \
        [0, 0, 0, 0, 1, 2, 2], \
        [0, 0, 0, 1, 2, 1, 2], \
        [0, 0, 0, 2, 1, 2, 1], \
        [0, 0, 0, 2, 1, 2, 2]], PLAYER_1, 5), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 2], \
        [0, 0, 0, 0, 0, 2, 1], \
        [0, 0, 0, 0, 2, 1, 2], \
        [0, 0, 0, 0, 1, 1, 1]], PLAYER_2, 3), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [1, 0, 1, 1, 2, 2, 2]], PLAYER_1, 1), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [1, 1, 1, 2, 2, 2, 0]], PLAYER_2, 6), \
      ([[1, 1, 1, 0, 0, 0, 0], \
        [1, 2, 1, 2, 0, 0, 0], \
        [2, 1, 2, 1, 0, 0, 0], \
        [2, 1, 2, 2, 0, 0, 0], \
        [1, 2, 2, 2, 0, 0, 0], \
        [1, 2, 1, 2, 0, 0, 0]], PLAYER_1, 3), \
      ([[0, 0, 0, 1, 1, 1, 0], \
        [0, 0, 0, 1, 2, 2, 2], \
        [0, 0, 0, 2, 1, 1, 2], \
        [0, 0, 0, 1, 2, 2, 2], \
        [0, 0, 0, 2, 1, 2, 1], \
        [0, 0, 0, 2, 1, 2, 1]], PLAYER_1, 6), \
      ([[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [1, 0, 0, 0, 0, 0, 0]], PLAYER_2, -1), \
      ([[0, 0, 0, 0], \
        [0, 0, 0, 0], \
        [0, 0, 0, 0], \
        [0, 0, 0, 2]], PLAYER_1, -1), \
      ([[2, 1, 2, 0], \
        [2, 1, 2, 1], \
        [1, 2, 1, 2], \
        [1, 2, 1, 2]], PLAYER_1, -1), \
      ([[0, 0, 0, 0], \
        [0, 0, 1, 2], \
        [0, 1, 2, 1], \
        [1, 2, 2, 2]], PLAYER_1, 3), \
]:
    # Attempt the function call
    try:
      print("  Attempting to use canWin on board with Player %d:" % p)
      print("    [%s," % str(b[0]))
      for i in range(1, len(b) - 1):
        print("     ", b[i], ",", sep="")
      print("     ", b[-1], "]... ", sep="", end="")
      result = canWin(b, p)
    except Exception as e:
      print("\nFAILED: An exception occurred during the attempt.")
      traceback.print_exc(file=sys.stdout)
      failed += 1
      continue

    # Does it have the correct return type?
    if type(result) is not int:
      print("\nFAILED: The value returned was a", str(type(result)) + ", not an integer.")
      failed += 1
      continue

    # Did it return the correct value
    if result != a:
      print("\nFAILED: The value returned was", str(result), "when", str(a), "was expected.")
      failed += 1
      continue

    print("Success.")
    passed += 1

  print()
  return (passed, failed)

#
# Play a game of connect 4 between the user and a computer AI. 
#
# Parameters: None.
#
# Returns: None.
#
def main():
  # Set the default board size
  columns = 7
  rows = 6
  ai = ai_medium

  # Process the command line parameters and reset the game board size if
  # necessary
  if len(sys.argv) == 3 or len(sys.argv) >= 5:
    usage()
  if len(sys.argv) >= 2:
    if sys.argv[1].lower() == "predictable":
      ai = ai_predictable
      print("Setting the AI to predictable...")
    elif sys.argv[1].lower() == "easy":
      ai = ai_easy
      print("Setting the AI to easy...")
    elif sys.argv[1].lower() == "medium":
      ai = ai_medium
      print("Setting the AI to medium...")
    elif sys.argv[1].lower() == "hard":
      ai = ai_hard
      print("Setting the AI to hard...")
    else:
      print("An invalid difficulty level was specified...\n")
      usage()
  if len(sys.argv) >= 3:
    try:
      rows = int(sys.argv[2])
      if rows < 4:
        print("\nThe game board must have at least 4 rows.  Quitting...\n")
        close()
        quit()
    except ValueError:
      print("\n'%s' is not a valid number of rows.  Quitting...\n" % sys.argv[2])
      close()
      quit()

    try:
      columns = int(sys.argv[3])
      if columns < 4:
        print("\nThe game board must have at least 4 columns.  Quitting...\n")
        close()
        quit()
    except ValueError:
      print("\n'%s' is not a valid number of columns.  Quitting...\n" % sys.argv[3])
      close()
      quit()

  # Verify that the image files are present
  if os.path.isfile("Win.gif") == False or \
     os.path.isfile("Lose.gif") == False or \
     os.path.isfile("Tie.gif") == False or \
     os.path.isfile("Grid.gif") == False:
    print("This program requires access to Win.gif, Lose.gif, Tie.gif and")
    print("Grid.gif.  Please download them from the course website and save")
    print("them in the same directory as this program.")
    close()
    quit()
  
  # Test the student's functions
  if testCreateBoard() == False:
    close()
    quit()
  if testColumnFull() == False:
    close()
    quit()
  if testDropChecker() == False:
    close()
    quit()
  if testGameTied() == False:
    close()
    quit()
  (whp, whf) = testWonHorizontal()
  (wvp, wvf) = testWonVertical()
  (wpsp, wpsf) = testWonPosSlope()
  (wnsp, wnsf) = testWonNegSlope()
  (cwp, cwf) = testCanWin()

  print("Summary:")
  print("  createBoard passed all test cases!")
  print("  columnFull passed all test cases!")
  print("  dropChecker passed all test cases!")
  print("  gameTied passed all test cases!")
  failed = False
  for (p, f, name) in [(whp, whf, "wonHorizontal"), (wvp, wvf, "wonVertical"), (wpsp, wpsf, "wonPosSlope"), (wnsp, wnsf, "wonNegSlope")]:
    if f == 0:
      print("  %s passed all test cases!" % name)
    else:
      print("  %s passed" % name, p, "test cases and failed", f, "test cases.")
      failed = True
  if cwf == 0:
    print("  canWin passed all test cases!")
  else:
    print("  canWin passed", cwp, "test cases and failed", cwf, "test cases.")

  if failed or cwf > 0:
    print("  *****************************************************")
    print("  **                                                 **")
    print("  **  WARNING: THERE WERE TEST CASES THAT FAILED!!!  **")
    print("  **                                                 **")
    print("  *****************************************************")
  print()

  gridImage = loadImage("Grid.gif")

  # Resize the window so that it is exactly the right size for the board and
  # user interface
  resize(SIZE * columns, SIZE * rows + BUTTON_HEIGHT + STATUS_HEIGHT)
  setAutoUpdate(False)

  # Create the board
  print("Creating the board...")
  board = createBoard(rows, columns)

  # Identify the starting player
  turn = startingPlayer()
  print("The starting player will be Player %d..." % turn)

  # Continue playing until there is a winner
  col = -1
  row = -1
  while gameTied(board) == False and (col == -1 or gameWon(board, row, col) == False) and not closed():
    # Update the user interface
    drawBoard(board, gridImage)
    pprint(board)
    if turn == PLAYER_1:
      drawButtons(board)
      drawStatus("It's your turn!", board)
      print("It's your turn!")
      clearMouseEvents()
    else:
      setColor(192, 192, 192)
      rect(0, 0, (len(board) + 1) * SIZE, BUTTON_HEIGHT)
      drawStatus("Player 2 is thinking...", board)
      print("Player 2 is about to make it's move...")
    update()

    if turn == PLAYER_1:
      # Get a column from the user
      col = -1
      while col == -1 and not closed():
        me = getMouseEvent()
        while not closed() and (me == None or me[0] != "<ButtonRelease-1>"):
          update()
          me = getMouseEvent()

        col = mouseX() // SIZE
        if col >= len(board[0]) or col < 0 or columnFull(board, col):
          col = -1

    if turn == PLAYER_2:
      sleep(THINK_TIME)
      col = ai(board)

    row = dropChecker(board, col)
    animateDrop(board, row, col, turn, gridImage)
    board[row][col] = turn

    # Make it the other player's turn
    if turn == PLAYER_1:
      turn = PLAYER_2
    else:
      turn = PLAYER_1

  # The game is over
  drawBoard(board, gridImage)
  drawButtons(board)
  drawStatus("", board)
  update()
  
  # Need to display the winner, or a message that indicates that it was a tie
  if gameWon(board, row, col):
    if turn == PLAYER_2:
      resultImage = loadImage("Win.gif")
      drawStatus("The human player won the game!", board)
    else:
      resultImage = loadImage("Lose.gif")
      drawStatus("The human player lost the game :(", board)
    sleep(0.1)
    drawImage(resultImage, getWidth() // 2 - getWidth(resultImage) // 2, getHeight() // 2 - getHeight(resultImage) // 2)
  else:
    drawStatus("It was a tie!", board)
    sleep(0.1)
    resultImage = loadImage("Tie.gif")
    drawImage(resultImage, getWidth() // 2 - getWidth(resultImage) // 2, getHeight() // 2 - getHeight(resultImage) // 2)

# Get the game started
main()
