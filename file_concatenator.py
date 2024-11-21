import tkinter as tk
from tkinter import filedialog, messagebox
import os
from gitignore_parser import parse_gitignore

class FileConcatenatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Concatenator")
        self.root.geometry("400x400")

        self.file_paths = []

        self.create_widgets()

    def create_widgets(self):
        self.import_button = tk.Button(self.root, text="Add Files", command=self.add_files)
        self.import_button.pack(pady=10)

        self.directory_button = tk.Button(self.root, text="Add Files from Directory", command=self.add_files_from_directory)
        self.directory_button.pack(pady=10)

        self.remove_button = tk.Button(self.root, text="Remove File", command=self.remove_file)
        self.remove_button.pack(pady=10)

        self.file_listbox = tk.Listbox(self.root, width=50, height=10)
        self.file_listbox.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_concatenation)
        self.start_button.pack(pady=10)

    def add_files(self):
        new_file_paths = filedialog.askopenfilenames(
            title="Select Files",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if new_file_paths:
            for file_path in new_file_paths:
                if file_path not in self.file_paths:
                    self.file_paths.append(file_path)
                    file_name = os.path.basename(file_path)
                    self.file_listbox.insert(tk.END, file_name)
            messagebox.showinfo("Files Added", f"{len(new_file_paths)} files added.")
        else:
            messagebox.showwarning("No Files Selected", "No files were selected.")

    def add_files_from_directory(self):
        selected_dir = filedialog.askdirectory(title="Select Directory")
        if not selected_dir:
            return

        gitignore_path = os.path.join(selected_dir, '.gitignore')
        if os.path.exists(gitignore_path):
            ignored = parse_gitignore(gitignore_path)
        else:
            ignored = lambda path: False

        exclude_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.pdf', '.zip', '.tar', '.gz'}

        added_files = []
        for root, dirs, files in os.walk(selected_dir):
            dirs[:] = [d for d in dirs if not ignored(os.path.join(root, d))]
            for file in files:
                file_path = os.path.join(root, file)
                if ignored(file_path):
                    continue
                _, ext = os.path.splitext(file_path)
                if ext.lower() in exclude_extensions:
                    continue
                if file_path in self.file_paths:
                    continue
                try:
                    with open(file_path, 'r') as f:
                        f.read()
                    self.file_paths.append(file_path)
                    file_name = os.path.basename(file_path)
                    self.file_listbox.insert(tk.END, file_name)
                    added_files.append(file_name)
                except PermissionError:
                    messagebox.showwarning("Permission Error", f"Cannot read {file_path}")

        if added_files:
            messagebox.showinfo("Files Added", f"{len(added_files)} files added from directory.")
        else:
            messagebox.showwarning("No Files Added", "No files were added from the selected directory.")

    def remove_file(self):
        selected_indices = self.file_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("No File Selected", "Please select a file to remove.")
            return

        for index in reversed(selected_indices):
            self.file_paths.pop(index)
            self.file_listbox.delete(index)
        messagebox.showinfo("File Removed", "Selected file(s) removed.")

    def start_concatenation(self):
        if not self.file_paths:
            messagebox.showwarning("No Files Selected", "Please add files first.")
            return

        output_content = []
        for file_path in self.file_paths:
            with open(file_path, 'r') as file:
                output_content.append(file.read())
            output_content.append("\n" + "-" * 40 + "\n")  # Add separator line

        output_file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if output_file_path:
            with open(output_file_path, 'w') as output_file:
                output_file.write("\n".join(output_content))
            messagebox.showinfo("Concatenation Complete", f"Files concatenated and saved to {output_file_path}")
        else:
            messagebox.showwarning("No Output File Selected", "Concatenation aborted.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileConcatenatorApp(root)
    root.mainloop()