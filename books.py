import sys

def solve():
    data = sys.stdin.read().split()
    ptr = 0
    n = int(data[ptr])

    t = int(data[ptr+1])

    ptr += 2

    a = list(int(x) for x in data[ptr:ptr+n])

    left , cur_sum , max_books = 0,0,0

    for r in range(n):
        cur_sum += a[r]

        while cur_sum > t:
            cur_sum -= a[left]
            left += 1

        current_window_size  = r - left +1
        if current_window_size > max_books:
            max_books = current_window_size

    sys.stdout.write(str(max_books))


if __name__ == "__main__":
    solve()
