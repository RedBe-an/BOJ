def determine_sequence(nums):
    if nums == list(range(1, 9)):
        return "ascending"
    elif nums == list(range(8, 0, -1)):
        return "descending"
    else:
        return "mixed"


input_nums = list(map(int, input().split()))

result = determine_sequence(input_nums)
print(result)
