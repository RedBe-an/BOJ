def fizzbuzz_next(seq):
    def fizzbuzz_value(n):
        if n % 3 == 0 and n % 5 == 0:
            return "FizzBuzz"
        elif n % 3 == 0:
            return "Fizz"
        elif n % 5 == 0:
            return "Buzz"
        else:
            return str(n)

    a, b, c = seq

    numbers = []
    for s in [a, b, c]:
        if s.isdigit():
            numbers.append(int(s))
        elif s == "FizzBuzz":
            numbers.append((numbers[-1] + 1 if numbers else 1))
            while numbers[-1] % 3 != 0 or numbers[-1] % 5 != 0:
                numbers[-1] += 1
        elif s == "Fizz":
            numbers.append((numbers[-1] + 1 if numbers else 1))
            while numbers[-1] % 3 != 0 or numbers[-1] % 5 == 0:
                numbers[-1] += 1
        elif s == "Buzz":
            numbers.append((numbers[-1] + 1 if numbers else 1))
            while numbers[-1] % 5 != 0 or numbers[-1] % 3 == 0:
                numbers[-1] += 1

    next_num = numbers[-1] + 1

    return fizzbuzz_value(next_num)


seq = [input().strip() for _ in range(3)]

print(fizzbuzz_next(seq))
