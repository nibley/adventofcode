num_double_words = 0
num_triple_words = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    letters = set(line)
    for letter in letters:
        if line.count(letter) == 2:
            num_double_words += 1
            break
    for letter in letters:
        if line.count(letter) == 3:
            num_triple_words += 1
            break

print(num_double_words * num_triple_words)
