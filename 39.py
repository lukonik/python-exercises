def word_count_from_file():
    words_count = 0
    with open("text.txt", "r") as file:
        all_lines = file.readlines()
        all_words = [word for line in all_lines for word in line.split()]
        words_count+=len(all_words)
    
    return words_count


print(word_count_from_file())
