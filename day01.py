#! /usr/local/bin/python3
####################################
# --- Day 01: Calorie Counting --- #
####################################

import AOCUtils
import re
DAY = AOCUtils.setDay(__file__)
logger = AOCUtils.setLogger(DAY)

######
# -- MAIN --
######
def main():
  AOCUtils.getArgs()
  input = AOCUtils.loadInput(DAY)

  logger.info(input)

  elf_cals = []
  total = 0

  for data in input:
    if (data != ''):
      total += int(data)
    else:
      elf_cals.append(total)
      total = 0

  elf_cals = sorted(elf_cals, reverse=True)
  print('-- part 1: ', elf_cals[0])

  top_three = sum([elf_cals[0], elf_cals[1], elf_cals[2]])
  print('-- part 2: ', top_three)

  AOCUtils.printTimeTaken()

if __name__ == '__main__':
    main()
