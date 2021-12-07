import os
from collections import defaultdict
input_path = os.path.join(os.path.dirname(__file__), "input.txt")


counts = defaultdict(int)

for line in open(input_path):
  for i, v in enumerate(line.strip()):
    if v == "1":
      counts[i] += 1
    elif v == "0":
      counts[i] -= 1
    else:
      raise NotImplementedError(v)

def digits_to_number(digits):
  result = 0
  for d in digits[:-1]:
    result += d
    result *= 2

  result += digits[-1]
  return result

gamma = digits_to_number([
  1 if v >= 0 else 0
  for v in counts.values()
])
epsilon = digits_to_number([
  0 if v >= 0 else 1
  for v in counts.values()
])

print(gamma * epsilon)
