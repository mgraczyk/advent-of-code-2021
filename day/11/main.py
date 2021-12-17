import os
import pprint
import itertools

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_input():
  with open(input_path) as f:
    lines = [l.strip() for l in f if l]

  return [[int(v) for v in l] for l in lines]

def print_grid(grid):
  print("\n".join(
    "".join(str(v) for v in l) for l in grid))

def neighbors(n, m, i, j):
  for ni in range(max(0, i - 1), min(n, i + 2)):
    for nj in range(max(0, j - 1), min(m, j + 2)):
      if ni == i and nj == j:
        continue
      yield ni, nj


def do_step(grid, flashed_at_step, step):
  n, m = len(grid), len(grid[0])

  def _flash_at_position(i, j):
    # Compare to 8 to account for energy increase
    # at the beginning of the step.
    if grid[i][j] <= 8:
      # no flash
      return

    if flashed_at_step[i][j] == step:
      # already flashed
      return

    flashed_at_step[i][j] = step
    for ni, nj in neighbors(n, m, i, j):
      grid[ni][nj] += 1
      _flash_at_position(ni, nj)

  for i in range(n):
    for j in range(m):
      _flash_at_position(i, j)

  for i in range(n):
    for j in range(m):
      value = grid[i][j] + 1
      if value > 9:
        value = 0
      grid[i][j] = value

  return sum(1 for row in flashed_at_step
      for v in row if v == step)

def part1(grid):
  flashed_at_step = [
      [0] * len(r) for r in grid
  ]

  total_flashes = 0
  for step in range(1, 101):
    # print(f"After step {step}")
    # print_grid(grid)
    total_flashes += do_step(grid, flashed_at_step, step)

  print(f"{total_flashes} total flashes")

def part2(grid):
  flashed_at_step = [
      [0] * len(r) for r in grid
  ]
  grid_size = len(grid) * len(grid[0])

  for step in itertools.count(1):
    num_flashes = do_step(grid, flashed_at_step, step)
    #print(f"After step {step + 1}")
    #print_grid(grid)
    if num_flashes == grid_size:
      break

  print(f"Grid reset at step {step}")

part1(parse_input())
part2(parse_input())
