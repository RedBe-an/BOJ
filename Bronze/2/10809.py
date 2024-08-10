S = input().strip()

positions = [-1] * 26

for index, char in enumerate(S):
    char_index = ord(char) - ord("a")
    if positions[char_index] == -1:
        positions[char_index] = index

print(" ".join(map(str, positions)))
