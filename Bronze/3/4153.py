import sys

results = []

while True:
    input = sys.stdin.readline
    a, b, c = input().rstrip().split()

    a, b, c = int(a), int(b), int(c)
    if a == 0 and b == 0 and c == 0:
        break

    sides = sorted([a, b, c])
    a, b, c = sides[0], sides[1], sides[2]
    if a * a + b * b == c * c:
        results.append("right")
    else:
        results.append("wrong")

for result in results:
    print(result)
