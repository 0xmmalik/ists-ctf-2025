# you have to guess my flag AND be lucky >:)

import random as x_292Sv
import ctypes
import sys as _92
import base64 as x_xX839
import zlib as k42_23921_aek
import base64 as _x19f0, hashlib as _zq00, marshal as _v52k, random as _rsn8, string as _t0k1, sys as _pqr6


_8398398 = 1
_91093hih = _8398398 * 9 + _8398398 - 7


def _iwo_2819(ihe98_29103):
    _17 = (_92.version_info, ihe98_29103[::-1 * _91093hih])
    return _17, x_xX839.b64encode(ihe98_29103.encode()).decode()


def _x819nf_(iio_290):
    x829_29 = _iwo_2819(iio_290)[_8398398]
    y184_29323_2482 = _829(x829_29)
    k7292_292 = x_292Sv.randint(_91093hih * 333 + _8398398, _91093hih * 3333 * _8398398)
    udu = "".join(chr(uei72_232_ ^ k7292_292) for uei72_232_ in y184_29323_2482)
    h82_2 = "".join(f"{ord(char):02x}" for char in udu)
    return h82_2


def _829(v_292):
    return k42_23921_aek.compress(v_292.encode())


def _adb829():
    oieoiwuer198498 = _x19f0.b64encode(_zq00.md5(__dm2().encode()).hexdigest().encode()).decode()
    return oieoiwuer198498


def __dm2():
    jkj29 = ''.join(_t0k1.ascii_letters + _t0k1.digits)
    return ''.join(_rsn8.choice(jkj29) for _ in range(16))


def _x819nf__():
    return "".join([_rsn8.choice(_t0k1.ascii_letters) for _ in range(100)])

def _iw0_2819():
    _count = 0
    for _ in range(50):
        _count += _rsn8.randint(1, 100)
    return _count

ueieu_293187 = "1088106c10fb10fe100310fb10fd10c510de10d910bf1084100110c3107e10c0103a10b9107b10c210fe105d10ba10c6100610bb10bb107c10f810ba10bb10fc10f910bb10bb105e108210da10be103910fa103a10bc1082100110bb107b10fc107f10c4100610c5100610ba107b10fc1081105d1000107c10c0104010f510f0109c10ca10e410d3"
_iw0_2819()
flag = _x819nf_(input("> "))
_adb829()
if flag == ueieu_293187:
    print("You're in!!!")
else:
    _x819nf__()
    print("GET OUT")
