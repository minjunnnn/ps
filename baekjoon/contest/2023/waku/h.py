import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n = int(input())

    s = (n - 1) ** 2
    print(s)

    for i in range(2, n + 1):
        print(1, i)

    
if __name__ == "__main__":
    solve()
