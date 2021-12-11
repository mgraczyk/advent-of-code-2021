import os
import pprint
input_path = os.path.join(os.path.dirname(__file__), "input.txt")


def parse_grid(lines):
  numbers = [[int(x) for x in line.split()] for line in lines if line]
  return numbers


def parse_input():
  with open(input_path) as f:
    lines = list(f)

  numbers = [int(x) for x in lines[0].split(',')]

  grids = []
  for i in range(2, len(lines), 6):
    grids.append(parse_grid(lines[i:i + 5]))

    # Check each is unique.
    assert len({c for row in grids[-1] for c in row}) == 25

  return grids, numbers


grids, numbers = parse_input()


def check_bingo(grid_marks):
  # rows
  return (any(all(row) for row in grid_marks) or
          any(all(grid_marks[i][j] for i in range(5)) for j in range(5)))


def mark_grid(grid_marks, grid, number):
  for i in range(5):
    mark_row = grid_marks[i]
    grid_row = grid[i]
    for j in range(5):
      if number == grid_row[j]:
        mark_row[j] = 1
        # Numbers are unique.
        return

def score_grid(grid, grid_marks, number_just_called):
  total_unmarked = 0
  for i in range(5):
    for j in range(5):
      if not grid_marks[i][j]:
        total_unmarked += grid[i][j]
  return total_unmarked * number_just_called

def show_score(grid, grid_marks, number):
  print(f"bingo")
  pprint.pprint(grid_marks)
  pprint.pprint(grid)
  score = score_grid(grid, grid_marks, number)
  print(score)
  return

def part1():
  grid_marks_pairs = list(zip(grids, [
      [[0] * 5 for _ in range(5)]
      for grid in grids]))
  for number in numbers:
    for grid_idx, (grid, grid_marks) in enumerate(grid_marks_pairs):
      mark_grid(grid_marks, grid, number)
      if check_bingo(grid_marks):
        show_score(grid, grid_marks, number)
        return


def part2():
  grid_marks_pairs = list(zip(grids, [
      [[0] * 5 for _ in range(5)]
      for grid in grids]))

  for number in numbers:
    to_remove = set()
    for grid_idx, (grid, grid_marks) in enumerate(grid_marks_pairs):
      mark_grid(grid_marks, grid, number)
      if check_bingo(grid_marks):
        if len(grid_marks_pairs) == 1:
          show_score(grid, grid_marks, number)
          return
        else:
          to_remove.add(grid_idx)

    grid_marks_pairs = [
        p for i, p in enumerate(grid_marks_pairs)
        if i not in to_remove]

part1()
part2()
