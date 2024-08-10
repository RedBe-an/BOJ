import sys

for line in sys.stdin:
    N, S = map(int, line.split())
    max_shares = S // (N + 1)
    print(max_shares)
