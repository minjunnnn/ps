import sys
from collections import Counter, defaultdict
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n = int(input())
    s = list(input())

    sC = Counter(s)

    sD = defaultdict(int)

    if n % 2 == 1:
        return -1

    for i in sC:
        if sC[i] > n // 2:
            return -1

    
    pairCount = 0
    for i in range(n // 2):
        if s[i] == s[n - i - 1]:
            sD[s[i]] += 1

    
    for i in sD:
        if sD[i] % 2 == 1:
            pairCount += sD[i] // 2 + 1
        else:
            pairCount += sD[i] // 2

    return pairCount

    

if __name__ == "__main__":
    for i in range(int(input())):
        print(solve())
