prompt = input("""
    Choose the option:
    1. Say Hello
    2. Calculate Square
    3. Exit
 """)

match prompt:
    case "1":
        print("Hello")
    case "2":
        square_prompt = input("Enter square radius")
        print(f"The square is {float(square_prompt) * 2}")
    case "3":
        print("Goodbye")
