import sys 

def solve():
    data = sys.stdin.read().split()

    if not data :
        return
    
    ptr = 0

    t = int(data[ptr])
    ptr += 1

    results = []

    for _ in range(t):
        n = int(data[ptr])
        ptr += 1
        a = data[ptr]
        ptr += 1
        
        if "..." in a:
            results.append("2")

        else :
            count_dots = a.count(".")
            results.append(str(count_dots))


    sys.stdout.write("\n".join(results)+"\n")

if __name__ == "__main__":
    solve()



