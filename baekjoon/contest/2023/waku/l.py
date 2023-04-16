
import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i] == 'O':
            ans += 2 ** i
            ans %= 1000000007

    print(ans)
            


if __name__ == "__main__":
    solve()
