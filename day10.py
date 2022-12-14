#! /usr/local/bin/python3
####################################
# --- Day 10: Cathode-Ray Tube --- #
####################################

import AOCUtils
import re
DAY = AOCUtils.setDay(__file__)
logger = AOCUtils.setLogger(DAY)

#####
# -- TESTS --
####
def test_solvePart1():
  input = ['addx 15',
           'addx -11',
           'addx 6',
           'addx -3',
           'addx 5',
           'addx -1',
           'addx -8',
           'addx 13',
           'addx 4',
           'noop',
           'addx -1',
           'addx 5',
           'addx -1',
           'addx 5',
           'addx -1',
           'addx 5',
           'addx -1',
           'addx 5',
           'addx -1',
           'addx -35',
           'addx 1',
           'addx 24',
           'addx -19',
           'addx 1',
           'addx 16',
           'addx -11',
           'noop',
           'noop',
           'addx 21',
           'addx -15',
           'noop',
           'noop',
           'addx -3',
           'addx 9',
           'addx 1',
           'addx -3',
           'addx 8',
           'addx 1',
           'addx 5',
           'noop',
           'noop',
           'noop',
           'noop',
           'noop',
           'addx -36',
           'noop',
           'addx 1',
           'addx 7',
           'noop',
           'noop',
           'noop',
           'addx 2',
           'addx 6',
           'noop',
           'noop',
           'noop',
           'noop',
           'noop',
           'addx 1',
           'noop',
           'noop',
           'addx 7',
           'addx 1',
           'noop',
           'addx -13',
           'addx 13',
           'addx 7',
           'noop',
           'addx 1',
           'addx -33',
           'noop',
           'noop',
           'noop',
           'addx 2',
           'noop',
           'noop',
           'noop',
           'addx 8',
           'noop',
           'addx -1',
           'addx 2',
           'addx 1',
           'noop',
           'addx 17',
           'addx -9',
           'addx 1',
           'addx 1',
           'addx -3',
           'addx 11',
           'noop',
           'noop',
           'addx 1',
           'noop',
           'addx 1',
           'noop',
           'noop',
           'addx -13',
           'addx -19',
           'addx 1',
           'addx 3',
           'addx 26',
           'addx -30',
           'addx 12',
           'addx -1',
           'addx 3',
           'addx 1',
           'noop',
           'noop',
           'noop',
           'addx -9',
           'addx 18',
           'addx 1',
           'addx 2',
           'noop',
           'noop',
           'addx 9',
           'noop',
           'noop',
           'noop',
           'addx -1',
           'addx 2',
           'addx -37',
           'addx 1',
           'addx 3',
           'noop',
           'addx 15',
           'addx -21',
           'addx 22',
           'addx -6',
           'addx 1',
           'noop',
           'addx 2',
           'addx 1',
           'noop',
           'addx -10',
           'noop',
           'noop',
           'addx 20',
           'addx 1',
           'addx 2',
           'addx 2',
           'addx -6',
           'addx -11',
           'noop',
           'noop',
           'noop']

  assert(solvePart1(input)) == 13140
  assert(solvePart2(input)) == """##..##..##..##..##..##..##..##..##..##..\n
  ###...###...###...###...###...###...###.
  ####....####....####....####....####....
  #####.....#####.....#####.....#####.....
  ######......######......######......####
  #######.......#######.......#######....."""

######
def getInstructionValue(ins):
  if ins == 'noop':
    return ''

  return int(ins.replace('addx ', ''))

# noop = 1 cycle | addx DD = 2 cycles
def solvePart1(input):
  value = ''

  answer = 0

  xReg = 1
  cycle = 0
  count = 0
  ss = []

  for ins in input:
    value = getInstructionValue(ins)
    count = 1 if value == '' else 2

    for _ in range(count):
      cycle += 1

      # Only calculate on cycles 20, 60, 100, 140, 180, 220
      if ((cycle / 20) % 2 == 1):
        ss.append(cycle * xReg)

    if (not value == ''):
      xReg += value

  answer = sum(ss)

  return answer

def solvePart2(input):
  xReg = 1
  cycle = 0
  crtPos = 0
  row = ''

  for ins in input:
    value = getInstructionValue(ins)
    count = 1 if value == '' else 2

    for _ in range(count):
      cycle += 1

      if crtPos in [xReg-1,xReg,xReg+1]:
        pixel = '#'
      else:
        pixel = '.'
      logger.debug('{} - {} in [{},{},{}] -> {}'.format(cycle, crtPos, xReg-1, xReg, xReg + 1, pixel))
      row += pixel

      crtPos += 1

      if ((cycle / 40) % 2 in [0, 1]):
        row += "\n"
        crtPos = 0

    if (not value == ''):
      xReg += value

    logger.debug('\n' + row)

  return row

######
# -- MAIN --
######
def main():
  AOCUtils.getArgs()
  input = AOCUtils.loadInput(DAY)

  part1 = solvePart1(input)
  logger.info("\t\t== Part 1: {} ==".format(part1))

  part2 = solvePart2(input)
  logger.info("\t\t== Part 2: \n{}\n ==".format(part2))

  AOCUtils.printTimeTaken()

if __name__ == '__main__':
    main()
