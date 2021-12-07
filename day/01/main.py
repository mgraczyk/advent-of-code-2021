import os
input_path = os.path.join(os.path.dirname(__file__), "input.txt")

values = [int(l) for l in open(input_path)]
result = sum(1
    for prev, curr in zip(values, values[1:])
    if curr > prev)
print(result)

tuples = zip(*(values[i:] for i in range(3)))
tuple_sums = list(map(sum, tuples))

result = sum(1
    for prev, curr in zip(tuple_sums, tuple_sums[1:])
    if curr > prev)
print(result)
