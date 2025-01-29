crib = "ISTS{"
enc = "FcGYnlBjz\"?op:{>Af9g?B2w"

key = [(ord(crib[i]) ^ ord(enc[i])) for i in range(5)]
key = key * (len(enc) // len(key)) + key[:len(enc) % len(key)]

flag = ''.join(chr(ord(c) ^ key[i] & 0xFF) for i, c in enumerate(enc))
print(flag)
