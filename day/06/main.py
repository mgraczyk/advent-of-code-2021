import os
import pprint

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_input():
  with open(input_path) as f:
    return [int(x) for x in f.read().split(",") if x]

def create_counts(days):
  counts = [0] * 9
  for d in days:
    counts[d] += 1
  return counts

def simulate_day(counts):
  new_counts = [0] * 9

  # Fish at 0 reproduce
  new_counts[6] += counts[0]
  new_counts[8] += counts[0]

  for d in range(1, 9):
    new_counts[d - 1] += counts[d]

  return new_counts


days = parse_input()
counts = create_counts(days)

for day in range(80):
  counts = simulate_day(counts)
print(sum(counts))

counts = create_counts(days)
for day in range(256):
  counts = simulate_day(counts)
print(sum(counts))
