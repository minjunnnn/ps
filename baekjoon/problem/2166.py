import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n = int(input())
    L = [[*map(int, input().split())] for i in range(n)]
    s=0
    L.sort(key=lambda x: (x[0], x[1]))
    for i in range(n-2):
        x1, y1= L[i]
        x2, y2 = L[i+1]
        x3, y3 = L[i+2]
        
        s += abs(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3) / 2

    return round(s, 1)
    

if __name__ == "__main__":
    print(solve())
