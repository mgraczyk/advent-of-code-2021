import os
import sys
import pprint
from collections import defaultdict

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_input():
  with open(input_path) as f:
    lines = [l.strip() for l in f if l]

  edges = [l.split("-") for l in lines]
  graph = defaultdict(set)
  for node_from, node_to in edges:
    graph[node_from].add(node_to)
    graph[node_to].add(node_from)

  return dict(graph)


def part1(graph):
  pprint.pprint(graph)

  lower_caves = {
      n for n in graph
      if n.islower()
  }
  visited = set()

  def visit(state):
    if state in visited:
      return 0

    if state == "end":
      return 1

    if state in lower_caves:
      visited.add(state)

    total = sum(visit(neighbor) for neighbor in graph[state])
    if state in lower_caves:
      visited.remove(state)
    return total

  num_paths = visit("start")
  print(f"{num_paths} paths from start to end")

def part2(graph):
  lower_caves = {
      n for n in graph
      if n.islower()
  }
  visited_once = set()
  visited_twice = None

  def visit(state):
    nonlocal visited_twice
    if (state == visited_twice
        or state in visited_once and visited_twice):
      return 0

    if state == "end":
      return 1

    if state in visited_once:
      visited_twice = state
    elif state in lower_caves:
      visited_once.add(state)

    total = sum(visit(neighbor) for neighbor in graph[state] if neighbor != "start")

    if state == visited_twice:
      visited_twice = None
    else:
      visited_once.discard(state)

    return total

  num_paths = visit("start")
  print(f"{num_paths} paths from start to end")

part1(parse_input())
part2(parse_input())
