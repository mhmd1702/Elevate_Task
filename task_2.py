import tkinter as tk
from tkinter import filedialog, font

class SimpleTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad [MOHAMMAD]")

        # Create text area with scroll
        self.text_area = tk.Text(root, undo=True, wrap=tk.WORD)
        self.text_area.pack(fill=tk.BOTH, expand=1)

        # Create menu bar
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)

        # Format menu
        self.format_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)
        self.format_menu.add_command(label="Font", command=self.choose_font)

        #mhmd menu
        self.mhmd_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="MHMD", menu=self.mhmd_menu)
        self.mhmd_menu.add_command(label="Next future comming soon !")


        # Default font
        self.text_font = font.Font(family="Arial", size=12)
        self.text_area.configure(font=self.text_font)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        self.filename = filedialog.askopenfilename(defaultextension=".txt",
                                                   filetypes=[("All Files", "*.*"),
                                                              ("Text Files", "*.txt"),
                                                              ("Python Files", "*.py")])
        if self.filename:
            self.text_area.delete(1.0, tk.END)
            with open(self.filename, "r") as file:
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        if hasattr(self, 'filename'):
            with open(self.filename, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            self.save_as_file()

    def save_as_file(self):
        self.filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("All Files", "*.*"),
                                                                ("Text Files", "*.txt"),
                                                                ("Python Files", "*.py")])
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def choose_font(self):
        font_window = tk.Toplevel(self.root)
        font_window.title("Choose Font")
        tk.Label(font_window, text="Font Family:").grid(row=0, column=0)
        font_families = list(font.families())
        font_family = tk.StringVar(value=self.text_font.actual()["family"])
        font_family_menu = tk.OptionMenu(font_window, font_family, *font_families)
        font_family_menu.grid(row=0, column=1)

        tk.Label(font_window, text="Font Size:").grid(row=1, column=0)
        font_size = tk.IntVar(value=self.text_font.actual()["size"])
        font_size_spinbox = tk.Spinbox(font_window, from_=8, to=72, textvariable=font_size)
        font_size_spinbox.grid(row=1, column=1)

        tk.Button(font_window, text="Apply", command=lambda: self.apply_font(font_family.get(), font_size.get())).grid(row=2, column=0, columnspan=2)

    def apply_font(self, family, size):
        self.text_font.config(family=family, size=size)
        self.text_area.configure(font=self.text_font)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleTextEditor(root)
    root.mainloop()
