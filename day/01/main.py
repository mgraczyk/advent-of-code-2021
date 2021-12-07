values = [int(l) for l in open("input.txt")]
result = sum(1
    for prev, curr in zip(values, values[1:])
    if curr > prev)
print(result)
