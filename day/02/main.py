import os
input_path = os.path.join(os.path.dirname(__file__), "input.txt")

# part 1
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

# part 2
distance, depth, aim = 0, 0, 0

for line in open(input_path):
  direction, value_str = line.strip().split()
  value = int(value_str)
  if direction == "forward":
    distance += value
    depth += aim * value
  elif direction == "up":
    aim -= value
  elif direction == "down":
    aim += value

print(depth * distance)
