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
        x = int(data[ptr+1])

        ptr += 2

        a = [int(x) for x in data[ptr:ptr+n]]
        ptr += n
        max_dist = a[0]

        for i in range(1,n):
            dist =  a[i] - a[i-1]
            if dist > max_dist:
                max_dist = dist 
       
        turn_t = 2 * (x- a[-1])
        if turn_t > max_dist:
            max_dist = turn_t

        res.append(str(max_dist))

    sys.stdout.write("\n".join(res)+"\n")


if __name__ == "__main__":
    solve()

        




        