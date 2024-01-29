# Dev_@ladinh production
# text_editor app, this app mainly entails a typical text editor app which you can use to write and store your data inform of notes

import tkinter as tk
from tkinter import filedialog
import os

current_file = None

def new_file():
    text.delete("1.0", tk.END)
    global current_file
    current_file = None
    
def exit_app():
    root.destroy()
    
def save_file():
    global current_file
    if current_file:
        with open(current_file, "w") as file:
            file.write(text.get("1.0", tk.END))
        root.title(f"Text Editor - {current_file}")
    else:
        save_file_as()
        
def save_file_as():
    global current_file
    initial_dir = "E:/Denno/DNI Documents/my text editor notes"
    file_path = filedialog.asksaveasfilename(initialdir=initial_dir, defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get("1.0", tk.END))
        root.title(f"Text Editor - {file_path}")
        current_file = file_path
        
def open_file():
    global current_file
    initial_dir = "E:/Denno/DNI Documents/my text editor notes"
    file_path = filedialog.askopenfilename(initialdir=initial_dir, defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text.delete("1.0", tk.END)
            text.insert(tk.END, file.read())
        root.title(f"Text Editor - {file_path}")
        current_file = file_path
        
def delete_file():
    global current_file
    if current_file and os.path.exists(current_file):
        os.remove(current_file)
        new_file()
        root.title("Text Editor")
    else:
        print("No note file to delete.")

root = tk.Tk()
root.geometry('550x500')
root.resizable(False, False)
root.config(bg="pink")
root.title(" Dev_@ladinh production                     Note Editor App")

text = tk.Text(root, wrap="word", width=50, height=80)
text.pack(side=tk.RIGHT, padx=5, pady=5)

exit_button = tk.Button(root, text="\n    EXIT   ", command=exit_app, bg="green")
exit_button.place(x=50, y=450)

new_window_button = tk.Button(root, text=" New Note \nWindow   ", command=new_file, bg="yellow")
new_window_button.place(x=10, y=10)

save_file_button = tk.Button(root, text="  \nSave the Note ", command=save_file, bg="green")
save_file_button.place(x=10, y=60)

open_file_button = tk.Button(root, text="  \nOpen a file Note   ", command=open_file, bg="green")
open_file_button.place(x=10, y=110)

delete_file_button = tk.Button(root, text="  \nDelete the    \Note   ", command=delete_file, bg="green")
delete_file_button.place(x=10, y=160)

root.mainloop()
