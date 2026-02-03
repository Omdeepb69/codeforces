import sys 
from collections import Counter

def solve():
    data = sys.stdin.read().split()

    ptr = 0

    t = int(data[ptr])

    ptr += 1

    r = []

    for _ in range(t):
        n = int(data[ptr])
        ptr += 1

        a = data[ptr]

        ptr += 1

        counts = Counter()
        counts[0] = 1

        cur_prefix = 0
        ans = 0 

        for i,digit in enumerate(a,1):
            cur_prefix += int(digit)
            
            val = cur_prefix -i

            ans += counts[val]

            counts[val] += 1

        r.append(str(ans))

    sys.stdout.write("\n".join(r)+"\n")


if __name__ == "__main__":
    solve()
        