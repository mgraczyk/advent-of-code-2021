import os
import pprint

input_path = os.path.join(os.path.dirname(__file__), "input.txt")


def parse_input():
  with open(input_path) as f:
    return [
        tuple(["".join(sorted(l))
               for l in part.split(" ")]
              for part in line.strip().split(" | ")
              if line)
        for line in f
    ]


entries = parse_input()

# part 1, digits 1, 4, 7, and 8
digit_lens = {2, 4, 3, 7}
num_digits = sum(1 for _, outputs in entries for output_symbol in outputs
                 if len(output_symbol) in digit_lens)
print(num_digits)


def determine_letters(entry):
  inputs, outputs = entry

  signals = [set(l) for l in inputs]

  one = next(l for l in signals if len(l) == 2)
  four = next(l for l in signals if len(l) == 4)

  zero_six_nine = [l for l in signals if len(l) == 6]

  topleft_middle = four - one
  zero = next(l for l in zero_six_nine if topleft_middle - l)

  six = next(l for l in zero_six_nine if len(one & l) != 2)
  seven = next(l for l in signals if len(l) == 3)
  eight = next(l for l in signals if len(l) == 7)
  nine = next(l for l in zero_six_nine if l is not zero and l is not six)

  two_three_five = [l for l in signals if len(l) == 5]
  three = next(l for l in two_three_five if len(l & one) == 2)
  five = next(l for l in two_three_five if len(l & six) == 5)
  two = next(l for l in two_three_five if l is not three and l is not five)

  str_to_val = {
      "".join(sorted(signal)): i
      for i, signal in zip(range(10), (zero, one, two, three, four, five, six,
                                       seven, eight, nine))
  }

  result = 0
  for output in outputs:
    result *= 10
    result += str_to_val[output]

  return result

total = sum(determine_letters(entry) for entry in entries)
print(total)
