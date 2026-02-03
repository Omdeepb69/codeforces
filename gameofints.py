import sys 

def solve():
    data = sys.stdin.read().split()

    if not data :
        return 
    
    ptr = 0
    
    t = int(data[ptr])

    ptr += 1

    res = []

    for _ in range(t):
        n = int(data[ptr])
        ptr+=1

        if n%3 != 0:
            res.append("First")

        else:
            res.append("Second")

    sys.stdout.write("\n".join(res)+"\n")

if __name__ == "__main__":
    solve()


