import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")


def get_line_score(line):
  open_to_close = {
    "[": "]",
    "{": "}",
    "(": ")",
    "<": ">",
  }
  close_to_score = {
      ")": 3,
      "]": 57,
      "}": 1197,
      ">": 25137,
  }

  stack = []
  for c in line:
    if c in "([{<":
      stack.append(c)
    else:
      assert stack
      assert c in ")]}>"
      open_c = stack.pop()
      expected_close = open_to_close[open_c]
      if c != expected_close:
        return close_to_score[c]

  return 0

def get_line_completion(line):
  open_to_close = {
    "[": "]",
    "{": "}",
    "(": ")",
    "<": ">",
  }

  stack = []
  for c in line:
    if c in "([{<":
      stack.append(c)
    else:
      assert c in ")]}>"
      assert stack
      open_c = stack.pop()
      expected_close = open_to_close[open_c]
      assert c == expected_close

  return "".join(
      open_to_close[c] for c in reversed(stack)
  )

def part1():
  with open(input_path) as f:
    lines = [l.strip() for l in f if f]

  total_score = sum(get_line_score(line) for line in lines)
  print(f"total score = {total_score}")


def part2():
  with open(input_path) as f:
    lines = [l.strip() for l in f if f]

  incomplete_lines = (
    l for l in lines
    if get_line_score(l) == 0
  )

  close_to_score = {
      ")": 1,
      "]": 2,
      "}": 3,
      ">": 4,
  }

  scores = []
  for line in incomplete_lines:
    score = 0
    for c in get_line_completion(line):
      score *= 5
      score += close_to_score[c]
    scores.append(score)

  scores.sort()
  middle_score = scores[len(scores) // 2]
  print(f"middle score {middle_score}")

part1()
part2()
