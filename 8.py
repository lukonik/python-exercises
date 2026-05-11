prompt = input("add nominator/denominator: ")
nominator, denominator = prompt.split("/")

result = int(nominator)/int(denominator) * 100

print(f"The result is: {result:.2f}")