ciphertext = input("Enter ciphertext: ")

key = input("enter decryption key: ")

def clean_key(key):
    out = []
    for c_in in key:
        try:
            c_out = int(c_in)
        except:
            c_out = ord(c_in.upper()) - 64
        out.append(c_out)
    return out



column_orders = clean_key(key)
column_length = len(ciphertext) // len(column_orders)

columns = {}

for i, column_order in enumerate(column_orders):
    column = ciphertext[i * column_length: (i + 1) * column_length]
    columns[column_order] = column

ordered_columns = map(lambda x: x[1], sorted(columns.items(), key=lambda x: x[0]))

plaintext = ""

## read off rows
for a, b, c in zip(*list(ordered_columns)):
    plaintext += a + b + c

print(plaintext)
