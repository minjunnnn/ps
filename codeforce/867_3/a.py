import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n, t = map(int, input().split())
    A = [*map(int, input().split())]
    B = [*map(int, input().split())]

    C = [*zip(A, B)]
    L = []
    for idx, i in enumerate(C):
        tt, vv = i
        tt += idx

        if tt <= t:
            L.append((idx+1, vv))

    if len(L) == 0:
        return [-1]
    else:
        return max(L, key=lambda x: x[1])
        

if __name__ == "__main__":
    for i in range(int(input())):
        print(solve()[0])
