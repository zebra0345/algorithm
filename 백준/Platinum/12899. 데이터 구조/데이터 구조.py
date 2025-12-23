import sys

from array import array

def ints_from_bytes(data: bytes):
    n = len(data)
    i = 0
    while i < n:
        while i < n and data[i] <= 32:
            i += 1
        if i >= n:
            break
        num = 0
        while i < n and data[i] > 32:
            num = num * 10 + (data[i] - 48)
            i += 1
        yield num

data = sys.stdin.buffer.read()
it = ints_from_bytes(data)

N = next(it)
MAX_VAL = 2_000_000

bit = array("I", [0]) * (MAX_VAL + 1)

def add(idx, delta):
    while idx <= MAX_VAL:
        bit[idx] += delta
        idx += idx & -idx

def kth(k):
    idx = 0
    step = 1 << (MAX_VAL.bit_length() - 1)
    while step:
        nxt = idx + step
        if nxt <= MAX_VAL and bit[nxt] < k:
            k -= bit[nxt]
            idx = nxt
        step >>= 1
    return idx + 1


out = []
for _ in range(N):
    t = next(it)
    x = next(it)
    if t == 1:
        add(x, 1)
    else:
        v = kth(x)
        out.append(str(v))
        add(v, -1)

sys.stdout.write("\n".join(out))
