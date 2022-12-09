#! /usr/local/bin/python3
################################
# --- Day 04: Camp Cleanup --- #
################################

import AOCUtils
import re
DAY = AOCUtils.setDay(__file__)
logger = AOCUtils.setLogger(DAY)

#####
# -- TESTS --
####
def test_solvePart1():
  input = ['2-4, 6-8',
           '2-3, 4-5',
           '5-7, 7-9',
           '2-8, 3-7',
           '6-6, 4-6',
           '2-6, 4-8']
           # A-B, C-D
  assert(solvePart1(input)) == 2

def test_solvePart2():
  input = ['2-4, 6-8',
           '2-3, 4-5',
           '5-7, 7-9',
           '2-8, 3-7',
           '6-6, 4-6',
           '2-6, 4-8']
  assert(solvePart2(input)) == 4

######
def splitPairs(pairs):
  p = re.compile('\d+')
  return list(map(int, p.findall(pairs)))

def isMatch(A, B, C, D):
  return A == C and B == D

# (A >= C or A == D) and A <= D and (B >= C or B == D) and B <= D and |B-A| <= |D-C|
# or
# (C >= A or C == B) and C <= B and (D >= A or D == B) and D <= B and abs(B-A) >= abs(D-C)
def isContained(pairs):
  A, B, C, D = splitPairs(pairs)

  if (isMatch(A, B, C, D) or ((A >= C or A == D) and A <= D and (B >= C or B == D) and B <= D and abs(B - A) <= abs(D - C)) or
      (C >= A or C == B) and C <= B and (
      D >= A or D == B) and D <= B and abs(B-A) >= abs(D-C)
      ):
      return True

  return False

def solvePart1(input):
  answer = 0

  for pairs in input:
    if (isContained(pairs)):
      logger.info('PAIR ({}) VERIFIED'.format(pairs))
      answer += 1

  return answer

# A <= C or C <= A and B <= D or D <= B
def isOverlap(pairs):
  A, B, C, D = splitPairs(pairs)
  if (isMatch(A, B, C, D) or
      A == C or B == C or B == D or
      (A <= C and B >= C) or
      (C <= A and D >= A)):
      return True

  return False

def solvePart2(input):
  answer = 0

  for pairs in input:
    if (isOverlap(pairs)):
      logger.info('PAIR ({}) VERIFIED'.format(pairs))
      answer += 1

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
