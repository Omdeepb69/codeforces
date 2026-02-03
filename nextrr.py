import sys 

def solve():
    data = sys.stdin.read().split()

    ptr = 0

    n = int(data[ptr])
    k = int(data[ptr+1])
    ptr += 2

    a = list(int(x) for x in data[ptr:ptr+n])

    k_score = a[k-1]
    ans = sum(1 for x in a if x >= k_score and x>0)

    sys.stdout.write(str(ans)+"\n")


if __name__ == "__main__":
    solve()