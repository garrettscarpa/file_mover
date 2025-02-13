import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to transfer the file/folder
def transfer_large_file_or_folder(src, dst):
    if not os.path.exists(src):
        messagebox.showerror("Error", f"Source {src} does not exist.")
        return

    if os.path.isfile(src):
        try:
            shutil.move(src, dst)
            messagebox.showinfo("Success", f"File {src} has been moved to {dst}.")
        except Exception as e:
            messagebox.showerror("Error", f"Error while moving file: {e}")
    
    elif os.path.isdir(src):
        try:
            shutil.move(src, dst)
            messagebox.showinfo("Success", f"Directory {src} has been moved to {dst}.")
        except Exception as e:
            messagebox.showerror("Error", f"Error while moving directory: {e}")
    else:
        messagebox.showerror("Error", "Source is neither a file nor a directory.")

# Function to open a file/folder dialog and set the source path
def browse_src():
    src_path = filedialog.askopenfilename(title="Select Source File")  # For file selection
    if src_path:
        src_entry.delete(0, tk.END)  # Clear the current text
        src_entry.insert(0, src_path)  # Insert the selected path

def browse_dst():
    dst_path = filedialog.askdirectory(title="Select Destination Folder")  # For folder selection
    if dst_path:
        dst_entry.delete(0, tk.END)  # Clear the current text
        dst_entry.insert(0, dst_path)  # Insert the selected path

# Function that triggers the transfer when button is clicked
def start_transfer():
    src = src_entry.get()
    dst = dst_entry.get()

    if not src or not dst:
        messagebox.showerror("Error", "Please specify both source and destination paths.")
        return

    transfer_large_file_or_folder(src, dst)

# Create the main window
root = tk.Tk()
root.title("File/Folder Transfer Tool")

# Create and place labels, entries, and buttons
src_label = tk.Label(root, text="Source File/Folder:")
src_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

src_entry = tk.Entry(root, width=50)
src_entry.grid(row=0, column=1, padx=10, pady=10)

src_button = tk.Button(root, text="Browse", command=browse_src)
src_button.grid(row=0, column=2, padx=10, pady=10)

dst_label = tk.Label(root, text="Destination Folder:")
dst_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

dst_entry = tk.Entry(root, width=50)
dst_entry.grid(row=1, column=1, padx=10, pady=10)

dst_button = tk.Button(root, text="Browse", command=browse_dst)
dst_button.grid(row=1, column=2, padx=10, pady=10)

transfer_button = tk.Button(root, text="Transfer", command=start_transfer)
transfer_button.grid(row=2, column=1, padx=10, pady=20)

# Start the GUI event loop
root.mainloop()
