import random
import sys as sys
import base64 as base64_f
import zlib as zlib
import base64 as base64, hashlib as hashlib, marshal as marshal, random as random, string as string, sys as sys


_1 = 1
_2 = _1 * 9 + _1 - 7


def func2(arg2):
    out = (sys.version_info, arg2[::-1 * _2])
    return out, base64_f.b64encode(arg2.encode()).decode()


def func1(usr_inp):
    first = func2(usr_inp)[_1]
    var2 = value(first)
    print("var2", var2, len(var2), len(first), len(usr_inp))
    print(first, "< first")
    anothervar = random.randint(_2 * 333 + _1, _2 * 3333 * _1)
    udu = "".join(chr(where ^ anothervar) for where in var2)
    h82_2 = "".join(f"{ord(char):02x}" for char in udu)
    return h82_2


def value(v_292):
    return zlib.compress(v_292.encode())


def _adb829():
    oieoiwuer198498 = base64.b64encode(hashlib.md5(__dm2().encode()).hexdigest().encode()).decode()
    return oieoiwuer198498


def __dm2():
    jkj29 = ''.join(string.ascii_letters + string.digits)
    return ''.join(random.choice(jkj29) for _ in range(16))


def _trash_code_1():
    return "".join([random.choice(string.ascii_letters) for _ in range(100)])

def _trash_code_2():
    _count = 0
    for _ in range(50):
        _count += random.randint(1, 100)
    return _count

ueieu_293187 = "9fd91998e9b19899779cd9b09cf92b9cd98f9b292d90f9b590f9af9739f69ca9cc9ce9b39f39299cd94f9b693598098590191198c9b1"
_trash_code_2()
flag = func1(input("> "))
_adb829()
print(flag)
if flag == ueieu_293187:
    print("You're in!!!")
else:
    _trash_code_1()
    print("GET OUT")
