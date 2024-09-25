from itertools import combinations

words = []
while True:
    try:
        line = input()
    except EOFError:
        break

    words.append(line)

if False:
    letters = set(line)
    for letter in letters:
        if line.count(letter) == 2:
            num_double_words += 1
            break
    for letter in letters:
        if line.count(letter) == 3:
            num_triple_words += 1
            break

for first_word, second_word in combinations(words, 2):
    differences = 0
    for first_word_char, second_word_char in zip(first_word, second_word):
        if first_word_char != second_word_char:
            differences += 1
        
        if differences > 1:
            break
    
    if differences == 1:
        print(''.join(first_word_char \
            for first_word_char, second_word_char \
            in zip(first_word, second_word) \
            if first_word_char == second_word_char)
        )
        break
