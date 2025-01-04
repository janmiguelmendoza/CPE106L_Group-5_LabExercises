filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"File '{filename}' not found.")
    exit()

while True:
    print(f"The file contains {len(lines)} lines.")
    try:
        line_number = int(input("Enter a line number (0 to quit): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if line_number == 0:
        print("Exiting the program.")
        break
    elif 1 <= line_number <= len(lines):
        print(f"Line {line_number}: {lines[line_number - 1].strip()}")
    else:
        print(f"Invalid line number. Please enter a number between 1 and {len(lines)}.")

