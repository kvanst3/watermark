import tkinter
from tkinter import filedialog
import os.path
from PIL import ImageTk, Image, ImageDraw, ImageFont

IMG = None

window = tkinter.Tk()
window.title("Watermarker")
window.minsize(width=500, height=500)
window.config(padx=10, pady=10)


# Title Label

label_img_placeholder = tkinter.Label(text="Upload image", font=("Arial"))
label_img_placeholder.grid(column=1, row=0)


# file explorer window

def browseFiles():
    file_path = filedialog.askopenfilename(
        initialdir=os.path.expanduser('~/Pictures'),
        title="Select a File",
        filetypes=(
            ("Png files", "*.png*"),
            ("all files", "*.*")
        )
    )
    global IMG
    IMG = Image.open(file_path).convert("RGBA")
    display_image()

    # move stuff around, change labels name, etc

    label_img_placeholder.grid(columnspan=2)
    browse_button.grid(column=1, row=2)
    label_file_explorer.grid(column=2, row=2, sticky='E')
    label_file_explorer.config(text=os.path.basename(file_path))

    wtmrk_button.grid(column=2, row=3, sticky='e')
    wtmrk_text.grid(column=1, row=3, sticky='w', columnspan=2)


def apply_watermark():
    width, height = IMG.size

    draw = ImageDraw.Draw(IMG)
    text = wtmrk_text.get()

    font = ImageFont.truetype('/usr/share/fonts/opentype/malayalam/Chilanka-Regular.otf', 26)
    textwidth, textheight = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font, fill=(255,255,255,150))

    display_image()
    save_button.grid(column=1, row=4, sticky='w')

def display_image():
    display_img = ImageTk.PhotoImage(IMG)
    label_img_placeholder.config(image=display_img)
    label_img_placeholder.image = display_img

def save_file():
    file = filedialog.asksaveasfile(mode='wb', defaultextension=".png")
    if file is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    IMG.save(file)

# File explorer Label

label_file_explorer = tkinter.Label(text="*upload an image to appose a watermark", font="Arial")
label_file_explorer.grid(column=2, row=3)

# Browse Button

browse_button = tkinter.Button(text="Browse", command=browseFiles)
browse_button.grid(column=2, row=2, sticky='W')


# Watermark Button

wtmrk_button = tkinter.Button(text="Watermark it!", command=apply_watermark)

# Watermark entry box

wtmrk_text = tkinter.Entry(width=35)

# Save Button

save_button = tkinter.Button(text="Save", command=save_file)

window.mainloop()
