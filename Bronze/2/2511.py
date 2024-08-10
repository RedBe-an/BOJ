A = list(map(int, input().split()))
B = list(map(int, input().split()))
score_a, score_b = 0, 0
last_winner = None

for i in range(10):
    if A[i] > B[i]:
        score_a += 3
        last_winner = "A"
    elif A[i] < B[i]:
        score_b += 3
        last_winner = "B"
    else:
        score_a += 1
        score_b += 1

print(score_a, score_b)
if score_a > score_b:
    print("A")
elif score_a < score_b:
    print("B")
else:
    if last_winner:
        print(last_winner)
    else:
        print("D")
