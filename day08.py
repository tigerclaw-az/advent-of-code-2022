#! /usr/local/bin/python3
######################################
# --- Day 08: Treetop Tree House --- #
######################################

import AOCUtils
import re
DAY = AOCUtils.setDay(__file__)
logger = AOCUtils.setLogger(DAY)

#####
# -- TESTS --
####
def test_solvePart1():
  input = ['30373',
           '25512',
           '65332',
           '33549',
           '35390']

  assert(solvePart1(input)) == 21

def test_solvePart2():
  input = ['30373',
           '25512',
           '65332',
           '33549',
           '35390']

  assert(solvePart2(input)) == 8

######
def setGrid(input):
  grid = []
  for line in input:
    line = str(line)
    grid.append(list(map(int, line)))

  return grid

def isEdge(row, col, size):
  if row == 0 or col == 0 or row == size or col == size:
    return True

  return False

def isShorter(row, col, grid):
  tree = grid[row][col]

  if tree > max(grid[row][:col]) or tree > max(grid[row][col+1:]) or tree > max([x[col] for x in grid[:row]]) or tree > max([x[col] for x in grid[row+1:]]):
    logger.info('{} is VISIBLE'.format(tree))
    return True

  return False

def solvePart1(input):
  answer = 0

  grid = setGrid(input)
  size = len(grid)

  for row in range(size):
    for col in range(size):
      logger.info('{},{} | {}'.format(row, col, grid[row][col]))
      if isEdge(row, col, size-1):
        answer += 1
      elif isShorter(row, col, grid):
        answer += 1

  return answer

def viewDistance(tree, trees):
  count = 0
  for t in trees:
    count += 1
    if tree <= t:
      break

  logger.info('{} => {} -- {}'.format(tree, trees, count))

  return count

def getScenicScore(row, col, grid):
  tree = grid[row][col]
  logger.info('{},{} - {}'.format(row, col, tree))

  left = viewDistance(tree, grid[row][col-1::-1])
  right = viewDistance(tree, grid[row][col+1:])
  top = viewDistance(tree, [x[col] for x in grid[row-1::-1]])
  bottom = viewDistance(tree, [x[col] for x in grid[row+1:]])

  score = top * left * right * bottom
  logger.info('{} * {} * {} * {} = {}'.format(top, left, right, bottom, score))

  return score

def solvePart2(input):
  answer = 0

  grid = setGrid(input)
  size = len(grid)

  for row in range(size):
    for col in range(size):
      if not isEdge(row, col, size-1):
        newScore = getScenicScore(row, col, grid)
        answer = newScore if newScore > answer else answer

  return answer

######
# -- MAIN --
######
def main():
  AOCUtils.getArgs()
  input = AOCUtils.loadInput(DAY)

  # logger.info(input)

  part1 = solvePart1(input)
  logger.info("\t\t== Part 1: {} ==".format(part1))

  part2 = solvePart2(input)
  logger.info("\t\t== Part 2: {} ==".format(part2))

  AOCUtils.printTimeTaken()

if __name__ == '__main__':
    main()
