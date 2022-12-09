#! /usr/local/bin/python3
###########################################
# --- Day 07: No Space Left On Device --- #
###########################################

import AOCUtils
import re
DAY = AOCUtils.setDay(__file__)
logger = AOCUtils.setLogger(DAY)

#####
# -- TESTS --
####
def test_solvePart1():
  input = ['$ cd /',
           '$ ls',
           'dir a',
           '14848514 b.txt',
           '8504156 c.dat',
           'dir d',
           '$ cd a',
           '$ ls',
           'dir e',
           '29116 f',
           '2557 g',
           '62596 h.lst',
           '$ cd e',
           '$ ls',
           '584 i',
           '$ cd ..',
           '$ cd ..',
           '$ cd d',
           '$ ls',
           '4060174 j',
           '8033020 d.log',
           '5626152 d.ext',
           '7214296 k']

  assert(solvePart1(input)) == 95437

def test_solvePart2():
  input = []
  assert(solvePart2(input)) == 0

######
def solvePart1(input):
  answer = 0

  for line in input:
    logger.info(line)

  return answer

def solvePart2(input):
  answer = 0

  for line in input:
    logger.info(line)

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

  # part2 = solvePart2(input)
  # logger.info("\t\t== Part 2: {} ==".format(part2))

  AOCUtils.printTimeTaken()

if __name__ == '__main__':
    main()
