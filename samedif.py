import sys 
from collections import Counter 

def solve():
    data = sys.stdin.read().split()

    ptr = 0

    t = int(data[ptr])

    ptr += 1

    r =[]

    for _ in range(t):
        n = int(data[ptr])

        ptr += 1

        a = list(int(x) for x in data[ptr:ptr+n])

        ptr += n

        transforemed = []

        for i in range(n):
            transforemed.append(a[i] - i)

        counts = Counter(transforemed)

        ans = 0 

        for k in counts.values():
            if k > 1:
                ans += (k*(k-1)) // 2

        r.append(str(ans))


    sys.stdout.write("\n".join(r)+"\n")


if __name__ == "__main__":
    solve()





        