import sys 

def solve():
    data = sys.stdin.read().split()

    if not data:
        return 
    
    ptr  = 0
    t = int(data[ptr])
    ptr += 1

    results = []

    for _ in range(t):
        n = int(data[ptr])
        k = int(data[ptr+1])

        ptr += 2

        a = [int(x) for x in data[ptr:ptr+n]]

        ptr += n

        if k >= 2 :
            results.append("YES")

        else:
            is_sortd = True
            for i in range(n-1):
                if a[i] > a[i+1]:
                    is_sortd = False
                    break

            if is_sortd:
                results.append("YES")

            else:
                results.append("NO")

    sys.stdout.write("\n".join(results)+"\n")

if __name__ == "__main__":
    solve()
