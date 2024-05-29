import os
import random
import string
from tkinter import filedialog, Tk, Button, Label

# Function to select a directory
def select_folder():
    global folder
    folder = filedialog.askdirectory()  # Open a dialog to select a directory
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]  # List all files in the directory
    num_files = len(files)  # Count the number of files
    folder_label.config(text=f"Selected folder: {folder}\nNumber of files: {num_files}")  # Update the label with the selected folder and number of files

# Function to rename files
def rename_files():
    try:
        for filename in os.listdir(folder):  # Iterate over all files in the directory
            if os.path.isfile(os.path.join(folder, filename)):  # If it's a file
                extension = os.path.splitext(filename)[1]  # Get the file extension
                new_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + extension  # Generate a new random name with the same extension
                os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))  # Rename the file
        folder_label.config(text="Files have been renamed")  # Update the label to indicate that the files have been renamed
    except Exception as e:
        folder_label.config(text=f"Error renaming files: {e}")  # If there's an error, update the label with the error message

root = Tk()
root.geometry("500x200")
root.title("File Renamer")

label = Label(root, text="Welcome to the File Renamer", font=("Arial", 20))
label.pack()

button1 = Button(root, text="Select folder", command=select_folder)  # Button to select a folder
button1.pack()

folder_label = Label(root, text="")
folder_label.pack()

button2 = Button(root, text="Rename files", command=rename_files)  # Button to rename files

button2.pack()
root.mainloop()  # Start the Tkinter event loop