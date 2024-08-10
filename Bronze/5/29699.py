WTS = "WelcomeToSMUPC"
WTS_len = len(WTS)

n = int(input())

a = 0

while a == 0:
    try:
        print(WTS[n - 1])
        a = 1
    except:
        n -= WTS_len
