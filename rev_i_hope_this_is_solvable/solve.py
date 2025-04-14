import base64
import zlib


test_nums = [i for i in range(1000,9999)]

def base64_encode(str):
    return base64.b64encode(str.encode()).decode()

def rand_xor_hex(str,n):
    base64_encoded = base64_encode(str)
    zlib_compressed = zlib_compress(base64_encoded)
    xored = ''.join((chr(b ^ n) for b in zlib_compressed))
    hexed = ''.join((f'{ord(char):02x}' for char in xored))
    return hexed

def zlib_compress(str):
    return zlib.compress(str.encode())

KNOWN = "ISTS{"

num = 0

for i in range(1000,9999):
    if rand_xor_hex(KNOWN, i).startswith("1088"):
        num = i
        break

encrypted_flag = '1088106c10fb10fe100310fb10fd10c510de10d910bf1084100110c3107e10c0103a10b9107b10c210fe105d10ba10c6100610bb10bb107c10f810ba10bb10fc10f910bb10bb105e108210da10be103910fa103a10bc1082100110bb107b10fc107f10c4100610c5100610ba107b10fc1081105d1000107c10c0104010f510f0109c10ca10e410d3'
compressed = b""
prev_stop = 0
for i in range(0,len(encrypted_flag),1):
    hex_chars = encrypted_flag[prev_stop:i]
    if len(hex_chars) < 1:
        continue
    as_int = int(hex_chars, 16)
    xored = as_int ^ num
    print(hex_chars, xored)
    if xored > -1 and xored < 256:
        compressed += xored.to_bytes(1, 'big')
        prev_stop = i

print(compressed.hex())