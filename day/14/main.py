import os
import pprint
from collections import Counter, defaultdict

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_input():
  with open(input_path) as f:
    lines = [l.strip() for l in f if l.strip()]

  template = lines[0]
  rules = dict(l.split(" -> ") for l in lines[1:])
  return template, rules


def convert_to_counts(template):
  unigrams = Counter(template)
  bigrams = Counter(template[i:i + 2] for i in range(len(template) - 1))
  return defaultdict(int, unigrams), defaultdict(int, bigrams)


def do_insertion_step(unigrams, bigrams, rules):
  # Copy bigrams since we'll modify during iteration.
  for bigram, count in bigrams.copy().items():
    insert_char = rules.get(bigram)
    if insert_char is not None:
      unigrams[insert_char] += count

      bigrams[bigram] -= count
      bigrams[bigram[0] + insert_char] += count
      bigrams[insert_char + bigram[1]] += count

  return unigrams, bigrams


def part1_2(template, rules, steps):
  unigrams, bigrams = convert_to_counts(template)

  for i in range(1, steps + 1):
    unigrams, bigrams = do_insertion_step(unigrams, bigrams, rules)

  most_least_diff = max(unigrams.values()) - min(unigrams.values())
  print(f"most least diff = {most_least_diff}")


part1_2(*parse_input(), 10)
part1_2(*parse_input(), 40)
