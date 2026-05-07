def cap_first_letter(text: str):
    output = [text[0].upper()]
    output.extend(text[1:])
    return "".join(output)


print(cap_first_letter("hello world from python"))
