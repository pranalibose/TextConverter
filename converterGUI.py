import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk

from tkinter.filedialog import askopenfile

window = tk.Tk()

window.title("Display Text from File")

logo = Image.open('cool-background.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1,row=0)

canvas = tk.Canvas(window, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)


text = tk.Label(window, text='Select a PDF file on your computer to extract all its text', font='Raleway')
text.grid(columnspan=3, column=0, row=1)

def open_file():
    txt.set("loading...")
    file = askopenfile(parent=window, mode='rb', title='Choose a file', filetype=[('Pdf file', '*.pdf')])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        #text_box
        text_box = tk.Text(window, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify='center')
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        txt.set("Browse")

txt = tk.StringVar()
button = tk.Button(window, textvariable=txt, command=lambda:open_file(), font='Raleway', bg='#20bebe', fg="white", height=2, width=15)
txt.set("Browse")
button.grid(column=1, row=2)

canvas = tk.Canvas(window, width=600, height=250)
canvas.grid(columnspan=3)

window.mainloop()