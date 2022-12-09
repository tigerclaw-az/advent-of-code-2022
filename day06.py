#! /usr/local/bin/python3
##################################
# --- Day 06: Tuning Trouble --- #
##################################

import AOCUtils
import re
DAY = AOCUtils.setDay(__file__)
logger = AOCUtils.setLogger(DAY)

#####
# -- TESTS --
####
def test_solvePart1():
  input = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
  assert(solvePart1(input, 4)) == 7

  input = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
  assert(solvePart1(input, 4)) == 5

  input = 'nppdvjthqldpwncqszvftbrmjlhg'
  assert(solvePart1(input, 4)) == 6

  input = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
  assert(solvePart1(input, 4)) == 10

  input = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
  assert(solvePart1(input, 4)) == 11

def test_solvePart2():
  input = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
  assert(solvePart1(input, 14)) == 19

  input = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
  assert(solvePart1(input, 14)) == 23

  input = 'nppdvjthqldpwncqszvftbrmjlhg'
  assert(solvePart1(input, 14)) == 23

  input = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
  assert(solvePart1(input, 14)) == 29

  input = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
  assert(solvePart1(input, 14)) == 26

######
def solvePart1(input, marker):
  answer = 0

  curBuffer = []
  foundDupe = 0
  for pos in range(len(input)):
    if len(curBuffer) == marker:
      answer = pos
      break

    char = input[pos]
    logger.info(char)
    try:
      foundDupe = curBuffer.index(char)
      curBuffer = curBuffer[slice(foundDupe+1, len(curBuffer))]
    except:
      logger.info('no dupe')

    curBuffer.append(char)

  return answer

######
# -- MAIN --
######
def main():
  AOCUtils.getArgs()
  input = AOCUtils.loadInput(DAY)

  logger.info(input)

  part1 = solvePart1(input, 4)
  logger.info("\t\t== Part 1: {} ==".format(part1))

  part2 = solvePart1(input, 14)
  logger.info("\t\t== Part 2: {} ==".format(part2))

  AOCUtils.printTimeTaken()

if __name__ == '__main__':
    main()
