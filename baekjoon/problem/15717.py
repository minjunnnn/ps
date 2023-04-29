import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write
MOD = int(10**9 + 7)

def mul(c):
    if c == 0:
        return 1
    mid = c // 2 
    if c % 2 == 0:
        return mul(mid) ** 2 % MOD
    else:
        return mul(mid) ** 2 * 2 % MOD
        

def solve():
    n = int(input())
    if n == 0:
        return 1

    return mul(n-1)

if __name__ == "__main__":
    print(solve())
