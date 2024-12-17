Programming exercise no 2

def navigatefile():
    try:
        filename = input("Enter the filename: ")
        with open(filename, 'r') as file:
            lines = file.readlines()

        linecount = len(lines)
        print(f"The file has {linecount} lines. Enter 0 to quit.")
