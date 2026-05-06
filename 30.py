def frequenecy_count(text: str):
    return {word: text.count(word) for word in text.split()}


print(frequenecy_count("apple banana apple cherry banana apple"))