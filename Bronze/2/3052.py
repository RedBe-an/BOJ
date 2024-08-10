remainders = set()

for _ in range(10):
    num = int(input())
    remainder = num % 42
    remainders.add(remainder)

print(len(remainders))
