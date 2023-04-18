import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write
flush = sys.stdout.flush

def solve():
    n = int(input())

    targetIndex = n // 2 + 1
    output(f"? {targetIndex}\n")
    flush()

    target = input()

    l = 0
    r = targetIndex + 1

    while l + 1 < r:
        mid = (l + r) >> 1
        output(f"? {mid}\n")
        flush()
        t = input()
        if t == target:
            r = mid
        else:
            l = mid
    first = r

    l = targetIndex
    r = n + 1

    while l + 1 <  r:
        mid = (l + r) >> 1
        output(f"? {mid}\n")
        flush()
        t = input()
        if t == target:
            l = mid
        else:
            r = mid
    second = l

    output(f"! {first} {second}\n")
    flush()

if __name__ == "__main__":
    solve()
