def new_score(score, max):
    return score / max * 100


N = int(input())
scores = list(map(int, input().split()))
new_scores = []
for score in scores:
    new_scores.append(new_score(score, max(scores)))

print(sum(new_scores) / len(new_scores))
