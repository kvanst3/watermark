import tkinter
from tkinter import filedialog
import os.path
from PIL import ImageTk, Image, ImageDraw, ImageFont

class WaterMarker():

    def __init__(self):
        self.img = None
        self.img_copy = None

        window = tkinter.Tk()
        window.title("Watermarker")
        window.minsize(width=500, height=500)
        window.config(padx=10, pady=10)


        # Title Label

        self.label_img_placeholder = tkinter.Label(text="Upload image", font=("Arial"))
        self.label_img_placeholder.grid(column=1, row=0)
         # File explorer Label

        self.label_file_explorer = tkinter.Label(text="*upload an image to appose a watermark", font="Arial")
        self.label_file_explorer.grid(column=2, row=3)

        # Browse Button

        self.browse_button = tkinter.Button(text="Browse", command=self.browseFiles)
        self.browse_button.grid(column=2, row=2, sticky='W')


        # Watermark Button

        self.wtmrk_button = tkinter.Button(text="Watermark it!", command=self.apply_watermark)

        # Watermark entry box

        self.wtmrk_text = tkinter.Entry(width=35)

        # Save Button

        self.save_button = tkinter.Button(text="Save", command=self.save_file)

        window.mainloop()



    # file explorer window

    def browseFiles(self):
        file_path = filedialog.askopenfilename(
            initialdir=os.path.expanduser('~/Pictures'),
            title="Select a File",
            filetypes=(
                ("Png files", "*.png*"),
                ("all files", "*.*")
            )
        )
        
        self.img = Image.open(file_path).convert("RGBA")
        self.display_image(self.img)

        # move stuff around, change labels name, etc

        self.label_img_placeholder.grid(columnspan=2)
        self.browse_button.grid(column=1, row=2)
        self.label_file_explorer.grid(column=2, row=2, sticky='E')
        self.label_file_explorer.config(text=os.path.basename(file_path))

        self.wtmrk_button.grid(column=2, row=3, sticky='e')
        self.wtmrk_text.grid(column=1, row=3, sticky='w', columnspan=2)


    def apply_watermark(self):
        
        self.img_copy = self.img.copy()
        width, height = self.img_copy.size

        draw = ImageDraw.Draw(self.img_copy)
        text = self.wtmrk_text.get()

        font = ImageFont.truetype('/usr/share/fonts/opentype/malayalam/Chilanka-Regular.otf', 26)
        textwidth, textheight = draw.textsize(text, font)

        # calculate the x,y coordinates of the text
        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin

        # draw watermark in the bottom right corner
        draw.text((x, y), text, font=font, fill=(255,255,255,150))

        self.display_image(self.img_copy)
        self.wtmrk_text.delete(0, 'end')
        self.save_button.grid(column=1, row=4, sticky='w')

    def display_image(self, img):
        display_img = ImageTk.PhotoImage(img)
        self.label_img_placeholder.config(image=display_img)
        self.label_img_placeholder.image = display_img

    def save_file(self):
        file = filedialog.asksaveasfile(mode='wb', defaultextension=".png")
        if file is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        self.img_copy.save(file)


wm = WaterMarker()
