def write_file_description(file_name: str):
    line_count = 0
    char_count = 0
    word_count = 0

    with open(file_name) as file:
        for line in file:
            line_count += 1
            char_count += len(line)
            word_count += len([word for word in line.split(" ")])

    return (line_count, char_count, word_count)


line_count, char_count, word_count = write_file_description("56.text")


print(f"Lines: {line_count}, Words: {word_count}, Chars: {char_count}")
