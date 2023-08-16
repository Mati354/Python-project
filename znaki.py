def analyze_word(word):
    word_upper = word.upper()
    word_lower = word.lower()
    word_length = len(word)
    
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    print(f"Entered word: {word}")
    print(f"Word in uppercase: {word_upper}")
    print(f"Word in lowercase: {word_lower}")
    print(f"Word length: {word_length}")
    print("Number of occurrences of each letter:")
    for letter, count in letter_count.items():
        print(f"{letter}: {count}")

word = input("Enter a word: ")
analyze_word(word)
