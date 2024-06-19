
mainstring = input("Enter the main string: ")
substring = input("Enter the substring to check: ")

if substring in mainstring:
    print(f"The substring '{substring}' is present in the main string.")
else:
    print(f"The substring '{substring}' is not present in the main string.")
