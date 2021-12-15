import os
from collections import deque

input_path = os.path.join(os.path.dirname(__file__), "input.txt")


def parse_input():
  with open(input_path) as f:
    lines = [l.strip() for l in f if l]
  return [[int(l) for l in line] for line in lines]


def get_low_points(grid):
  n, m = len(grid), len(grid[0])
  low_points = []

  def is_low_point(grid, i, j):
    value = grid[i][j]
    neighbor_deltas = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for di, dj in neighbor_deltas:
      ni = i + di
      nj = j + dj
      if ni < 0 or nj < 0 or ni == n or nj == m:
        continue
      neighbor = grid[ni][nj]
      if value >= neighbor:
        return False
    return True

  return [
      (i, j) for i in range(n) for j in range(m) if is_low_point(grid, i, j)
  ]


def calc_basin_size(grid, i, j):
  # bfs for each basin.
  # optimal because we visit each grid element
  # at most a constant number of times.
  n, m = len(grid), len(grid[0])
  neighbor_deltas = ((-1, 0), (1, 0), (0, -1), (0, 1))

  basin_size = 0
  q = deque()
  q.append((i, j))
  visited = set()

  while q:
    i, j = q.pop()
    if (i, j) in visited:
      continue
    visited.add((i, j))
    basin_size += 1

    value = grid[i][j]
    for di, dj in neighbor_deltas:
      ni = i + di
      nj = j + dj
      if ni < 0 or nj < 0 or ni == n or nj == m:
        continue
      neighbor = grid[ni][nj]
      if neighbor == 9:
        continue
      if value < neighbor:
        q.append((ni, nj))

  return basin_size


def part1(grid):

  low_points = get_low_points(grid)

  total_risk_level = sum(grid[i][j] for i, j in low_points) + len(low_points)

  print(f"total risk level: {total_risk_level}")


def part2(grid):
  low_points = get_low_points(grid)
  basin_sizes = [calc_basin_size(grid, i, j) for i, j in low_points]
  assert len(basin_sizes) >= 3
  basin_sizes.sort(reverse=True)

  prod_basin_sizes = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
  print(f"Product of three largest basin sizes: {prod_basin_sizes}")
  return


grid = parse_input()
part1(grid)
part2(grid)
