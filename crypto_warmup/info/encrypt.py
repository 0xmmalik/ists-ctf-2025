from random import randint

from string import printable

flag = open("flag.txt").read()
encrypted = "\x00"

while not all(c in printable for c in encrypted):
    key = [randint(1, 2 ** 31) for _ in range(5)]
    encrypted = ''.join(chr(ord(char) ^ key[i % len(key)] & 0xFF) for i, char in enumerate(flag))

print(encrypted)
