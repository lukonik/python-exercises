str1 = "Emma25 is Data scientist50 and AI Expert"

words = [
    word
    for word in str1.split()
    if any([le for le in word if le.isdigit()])
    and any([le for le in word if le.isalpha()])
]

print(words)
