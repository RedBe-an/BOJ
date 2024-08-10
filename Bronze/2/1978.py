def is_prime(n) -> bool:
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


N = int(input())
numbers = list(map(int, input().split()))

result = 0
for number in numbers:
    if is_prime(number):
        result += 1

print(result)
