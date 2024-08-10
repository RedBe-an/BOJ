def hotel_room_assignment(T, test_cases):
    results = []
    for i in range(T):
        H, _, N = test_cases[i]

        floor = (N - 1) % H + 1

        room_number = (N - 1) // H + 1

        room_id = floor * 100 + room_number
        results.append(room_id)

    return results


T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

results = hotel_room_assignment(T, test_cases)
for result in results:
    print(result)
