import sys

def solve():
    data = sys.stdin.read().split()
    ptr = 0

    t = int(data[ptr])
    ptr += 1

    r = []

    for _ in range(t):
        n = int(data[ptr])
        m = int(data[ptr + 1])
        ptr += 2

        x = data[ptr]
        ptr += 1

        s = data[ptr]
        ptr += 1

        cur = x
        count = 0
        found = False

        while len(cur) <= 2 * len(s):
            if s in cur:
                r.append(str(count))
                found = True
                break
            cur += cur
            count += 1

        if not found:
            r.append("-1")

    sys.stdout.write("\n".join(r))


if __name__ == "__main__":
    solve()
