
lines = []

while True:
    line = input("Enter a line (or leave empty to finish): ")
    if line == "":
        break
    lines.append(line)

print("\nLines entered:")
for line in lines:
    print(line)
