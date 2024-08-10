def is_palindrom(arg):
    if arg == arg[::-1]:
        return "yes"
    return "no"


results = []

while True:
    a = input().strip()

    if a == "0":
        break

    results.append(is_palindrom(a))

for result in results:
    print(result)
