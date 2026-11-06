import numpy as np

x = 0b010101
y = 0b100101
z = np.uint8(0b100100)

print("AND:", bin(x&y))  # AND

print("OR:", bin(x|y)) # OR

print("NOT:", bin(~z)) # NOT

print("XOR:", bin(x^y)) # XOR

print("LEFT SHIFT X:", bin(x<<2)) # LEFT SHIFT

print("RIGHT SHIFT X:", bin(x>>2)) # RIGHT SHIFT

print("LEFT SHIFT Y:", bin(y<<2)) # LEFT SHIFT

print("RIGHT SHIFT Y:", bin(y>>2)) # RIGHT SHIFT