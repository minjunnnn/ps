import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    d1, d2, rate = map(int, input().split())
    a = (rate / 100) / max(d1, d2) 
    b = ((100 - rate) / 100) / min(d1, d2)
    c = 1 / (a + b)

    return f'{c:.6f}'
    

if __name__ == "__main__":
    print(solve())
