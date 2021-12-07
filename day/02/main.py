import os
input_path = os.path.join(os.path.dirname(__file__), "input.txt")

distance, depth = 0, 0

for line in open(input_path):
  direction, value_str = line.strip().split()
  value = int(value_str)
  if direction == "forward":
    distance += value
  elif direction == "up":
    depth -= value
  elif direction == "down":
    depth += value

print(depth * distance)
