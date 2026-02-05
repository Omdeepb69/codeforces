import sys 

def solve():
    data = sys.stdin.read().split()

    ptr = 0

    n = int(data[ptr])

    ptr+=1

    a = list(int(x) for x in data[ptr:ptr+n])

    left = 0
    max_length = 0
    counts = {}

    for r in range(n):
        val = a[r]
        counts[val] = counts.get(val,0) + 1

        while len(counts) > 1 and (max(counts.keys()) - min(counts.keys()) > 1):
            left_val = a[left]
            counts[left_val] -= 1

            if counts[left_val] == 0:
                del counts[left_val]

            left += 1

        max_length = max(max_length,r-left + 1)

    sys.stdout.write(str(max_length)+"\n")

if __name__ == "__main__":
    solve()

        



        
