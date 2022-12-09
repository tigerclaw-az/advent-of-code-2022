#! /usr/local/bin/python3
###########################################
# --- Day 03: Rucksack Reorganization --- #
###########################################

import AOCUtils
DAY = AOCUtils.setDay(__file__)
logger = AOCUtils.setLogger(DAY)

#####
# -- TESTS --
####
def test_solvePart1():
  input = ['vJrwpWtwJgWrhcsFMMfFFhFp',
           'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
           'PmmdzqPrVvPwwTWBwg',
           'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
           'ttgJtRGJQctTZtZT',
           'CrZsJsPPZsGzwwsLwLmpwMDw']
  assert(solvePart1(input)) == 157

def test_solvePart2():
  input = ['vJrwpWtwJgWrhcsFMMfFFhFp',
           'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
           'PmmdzqPrVvPwwTWBwg',
           'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
           'ttgJtRGJQctTZtZT',
           'CrZsJsPPZsGzwwsLwLmpwMDw']
  assert(solvePart2(input)) == 70

######
def getPriority(val):
  priority = list(' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
  return priority.index(val)

def solvePart1(input):
  answer = 0
  item_types = []
  for data in input:
    stop = int(len(data) / 2)
    first = slice(0, stop)
    second = slice(-1, (stop + 1) * -1, -1)
    match = False
    for f in data[first]:
      if (match): break
      for s in data[second]:
        if f == s:
          item_types.append(getPriority(f))
          match = True
          break

  answer = sum(item_types)
  return answer

def solvePart2(input):
  answer = 0
  start = 0
  item_types = []
  while (start+3 < len(input)+1):
    group = slice(start, start+3)
    rucksacks = input[group]
    logger.info(rucksacks)
    for item in rucksacks[0]:
      if (item in rucksacks[1] and item in rucksacks[2]):
        item_types.append(getPriority(item))
        break

    start += 3

  answer = sum(item_types)
  return answer

######
# -- MAIN --
######
def main():
  AOCUtils.getArgs()
  input = AOCUtils.loadInput(DAY)

  # logger.info(input)

  # part1 = solvePart1(input)
  # logger.info("\t\t== Part 1: {} ==".format(part1))

  part2 = solvePart2(input)
  logger.info("\t\t== Part 2: {} ==".format(part2))

  AOCUtils.printTimeTaken()

if __name__ == '__main__':
    main()
