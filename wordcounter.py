import tkinter as tk
from tkinter import filedialog, messagebox

def count_words():
    text = text_area.get("1.0", tk.END).strip()
    if text:
        word_count = len(text.split())
        result_label.config(text=f"Word Count: {word_count}")
    else:
        messagebox.showinfo("Input Required", "Please enter some text to count words.")

def count_words_from_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                word_count = len(content.split())
                result_label.config(text=f"Word Count from File: {word_count}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while reading the file: {e}")
    else:
        messagebox.showinfo("No File Selected", "Please select a file to count words.")

# Create the main window
root = tk.Tk()
root.title("Interactive Word Counter")

# Text area for manual input
text_area = tk.Text(root, height=10, width=50, wrap=tk.WORD)
text_area.pack(pady=10)

# Button to count words in manual input
count_button = tk.Button(root, text="Count Words", command=count_words, bg="lightblue", fg="black")
count_button.pack(pady=5)

# Button to count words from file
file_button = tk.Button(root, text="Count Words from File", command=count_words_from_file, bg="lightgreen", fg="black")
file_button.pack(pady=5)

# Label to display the result
result_label = tk.Label(root, text="Word Count: 0", font=("Arial", 12))
result_label.pack(pady=10)

# Run the application
root.mainloop()
