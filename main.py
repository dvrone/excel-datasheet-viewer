from tkinter import *
from tkinter import filedialog, messagebox, ttk

import pandas as pd

root = Tk()
root.title("Excel DataSheet Viewer")
root.geometry("1140x500+200+200")


# Open Excel file
def open_file():
    filename = filedialog.askopenfilename(
        title="Select an Excel File",
        filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")],
    )

    if not filename:
        return

    try:
        df = pd.read_excel(filename)
    except Exception as e:
        messagebox.showerror("Error", f"Unable to open this file!\n\n{e}")
        return

    # Clear previous data
    tree_view.delete(*tree_view.get_children())

    # Configure columns
    tree_view["columns"] = list(df.columns)
    tree_view["show"] = "headings"

    for col in df.columns:
        tree_view.heading(col, text=col)
        tree_view.column(col, width=120, minwidth=80, anchor="center")

    # Insert data
    for _, row in df.iterrows():
        tree_view.insert("", "end", values=list(row))


# Icon
try:
    icon = PhotoImage(file="excel-file.png")
    root.iconphoto(False, icon)
except TclError:
    pass

# Main frame
frame = Frame(root)
frame.pack(fill="both", expand=True, padx=10, pady=15)

# Table and scrollbars
table_frame = Frame(frame)
table_frame.pack(fill="both", expand=True)

tree_view = ttk.Treeview(table_frame)

scroll_y = ttk.Scrollbar(table_frame, orient="vertical", command=tree_view.yview)
scroll_x = ttk.Scrollbar(table_frame, orient="horizontal", command=tree_view.xview)

tree_view.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

tree_view.grid(row=0, column=0, sticky="nsew")
scroll_y.grid(row=0, column=1, sticky="ns")
scroll_x.grid(row=1, column=0, sticky="ew")

table_frame.rowconfigure(0, weight=1)
table_frame.columnconfigure(0, weight=1)

# Open button
btn_open = Button(
    root,
    text="Open Excel File",
    width=25,
    height=2,
    font=("Arial", 12),
    bg="#0078D7",
    fg="#FFFFFF",
    command=open_file,
)
btn_open.pack(pady=(0, 15))

root.mainloop()
