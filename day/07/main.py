import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")


def parse_input():
  with open(input_path) as f:
    return [int(x) for x in f.read().split(",") if x]


numbers = sorted(parse_input())


def compute_fuel(numbers, center):
  return sum(abs(n - center) for n in numbers)


# part 1
median = numbers[len(numbers) // 2]
total_fuel = compute_fuel(numbers, median)
print(total_fuel)


def compute_fuel_quadratic(numbers, center):
  return sum(abs(n - center) * (abs(n - center) + 1) // 2 for n in numbers)


# part 2
center = sum(numbers) / len(numbers)
total_fuel = min(
    compute_fuel_quadratic(numbers, v) for v in (int(center), int(center + 1)))
print(total_fuel)
