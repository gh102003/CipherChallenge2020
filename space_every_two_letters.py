ciphertext = input("enter ciphertext: ")

for i in range(0, len(ciphertext), 2):
  print(ciphertext[i:i+2], end=" ")