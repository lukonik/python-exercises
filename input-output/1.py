def multiply():
    prompt = input("Enter two value: a-b")
    a, b = [int(value) for value in prompt.split("-")]
    return a * b


print(multiply())
