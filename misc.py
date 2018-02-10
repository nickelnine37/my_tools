import os
import math
import threading
import time
import numpy as np
import multiprocessing


def sigfig(x, nsf):
    """
    returns a string representation of x formatted with a precision of nsf

    Based on the webkit javascript implementation taken from here:
    https://code.google.com/p/webkit-mirror/source/browse/JavaScriptCore/kjs/number_object.cpp
    """

    x = float(x)

    if x == 0.:
        return "0." + "0" * (p - 1)

    out = []

    if x < 0:
        out.append("-")
        x = -x

    e = int(math.log10(x))
    tens = math.pow(10, e - nsf + 1)
    n = math.floor(x / tens)

    if n < math.pow(10, nsf - 1):
        e = e - 1
        tens = math.pow(10, e - nsf + 1)
        n = math.floor(x / tens)

    if abs((n + 1.) * tens - x) <= abs(n * tens - x):
        n = n + 1

    if n >= math.pow(10, nsf):
        n = n / 10.
        e = e + 1

    m = "%.*g" % (nsf, n)

    if e < -2 or e >= nsf:
        out.append(m[0])
        if nsf > 1:
            out.append(".")
            out.extend(m[1:nsf])
        out.append('e')
        if e > 0:
            out.append("+")
        out.append(str(e))
    elif e == (nsf - 1):
        out.append(m)
    elif e >= 0:
        out.append(m[:e + 1])
        if e + 1 < len(m):
            out.append(".")
            out.extend(m[e + 1:])
    else:
        out.append("0.")
        out.extend(["0"] * -(e + 1))
        out.append(m)

    return "".join(out)


def beep():
    os.system('play --no-show-progress --null --channels 1 synth 0.5 sine 440')
