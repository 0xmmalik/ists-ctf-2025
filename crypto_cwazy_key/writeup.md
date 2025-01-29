# ISTS CTF 2025 Writeup — Cwazy Key

#### Challenge Setup.
The encryption function generates a random key of size five and XORs each character of the flag with it. 

#### Solution.
Theoretically, we _could_ try every possible key and see which plaintext creates a reasonable flag. But we could save a lot of time and resources by noticing that the first five characters must be the flag wrapper, `ISTS{`. Fortunately, the key has length five, so we can trivially determine what key was used for encryption by XORing `ISTS{` with the first five characters of the encrypted flag. This uses the property of XOR (`^`) that `(A ^ B) ^ C = A ^ (B ^ C)`. Now, because `A ^ B ^ B = A`, we can simply apply the key again to reveal the flag. A full solve script can be [solve.py](solve.py).
