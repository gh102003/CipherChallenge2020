# Fill in rows, reorder columns then read off rows

ciphertext = input("Enter ciphertext: ")

# key = RDF

plaintext = ""

for a, b, c in zip(ciphertext[0::3], ciphertext[1::3], ciphertext[2::3]):
  plaintext += c + a + b

print()
print(plaintext)