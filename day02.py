#! /usr/local/bin/python3
#######################################
# --- Day 02: Rock Paper Scissors --- #
#######################################

import AOCUtils
DAY = AOCUtils.setDay(__file__)
logger = AOCUtils.setLogger(DAY)

shape_score = { 'X': 1, 'Y': 2, 'Z': 3 }
outcome_score = { 'LOSE': 0, 'DRAW': 3, 'WIN': 6 }
result_dict = {
  'AX': 'DRAW', 'AY': 'WIN', 'AZ': 'LOSE',
  'BX': 'LOSE', 'BY': 'DRAW', 'BZ': 'WIN',
  'CX': 'WIN', 'CY': 'LOSE', 'CZ': 'DRAW',
}

#####
# -- TESTS --
####
def test_solvePart2():
  input = ['A Y', 'B X', 'C Z']
  assert(solvePart2(input)) == 12

######
def solvePart1(input):
  total = 0
  for data in input:
    opp, player = data.split(' ')
    result = opp + player
    total += shape_score[player] + outcome_score[result_dict[result]]

  logger.info("\t\t== Part 1: {} ==".format(total))

def solvePart2(input):
  guide = { 'X': 'LOSE', 'Y': 'DRAW', 'Z': 'WIN' }
  total = 0
  for data in input:
    opp, round = data.split(' ')
    result = guide[round]
    for shape in list(shape_score):
      if result_dict[opp + shape] == result:
        total += outcome_score[result] + shape_score[shape]

  return total

######
# -- MAIN --
######
def main():
  AOCUtils.getArgs()
  input = AOCUtils.loadInput(DAY)

  # logger.info(input)

  solvePart1(input)
  part2 = solvePart2(input)
  logger.info("\t\t== Part 2: {} ==".format(part2))

  AOCUtils.printTimeTaken()

if __name__ == '__main__':
    main()
