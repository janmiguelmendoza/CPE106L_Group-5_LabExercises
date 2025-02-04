import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            text_widget.delete("1.0", tk.END)  # Clear previous text
            text_widget.insert(tk.END, content)  # Display file content

# Create the main GUI window
root = tk.Tk()
root.title("File Opener")

# Create and place the button
open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(pady=10)

# Create a text widget to display file content
text_widget = tk.Text(root, wrap="word", height=20, width=60)
text_widget.pack(padx=10, pady=10)

# Run the GUI event loop
root.mainloop()

