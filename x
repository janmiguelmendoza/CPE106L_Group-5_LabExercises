Programming exercise no 2

def navigatefile():
    try:
        filename = input("Enter the filename: ")
        with open(filename, 'r') as file:
            lines = file.readlines()

        linecount = len(lines)
        print(f"The file has {linecount} lines. Enter 0 to quit.")

  while True:
            try:
                linenumber = int(input(f"Enter a line number (1-{line_count}): "))

                if line_number == 0:
                    print("Exiting program.")
                    break
                elif 1 <= line_number <= line_count:
                    print(f"Line {line_number}: {lines[line_number - 1].strip()}")
                else:
                    print(f"Invalid line number. Please enter a number between 1 and {line_count}.")
            except ValueError:
                print("Please enter a valid integer.")
