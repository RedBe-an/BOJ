A = int(input())
B = int(input())
C = int(input())

result = A * B * C

result_str = str(result)
count = [0] * 10

for char in result_str:
    count[int(char)] += 1

for num in count:
    print(num)
