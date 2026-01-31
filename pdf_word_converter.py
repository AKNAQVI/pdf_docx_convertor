import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2docx import Converter
from docx2pdf import convert
import os

# File open karne ke liye dialog box dikhana
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("Word files", "*.docx")])
    return file_path

# PDF ko DOCX mein convert karne ka function
def pdf_to_doc():
    pdf_file = open_file()  # File select karwana
    if pdf_file:
        docx_file = pdf_file.replace(".pdf", ".docx")  # PDF ko DOCX mein convert karna
        try:
            # pdf2docx library ka use kar ke PDF ko DOCX mein convert karna
            converter = Converter(pdf_file)
            converter.convert(docx_file, start=0, end=None)  # PDF ko DOCX mein convert karna
            converter.close()
            messagebox.showinfo("Success", f"File successfully converted! Saved as {docx_file}")  # Success message
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during conversion: {e}")  # Agar error ho toh message

# DOCX ko PDF mein convert karne ka function
def doc_to_pdf():
    docx_file = open_file()  # File select karwana
    if docx_file:
        try:
            # docx2pdf library ka use kar ke DOCX ko PDF mein convert karna
            convert(docx_file)
            messagebox.showinfo("Success", f"File converted successfully!")  # Success message
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during conversion: {e}")  # Agar error ho toh message

# Main window create karna
root = tk.Tk()
root.title("PDF to Word Converter")  # Window ka title set karna
root.geometry("400x200")  # Window ka size set karna
root.config(bg="light Blue")  # Background color set karna

# Logo ko display karna (assuming logo file 'szabist-logo.png' ke naam se hai)
logo = tk.PhotoImage(file="szabist-logo.png")
logo = logo.subsample(3, 3)  # Logo ko thoda chhota karna
logo_label = tk.Label(root, image=logo, bg="light Blue")  # Logo ko label mein rakhna
logo_label.place(relx=0.23, rely=0.5, anchor="center")  # Logo ki position set karna

# Title ko screen ke center mein dikhana
title_label = tk.Label(
    root, 
    text="QuickConvert",  # Title ka text
    font=("Arial Black", 28, "bold italic"),  # Font style
    fg="Black", 
    bg="light Blue"
)
title_label.place(relx=0.5, rely=0.3, anchor="center")  # Title ki position set karna

# Rounded buttons create karne ka function
def create_button(text, command, x, y):
    return tk.Button(
        root, 
        text=text,  # Button ka text
        command=command,  # Button click hone par function call hona
        bg="blue", 
        fg="white", 
        font=("Arial", 12, "bold"), 
        relief="groove", 
        bd=0, 
        width=18, 
        height=2
    ).place(relx=x, rely=y, anchor="center")  # Button ki position set karna

# PDF to DOCX button create karna
create_button("PDF to DOCX", pdf_to_doc, 0.5, 0.5)

# DOCX to PDF button create karna
create_button("DOCX to PDF", doc_to_pdf, 0.5, 0.6)

# Exit button jo app ko band kare
exit_button = tk.Button(
    root, 
    text="Exit",  # Exit button ka text
    command=root.quit,  # App band karne ke liye command
    bg="dark red", 
    fg="white", 
    font=("Arial", 12, "bold"), 
    relief="ridge", 
    bd=3,
    width=10, 
    height=1
)
exit_button.place(relx=0.9, rely=0.9, anchor="center")  # Exit button ki position set karna

# Footer mein "Made by Ali Kamal" likhna
footer_label = tk.Label(root, text="Made by Ali Kamal", font=("Arial", 12), fg="black", bg="light Blue")
footer_label.place(relx=0.5, rely=0.95, anchor="center")  # Footer ki position set karna

# Main event loop chalana
root.mainloop()
