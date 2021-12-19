import os
import heapq

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_input():
  with open(input_path) as f:
    lines = [l.strip() for l in f if l.strip()]

  grid = [[int(v) for v in l] for l in lines]
  return grid

def neighbors(grid, i, j):
  deltas = ((-1, 0), (1, 0), (0, -1), (0, 1))
  for di, dj in deltas:
    ni, nj = i + di, j + dj
    if (ni >= 0
        and nj >= 0
        and ni < len(grid)
        and nj < len(grid[0])):
      yield ni, nj

def find_lowest_risk_path(grid):
  heappush = heapq.heappush
  heappop = heapq.heappop

  # Heap containing total risk of path.
  # Do not count the first position
  heap = [(0, 0, 0)]
  visited = [[False] * len(row) for row in grid]
  total_risk = 0

  while heap:
    total_risk, i, j = heappop(heap)
    if visited[i][j]:
      continue

    visited[i][j] = True

    for ni, nj in neighbors(grid, i, j):
      if not visited[ni][nj]:
        heappush(heap, (total_risk + grid[ni][nj], ni, nj))

  return total_risk

def tile_grid(grid, num_times):
  n = len(grid)
  m = len(grid[0])
  return [
    [
      ((grid[i % n][j % m] + (i//n) + (j//m) - 1) % 9 + 1)
      for j in range(m * num_times)
    ]
    for i in range(n * num_times)
  ]


def part1(grid):
  endpoint_total_risk = find_lowest_risk_path(grid)
  print(f"endpoint total risk {endpoint_total_risk}")

def part2(grid):
  grid = tile_grid(grid, 5)
  endpoint_total_risk = find_lowest_risk_path(grid)
  print(f"endpoint total risk {endpoint_total_risk}")

part1(parse_input())
part2(parse_input())
