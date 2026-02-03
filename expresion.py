import sys 

def solve():
    # Read exactly three integers as per the problem
    data = sys.stdin.read().split()
    if not data: return
    
    a, b, c = map(int, data)

    # Calculate all possible results without changing the order of a, b, c
    res1 = a + b + c
    res2 = a * b * c
    res3 = (a + b) * c
    res4 = a * (b + c)
    res5 = a + (b * c)
    res6 = (a * b) + c

    # Output the absolute maximum
    sys.stdout.write(str(max(res1, res2, res3, res4, res5, res6)) + "\n")

if __name__ == "__main__":
    solve()