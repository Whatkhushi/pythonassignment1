user_input = input("Enter a string: ")
file_name = "output.txt"

with open(file_name, "w") as file:
    file.write(user_input)

print(f"The string has been written to {file_name}.")