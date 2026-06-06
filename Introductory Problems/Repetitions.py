sequence = input()

length = 1
prev_char = sequence[0]
max_length = 1

for i in range(1, len(sequence)):
    if sequence[i] == prev_char:
        length += 1
    else:
        prev_char = sequence[i]
        length = 1

    max_length = max(max_length, length)

print(max_length)