import sys 

def solve():
    data = sys.stdin.read().split()

    n,a,b = map(int, data)

    start_pos = max(a+1,n-b)

    ans = n - start_pos + 1

    sys.stdout.write(str(ans)+"\n")


if __name__ == "__main__":
    solve()