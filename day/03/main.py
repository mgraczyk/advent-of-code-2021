import os
from collections import defaultdict
input_path = os.path.join(os.path.dirname(__file__), "input.txt")

# Part 1
def digits_to_number(digits):
  result = 0
  for d in digits[:-1]:
    result += d
    result *= 2

  result += digits[-1]
  return result

digit_str_to_int = {
  "0": 0,
  "1": 1,
}
digits = [
  tuple(digit_str_to_int[v]
      for v in line.strip())
  for line in open(input_path)
]
bit_len = max(len(d) for d in digits)

counts = [
    sum(2 * d[i] - 1 for d in digits)
    for i in range(bit_len)
]

gamma = digits_to_number([
  1 if v >= 0 else 0
  for v in counts
])
epsilon = digits_to_number([
  0 if v >= 0 else 1
  for v in counts
])

print(gamma * epsilon)

# part 2

def oxygen_bit_criteria(digits, bit_pos):
  # most common bit.
  return (1 if sum(
      d[bit_pos] for d in digits) >= (len(digits) + 1) // 2
      else 0)

def co2_bit_criteria(digits, bit_pos):
  # least common bit
  return 1 - oxygen_bit_criteria(digits, bit_pos)


def compute_rating(digits, bit_criteria):
  for bit_pos in range(bit_len):
    if len(digits) == 1:
      return digits_to_number(digits[0])

    selected_bit = bit_criteria(digits, bit_pos)
    digits = [
      d for d in digits
      if d[bit_pos] == selected_bit
    ]

  assert len(digits) == 1
  return digits_to_number(digits[0])

oxygen_rating = compute_rating(digits, oxygen_bit_criteria)
co2_rating = compute_rating(digits, co2_bit_criteria)

print(oxygen_rating * co2_rating)
