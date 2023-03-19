#! /usr/local/bin/python3
########################################
# --- Day 12:  --- #
########################################

import AOCUtils
import re
DAY = AOCUtils.setDay(__file__)
logger = AOCUtils.setLogger(DAY)

#####
# -- TESTS --
####
def test_solvePart1():
  input = AOCUtils.loadInput(DAY)

  assert(solvePart1(input)) == 0


def test_solvePart2():
  input = AOCUtils.loadInput(DAY)

  assert(solvePart2(input)) == 0

######
def solution(input):
  return 0

def solvePart1(input):
  return solution(input)

def solvePart2(input):
  return solution(input)

######
# -- MAIN --
######
def main():
  AOCUtils.getArgs()
  input = AOCUtils.loadInput(DAY)

  part1 = solvePart1(input)
  logger.info("\t\t== Part 1: {} ==".format(part1))

  part2 = solvePart2(input)
  logger.info("\t\t== Part 2: {} ==".format(part2))

  AOCUtils.printTimeTaken()

if __name__ == '__main__':
    main()
