"""
This program writes pictures to a pdf.

Running the program will launch tkinter file dialogs to get a path to images you want converted to a pdf. 

    - Images must be vertically oriented 
    - Images must be stored in the order you want written
    - Only works with png, jpg, and jpeg currently 


This was just a quick and dirty solution becuase my computers pdf printer driver was corrupted and I couldn't 
be bothered to figure that one out. 

"""

from PIL import Image
from os import listdir, getcwd
from os.path import join
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw() #hide the tkinter window

# Select folder with all the pictures in order you want stored
files_path = filedialog.askdirectory(initialdir = getcwd(), title = "Select Files")
# save as a pdf
outfile = filedialog.asksaveasfilename(initialdir = getcwd(),initialfile='output.pdf' ,title = "Save As", filetypes = (("pdf", "*.pdf*"), ("all files", "*.*")))

if not outfile.endswith('.pdf'):
    outfile += '.pdf'

# get the path for all the images 
images = [join(files_path, f) for f in listdir(files_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# have to create a starting image to append the rest of the images to 
start = Image.open(images.pop(0)).rotate(-90, expand=True).convert('RGB')
others = [Image.open(img).rotate(-90, expand=True).convert('RGB') for img in images]

start.save(fp=outfile, save_all=True, append_images=others)
