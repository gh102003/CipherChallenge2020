import itertools
from tkinter import *

root = Tk()
root.geometry("750x500")

ciphertext_in = StringVar()
plaintext_out = StringVar()
key = StringVar()

Entry(textvariable=ciphertext_in).pack()

Label(text="Key").pack()
Entry(textvariable=key).pack()

def clean_key(key):
  out = []
  for c_in in key:
    try:
      c_out = int(c_in)
    except:
      c_out = ord(c_in.upper()) - 64
    out.append(c_out)
  return out

def decode(ciphertext, key):
  print("key:",key)
  out = ""
  for c, k in zip(ciphertext.upper(), itertools.cycle(key)):
    c_pos = ord(c) - 64
    new_pos = c_pos - int(k) + 1
    if new_pos >= 26:
      new_pos -= 26
    if new_pos < 1:
      new_pos += 26
    out += chr(new_pos + 64)
  return out

Label(textvariable=plaintext_out, wraplength=720).pack()

def update_plaintext(*args):
  decoded = decode(ciphertext_in.get().replace(" ", ""), clean_key(key.get()))
  plaintext_out.set(decoded)
  print(decoded)

ciphertext_in.trace("w", update_plaintext)
key.trace("w", update_plaintext)

root.mainloop()
