import tkinter
from tkinter import filedialog
import os.path
from PIL import ImageTk, Image  

window = tkinter.Tk()
window.title("Watermarker")
window.minsize(width=500, height=500)
window.config(padx=10, pady=10)


# Title Label

label = tkinter.Label(text="Upload image", font=("Arial"))
label.grid(column=1, row=0)


# file explorer window

def browseFiles():
    file_path = filedialog.askopenfilename(
        # mode='rb',
        initialdir=os.path.expanduser('~/Pictures'),
        title="Select a File",
        filetypes=(
            ("Png files", "*.png*"),
            ("all files", "*.*")
        )
    )
    img = Image.open(file_path)
    display_image = ImageTk.PhotoImage(img)
    label.config(image=display_image)
    label.grid(columnspan=2)
    label.image = display_image
    button.grid(column=1, row=2)
    label_file_explorer.grid(column=2, row=2, sticky='E')
    label_file_explorer.config(text=os.path.basename(file))


#Browse Button

button = tkinter.Button(text="Browse", command=browseFiles)
button.grid(column=2, row=2, sticky='W')


# File explorer Label

label_file_explorer = tkinter.Label(text="*upload an image to appose a watermark", font="Arial")
label_file_explorer.grid(column=2, row=3)


window.mainloop()
