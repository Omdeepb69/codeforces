import sys 

def solve():
    data = sys.stdin.read().split()
    if not data :return

    target = data.index("1")

    r = target // 5
    c = target % 5
    moves = abs(r - 2) + abs(c - 2)

    sys.stdout.write(str(moves)+"\n")

if __name__ == "__main__":
    solve()

