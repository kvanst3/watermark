import tkinter
from tkinter import filedialog
import os.path

window = tkinter.Tk()
window.title("Watermarker")
window.minsize(width=500, height=500)
window.config(padx=10, pady=10)

# Title Label

label = tkinter.Label(text="Upload image", font=("Arial"))
label.grid(column=1, row=0)


# file explorer window

def browseFiles():
    file = filedialog.askopenfile(
        mode='rb',
        initialdir=os.path.expanduser('~/Pictures'),
        title="Select a File",
        filetypes=(
            ("Jpeg files", "*.jpeg*"),
            ("all files", "*.*")
        )
    )

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + os.path.basename(file.name))
    if file:
        data = file.read()
        file.close()
        print("I got %d bytes from this file." % len(data))




button = tkinter.Button(text="Browse", command=browseFiles)
button.grid(column=2, row=2, sticky='W')


# Result Label

label_file_explorer = tkinter.Label(text="*upload an image to appose a watermark", font="Arial")
label_file_explorer.grid(column=2, row=3)


window.mainloop()