def if_prompt_has_digits():
    prompt = input("Please enter prompt: ")
    for char in prompt:
        if char.isdigit():
            return True
    return False


print(if_prompt_has_digits())
