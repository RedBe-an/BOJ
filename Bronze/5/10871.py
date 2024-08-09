N,X = map(int,input().split())
A = [int(x) for x in input().split()] 

for i in A:
    if i < X:
        print(i,end=" ")
       