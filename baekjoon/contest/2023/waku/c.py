
import sys
from math import log2
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n = int(input())
    if n == 0:
        return 0
    log2n = log2(n)

    if int(log2n) == log2n:
        return int(log2n) + 1
    else:
        return int(log2n) + 2

if __name__ == "__main__":
    print(solve())
