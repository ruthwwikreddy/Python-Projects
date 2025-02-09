import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

# Define the main window
root = tk.Tk()
root.title("YOUR AI ASSISTANT")

# Adding a background color to the window
root.configure(bg='steelblue')

# Define the function to automate YouTube search
def search_youtube():
    query = entry.get()
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

# Define the function to automate Google search
def search_google():
    query = entry.get()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

# Define the function to automate Instagram search
def search_instagram():
    username = entry.get().replace('@', '')  # Ensure username is clean of '@'
    url = f"https://www.instagram.com/{username}/"
    webbrowser.open(url)

# Create input field, labels, and buttons with background colors
Label(root, text="Enter your command:", bg='lightblue', font=("Helvetica", 12)).pack(pady=10)
entry = Entry(root, width=50)
entry.pack(pady=10)

Button(root, text="Search on YouTube", command=search_youtube, bg='red', fg='white').pack(pady=5)
Button(root, text="Search on Google", command=search_google, bg='green', fg='white').pack(pady=5)
Button(root, text="Search on Instagram", command=search_instagram, bg='purple', fg='white').pack(pady=5)

# Run the main loop
root.mainloop()
