#! /usr/local/bin/python3
###############################
# --- Day 09: Rope Bridge --- #
###############################

import AOCUtils
import re
DAY = AOCUtils.setDay(__file__)
logger = AOCUtils.setLogger(DAY)

#####
# -- TESTS --
####
def test_solvePart1():
  input = ['R 4',
           'U 4',
           'L 3',
           'D 1',
           'R 4',
           'D 1',
           'L 5',
           'R 2']

  assert(solvePart1(input)) == 0

def test_solvePart2():
  input = []

  assert(solvePart2(input)) == 0

######
def solvePart1(input):
  answer = 0

  return answer

def solvePart2(input):
  answer = 0

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
