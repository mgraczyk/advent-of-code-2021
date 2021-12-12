import os
import pprint
from collections import defaultdict

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_input():
  with open(input_path) as f:
    lines = [line.strip() for line in f if line]

  inout_lines = [line.split(" -> ") for line in lines]
  parsed = tuple(
      tuple(
        tuple(int(x) for x in p.split(","))
        for p in pair)
      for pair in inout_lines
  )

  return parsed


def bidi_range(a, b):
  if a > b:
    return range(b, a + 1)
  else:
    return range(a, b + 1)


def part2(lines, skip_diagonal=False):
  grid = defaultdict(int)
  for (x1, y1), (x2, y2) in lines:
    if x1 == x2:
      for y in bidi_range(y1, y2):
        grid[x1, y] += 1
    elif y1 == y2:
      for x in bidi_range(x1, x2):
        grid[x, y1] += 1
    elif not skip_diagonal:
      if x2 > x1:
        if y2 > y1:
          xy_range = zip(range(x1, x2 + 1), range(y1, y2 + 1))
        else:
          xy_range = zip(range(x1, x2 + 1), range(y1, y2 - 1, -1))
      else:
        if y2 > y1:
          xy_range = zip(range(x2, x1 + 1), range(y2, y1 - 1, -1))
        else:
          xy_range = zip(range(x2, x1 + 1), range(y2, y1 + 1))

      for x, y, in xy_range:
        grid[x, y] += 1

  return sum(1 for v in grid.values() if v >= 2)

def part1(lines):
  return part2(lines, True)

lines = parse_input()
print(part1(lines))
print(part2(lines))
