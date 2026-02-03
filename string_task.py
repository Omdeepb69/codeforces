import sys
def solve():
    input_string = sys.stdin.read().strip().lower()

    if not input_string:
        return

    vowels = set("aeiouy")

    r = []

    for char in input_string:
        if char not in vowels:
            r.append(".")
            r.append(char)

    sys.stdout.write("".join(r)+"\n")


if __name__ == "__main__":
    solve()