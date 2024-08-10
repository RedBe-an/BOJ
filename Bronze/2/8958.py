n = int(input())

for _ in range(n):
    result = input().strip()
    score = 0
    current_streak = 0

    # 결과 문자열을 순회
    for char in result:
        if char == "O":
            current_streak += 1
            score += current_streak
        else:
            current_streak = 0

    # 점수 출력
    print(score)
