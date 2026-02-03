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

        a = [int(x) for x in data[ptr:ptr + n]]
        ptr += n


        #code 


        r.append("HMM")

    sys.stdout.write("\n".join(r)+"\n")


if __name__ == "__main__":
    solve()