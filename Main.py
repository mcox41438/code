import tkinter as tk
import os
import sys
import openpyxl
import csv
import xml.etree.ElementTree as ET
from tkinter import filedialog
from PIL import Image, ImageTk

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class MyCustomWindow(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        tk.Label(self, image= img).pack()
        self.pack(side='top')
    def set(window, title, icon_path= None):
        window.title(title)
        window.geometry('550x550')
        if icon_path:
            window.iconbitmap(icon_path)
    def button(window, texti, command1):
        button1 = tk.Button(window, text=texti, command=command1)
        button1.pack()
    def label(window, texti):
        label = tk.Label(window, text=texti)
        label.pack()
    def entry(window, text, command):
        MyCustomWindow.button(window, text, command)
        

class file():
    def browse_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            file.parse_file(file_path)
    def parse_file(file_path):
    # Determine the file extension
        file_extension = os.path.splitext(file_path)[1].lower()
        if file_extension == '.xml':
            file.parse_xml_file(file_path)
        elif file_extension == '.txt':
            file.parse_text_file(file_path)
        elif file_extension == '.xlsx':
            file.parse_excel_file(file_path)
        elif file_extension == '.ifix':
            file.parse_ifix_file(file_path)
        elif file_extension == '.csv':
            file.parse_csv_file(file_path)
        else:
            print("Unsupported file format")
    def parse_xml_file(file_path):
    # Implement XML parsing logic here
        print("Parsing XML file:", file_path)
        tree = ET.parse(file_path)
        root = tree.getroot()
        for child in root:
            print(child.tag, child.attrib, child.text)
    def parse_text_file(file_path):
    # Implement text file parsing logic here
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip()) 
    def parse_excel_file(file_path):
        # Implement Excel file parsing logic here
        print("Parsing Excel file:", file_path)
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        for row in sheet.iter_rows(values_only=True):
            print(row)
        wb.close()
    def parse_ifix_file(file_path):
        # Implement iFix file parsing logic here
        print("Parsing iFix file:", file_path)
        #/*/*//*//*/*//**/add more to actually read file**//*//*/*/*/
    def parse_csv_file(file_path):
    # Implement iFix file parsing logic here
        print("Parsing CSV file:", file_path)
        with open(file_path, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                print(row)

#class cad():
    #def 
                
def open_window1():
    window1 = tk.Toplevel(root)
    MyCustomWindow(window1)
    MyCustomWindow.set(window1, "Window 1", icon)
    MyCustomWindow.label(window1, "This is Window 1")
    MyCustomWindow.button(window1, "Pick File", file.browse_file)

def open_window2():
    window2 = tk.Toplevel(root)
    MyCustomWindow(window2)
    MyCustomWindow.set(window2, "Window 2", icon)
    MyCustomWindow.label(window2, "This is Window 2")
    MyCustomWindow.button(window2, "Pick File", file.browse_file)

def open_window3():
    window3 = tk.Toplevel(root)
    MyCustomWindow(window3)
    MyCustomWindow.set(window3, "Window 3", icon)
    MyCustomWindow.label(window3, "This is Window 3")

def create_help_window():
    help_window = tk.Toplevel(root)
    help_window.overrideredirect(True)  # Remove window border
    help_window.geometry('200x200')

def main():
    global root, icon, img
    root = tk.Tk()
    image1_path = resource_path("logo.png")
    icon = resource_path("OIP.ico")
    img= tk.PhotoImage(file= image1_path)
    MyCustomWindow(root)
    MyCustomWindow.set(root, "Engineer's Assistant", icon)
    MyCustomWindow.label(root, "Pick What You Need Done.")
    MyCustomWindow.button(root, "Graphics", open_window1)
    MyCustomWindow.button(root, "CAD TOOLS", open_window2)
    MyCustomWindow.button(root, "Open Window 3", open_window3)
    root.mainloop()

if __name__ == "__main__":
    main()
