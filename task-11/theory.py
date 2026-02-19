#1855

from math import *
L=101
N=10+4090
i=ceil(log2(N))
I=ceil(L*i/8)
print(2048*I/2**10)

#23270

from math import *
for L in range(1,10**9):
    N=10+4090
    i=ceil(log2(N))
    I=ceil(L*i/8)
    if 3548*I>12*2**10:
        print(L)
        break
#23195
from math import *
for N in range(1,10**9):
    L = 172
    i=ceil(log2(N))
    I=ceil(L*i/8)
print(54*I/2**10)
