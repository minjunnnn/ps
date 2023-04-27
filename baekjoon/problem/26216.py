import sys
from math import ceil
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def findWhiteNode(n):
    global h, k
    s = 0
    child = k+1

    while True:
        a = n / child

        if a == int(a):
            s+=1
            n //= child
        else:
            break

    n = ceil(n / child)

    return [n, h - s]

def findLength(f, s):
    global h, k
    child = k+1
    fWhite = findWhiteNode(f)
    sWhite = findWhiteNode(s)
    result = 2

    while fWhite[1] != sWhite[1]:
        print(fWhite, sWhite)
        if fWhite[1] > sWhite[1]:
            fWhite = [ceil(fWhite[0]/child), fWhite[1] - 1]
            result += 1
        elif fWhite[1] < sWhite[1]:
            sWhite = [ceil(sWhite[0]/child), sWhite[1] - 1]
            result += 1
        else:
            pass
    
    while fWhite[0] != sWhite[0]:
        print(fWhite, sWhite)
        fWhite = [ceil(fWhite[0]/child), fWhite[1] - 1]
        sWhite = [ceil(sWhite[0]/child), sWhite[1] - 1]
        result += 2

        if fWhite[1] == 0:
            return -1

    return result

def solve():
    global h, k
    k, h, q = map(int, input().split())
    MAX_ = (k + 1) ** h

    for i in range(q):
        a, b = map(int, input().split())
        if a >= MAX_ or b >= MAX_:
            print(-1)
            continue
        print(findLength(a, b))

if __name__ == "__main__":
    solve()
