import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def vertical():
    global A
    q = A.pop(0)
    A.append(q)

def horizon():
    global A
    for i in A:
        q = i.pop(0)
        i.append(q)

def solve():
    global A, B
    h, w = map(int,input().split())

    A = [list(input()) for i in range(h)]
    B = [list(input()) for i in range(h)]

    for i in range(h):
        for j in range(w):
            horizon()
            if A == B:
                return "Yes"
        vertical()

    return "No"

if __name__ == "__main__":
    print(solve())
