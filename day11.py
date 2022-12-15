#! /usr/local/bin/python3
########################################
# --- Day 11: Monkey in the Middle --- #
########################################

import AOCUtils
import re, math
DAY = AOCUtils.setDay(__file__)
logger = AOCUtils.setLogger(DAY)

#####
# -- TESTS --
####
def test_solvePart1():
  input = AOCUtils.loadInput(DAY)

  assert(solvePart1(input)) == 10605

######
def solvePart1(input):
  monkeys = []
  inspect = []

  for i in range(0, len(input), 7):
    # num = int(re.search(r'\d+', input[i]).group())
    op = re.search('old .*', input[i+2]).group().replace('old', 'item')
    monkeys.append({
      'items': list(map(int, re.findall(r'\d+', input[i+1]))),
      'operation': op,
      'test': {
        'value': int(re.search(r'\d+', input[i+3]).group()),
        True: int(re.search(r'\d+', input[i+4]).group()),
        False: int(re.search(r'\d+', input[i+5]).group()),
      },
    })
    inspect.append(0)

  for r in range(1, 21):
    logger.debug(f'== ROUND: {r} ==')
    for num in range(0, len(monkeys)):
      logger.debug(f'Monkey {num}: {monkeys[num]}')
      items = monkeys[num]['items']
      operation = monkeys[num]['operation']
      test = monkeys[num]['test']
      inspect[num] += len(items)

      # Start throwing items
      for item in items:
        logger.debug(f'Monkey inspects an item with a worry level of {item}')
        # item is used within the 'eval()' code
        item = eval(operation)
        logger.debug(f'\tWorry level is {operation} to {item}')
        item = int(math.floor(item / 3))
        logger.debug(f'\tMonkey gets bored with item. Worry level divided by 3 to {item}')

        conditional = item / test['value'] % 1 == 0
        logger.debug(f'\tCurrent worry level is ' + ('' if conditional else 'NOT ') + f"divisible by {test['value']}")
        throwTo = test[conditional]
        logger.debug(f'\tItem with worry level {item} is thrown to monkey {throwTo}.')
        monkeys[throwTo]['items'].append(item)

      # Clear items for monkey that is done throwing
      monkeys[num]['items'] = []

    logger.debug(f'== END OF ROUND: {r} ==')
    logger.debug(monkeys)

  print('-----------')
  logger.debug(f'\n{inspect}\n')
  insSorted = sorted(inspect)
  m1,m2 = [insSorted.pop(), insSorted.pop()]
  return m1 * m2

######
# -- MAIN --
######
def main():
  AOCUtils.getArgs()
  input = AOCUtils.loadInput(DAY)

  part1 = solvePart1(input)
  logger.info("\t\t== Part 1: {} ==".format(part1))

  # part2 = solvePart2(input)
  # logger.info("\t\t== Part 2: {} ==".format(part2))

  AOCUtils.printTimeTaken()

if __name__ == '__main__':
    main()
