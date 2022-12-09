#! /usr/local/bin/python3
#################################
# --- Day 05: Supply Stacks --- #
#################################

import AOCUtils
import re
DAY = AOCUtils.setDay(__file__)
logger = AOCUtils.setLogger(DAY)

#####
# -- TESTS --
####
def test_solvePart1():
  input = ['    [D]    ',
           '[N] [C]    ',
           '[Z] [M] [P]',
           ' 1   2   3 ',
           '',
           'move 1 from 2 to 1',
           'move 3 from 1 to 3',
           'move 2 from 2 to 1',
           'move 1 from 1 to 2']

  assert(solvePart1(input)) == 'CMZ'

def test_solvePart2():
  input = []
  assert(solvePart2(input)) == 0

######
def moveCrates(items, steps):
  num, fStack, tStack = steps
  newItems = items
  pullStack = newItems[fStack-1]
  pushStack = newItems[tStack-1]

  moveItem = ''
  for n in range(num):
    for i in range(len(pullStack)):
      if pullStack[i] != '':
        moveItem = pullStack[i]
        pullStack[i] = ''
        break

    for p in range(len(pushStack)-1, -1, -1):
      # logger.info('*p*' + str(p))
      if pushStack[p] == '':
        pushStack[p] = moveItem
        break
      elif p == 0:
        pushStack.insert(0, moveItem)

  return newItems

def solvePart1(input):
  answer = ''
  c = re.compile(r'(?:   |\[([A-Z])\]) ?')
  m = re.compile(r'\d+')
  foundAllCrates = False
  stacks = []
  for line in input:

    # logger.info(line)
    if (re.search(r'\s*1', line)):
      foundAllCrates = True

    if (foundAllCrates and re.search(r'^move', line)):
      moves = list(map(int, m.findall(line)))
      logger.info(moves)
      stacks = moveCrates(stacks, moves)
      logger.info(stacks)
    elif (not foundAllCrates):
      row = c.findall(line)
      for i in range(len(row)):
        try:
          stacks[i]
        except:
          stacks.append([])

        stacks[i].append(row[i])
      logger.info(stacks)

  for crates in stacks:
    if crates[0] != '':
      answer += crates[0]
    else:
      for i in range(len(crates)):
        if crates[i] != '':
          answer += crates[i]
          break

  return answer

def solvePart2(input):
  answer = 0

  #for data in input:

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
