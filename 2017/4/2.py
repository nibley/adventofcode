num_valid = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    unique_words = set()
    words = line.split(' ')
    valid = True
    for word in words:
        word = tuple(sorted(word))

        if word in unique_words:
            valid = False
            break
        
        unique_words.add(word)
    
    if valid:
        num_valid += 1

print(num_valid)
