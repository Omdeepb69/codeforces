import sys
from collections import Counter

def solve():
    input_iter = iter(sys.stdin.read().split())
    try:
        t_str = next(input_iter)
    except StopIteration:
        return
    

    t = int(t_str)

    r = []

    for _ in range(t):
        n = int(next(input_iter))

        a = [int(next(input_iter)) for _ in range(n)]

        counts = Counter(a)
        distinct_elements = list(counts.keys())
        if len(distinct_elements) == 1:
            r.append("YES")
        elif len(distinct_elements) == 2:
            val1 = counts[distinct_elements[0]]
            val2 = counts[distinct_elements[1]]

            if abs(val1-val2) <= 1:
                r.append("YES")

            else :
                r.append("NO")

        else:
            r.append("NO")

    sys.stdout.write("\n".join(r)+"\n")


if __name__=="__main__":
    solve()