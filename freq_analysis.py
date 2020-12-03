from collections import defaultdict

letters = defaultdict(int)

ciphertext = input("Enter ciphertext: ")

for c in ciphertext:
  if c != " ":
    letters[c] += 1

total = sum(letters.values())

print(letters)

percentages = {c: (occurrences / total * 100) for c, occurrences in letters.items()}

for c, p in sorted(percentages.items(), key=lambda x: x[1], reverse=True):
  print(f"{c}: {p:.3f}%")