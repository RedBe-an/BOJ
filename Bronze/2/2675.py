
T = int(input())

results = []

for _ in range(T):
    R, S = input().split()
    R = int(R)

    P = ''.join([char * R for char in S])
    
    results.append(P)

for result in results:
    print(result)
