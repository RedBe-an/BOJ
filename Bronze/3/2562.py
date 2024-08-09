array = [int(input()) for _ in range(9)]

print(f"{max(array)}\n{array.index(max(array))+1}")