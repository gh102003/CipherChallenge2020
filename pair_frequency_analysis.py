from collections import defaultdict

pairs = defaultdict(int)

ciphertext = input("Enter ciphertext: ")

for i in range(0, len(ciphertext), 2):
  pair = ciphertext[i:i+2]
  pairs[pair] += 1

total = sum(pairs.values())

print(pairs)

percentages = {pair: (occurrences / total * 100) for pair, occurrences in pairs.items()}

for pair, percentage in sorted(percentages.items(), key=lambda x: x[1], reverse=True):
  print(f"{pair}: {percentage:.3f}%")