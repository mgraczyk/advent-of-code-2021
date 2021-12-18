import os
import pprint

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_input():
  with open(input_path) as f:
    lines = [l.strip() for l in f if l]

  foldlines = [
    l.strip()
    for l in lines if l.startswith("fold")
    if l.strip()]
  non_foldlines = [
    l.strip()
    for l in lines if not l.startswith("fold")
    if l.strip()]

  dots = {tuple(int(v) for v in l.split(","))
    for l in non_foldlines}

  def parse_fold(l):
    direction, pos_str = l.rsplit(" ", 1)[-1].split("=")
    return direction, int(pos_str)

  folds = [parse_fold(l) for l in foldlines]

  return dots, folds

def print_dots(dots):
  width = max(x for x, y in dots) + 1
  height = max(y for x, y in dots) + 1

  grid = [
    ["."]*width
    for _ in range(height)]

  for x, y in dots:
    grid[y][x] = "#"

  s = "\n".join("".join(r) for r in grid)
  print(s)


def do_fold(dots, fold):
  direction, pos = fold
  def fold_dot(x, y):
    if direction == "x" and x > pos:
      return pos - (x - pos), y
    elif direction == "y" and y > pos:
      return x, pos - (y - pos)

    return x, y

  return {
      fold_dot(x, y) for x, y in dots
  }

def part1(dots, folds):
  result = do_fold(dots, folds[0])
  print(f"{len(result)} dots")

def part2(dots, folds):
  for fold in folds:
    dots = do_fold(dots, fold)

  print_dots(dots)

part1(*parse_input())
part2(*parse_input())
