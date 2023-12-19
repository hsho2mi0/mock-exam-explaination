import tkinter as tk
import os
import webbrowser

def open_pdf(event=None):  # 'event' parameter is for the Enter key binding
    # Extracting values from the single entry field
    input_text = input_entry.get()
    parts = input_text.split()

    # Determine if 's' is provided
    if len(parts) == 3:
        yy, g, mm = parts
        s = ""
    elif len(parts) == 4:
        yy, g, mm, s = parts
    else:
        # If the input format is incorrect, show an error message
        status_label.config(text="Invalid input. Format: yy g mm [s]")
        return

    # Constructing the file path
    file_path = os.path.join(g, yy, mm, f"{yy}{g}{mm}{s}.pdf")

    # Check if the file exists
    if os.path.exists(file_path):
        # Open the pdf file
        webbrowser.open_new(file_path)
    else:
        # Update the status label if the file does not exist
        status_label.config(text="File does not exist.")

# Create the main window
root = tk.Tk()
root.title("모의고사 해설지 Finder")

# Configure grid rows and columns
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

# Create and grid the label, entry, and button
tk.Label(root, text="연도, 학년, 달, [과목]을 다음과 같은 형태로 입력하시오. (yy g mm [s]):").grid(row=0, column=0)
input_entry = tk.Entry(root)
input_entry.grid(row=0, column=1, sticky='w', padx=(10, 10))
input_entry.bind("<Return>", open_pdf)  # Bind the Enter key to the open_pdf function

open_button = tk.Button(root, text="Open PDF", command=open_pdf)
open_button.grid(row=0, column=2, sticky='w', padx=(0, 10))


# Status label
status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=2)

# Copyright label
copyright_label = tk.Label(root, text="이 프로그램에 대한 모든 저작권은 한신희에게 있습니다.")
copyright_label.grid(row=3, column=2, sticky='se')

# Run the application
root.mainloop()
