from tkinter import *
from tkinter import ttk
from colors import *
import barcode_excel_gen
import word_gen
from tkinter import filedialog


# C:\Users\Роман\PycharmProjects\barcode\report_2022_3_10.xlsx
def generate_excel_barcodes():

    global filename, ext, loading, window2

    directory, path, filename, ext = barcode_excel_gen.pathSplit(full_path)

    if ext == '.xlsx':
        # Окно с выбором типа
        window2 = Tk()
        window2.title("Choose ean13 or code128 to generate")
        window2.config(bg=LIGHT_GRAY)

        frame2_1 = Frame(window2)
        frame2_1.grid(row=0, column=0)
        frame2_2 = Frame(window2)
        frame2_2.grid(row=1, column=0)

        txt2 = Label(frame2_1, text='Choose the type of the barcode')
        txt2.grid(row=0, column=0, sticky=SE)
        b_ean13 = Button(frame2_2, text='ean13', command=gen_ean13,
                         width=10, height=5, bg=DARK_GRAY, foreground=WHITE)
        b_ean13.grid(column=0, row=1, padx=2.5, pady=2.5)
        b_code128 = Button(frame2_2, text='code128', command=gen_code128,
                           width=10, height=5, bg=DARK_GRAY, foreground=WHITE)
        b_code128.grid(column=1, row=1, padx=2.5, pady=2.5)

        window2.mainloop()
    else:
        status(2, alarm='Wrong file format. Should be .xlsx')


def generate_docx():
    global window3, country_en, firm_en, year_en

    window3 = Tk()
    window3.title("Enter values")
    window3.config(bg=LIGHT_GRAY)

    frame3 = Frame(window3, width=120, height=1200, bg=LIGHT_GRAY)
    frame3.grid(row=0, column=0, padx=10, pady=5)

    frame4 = Frame(window3, width=120, height=30, bg=LIGHT_GRAY)
    frame4.grid(row=1, column=0, padx=10, pady=5)

    # Страна производства
    country_lab = Label(frame3, text='Страна производства', width=25, borderwidth=1)
    country_lab.grid(row=0, column=0, padx=2.5, pady=2.5)
    country_en = Entry(frame3, width=40)
    country_en.grid(row=0, column=1)
    # Производитель
    firm_lab = Label(frame3, text='Производитель', width=25, borderwidth=1)
    firm_lab.grid(row=1, column=0, padx=2.5, pady=2.5)
    firm_en = Entry(frame3, width=40)
    firm_en.grid(row=1, column=1)
    # Год производства
    year_lab = Label(frame3, text='Дата производства', width=25, borderwidth=1)
    year_lab.grid(row=2, column=0, padx=2.5, pady=2.5)
    year_en = Entry(frame3, width=40)
    year_en.grid(row=2, column=1)
    # Apply changes button
    b4 = Button(frame4, text='Apply settings', command=genStart)
    b4.grid(column=0, row=0, sticky=SE)


def genStart():
    status(4)

    country = country_en.get()
    firm = firm_en.get()
    year = year_en.get()

    al = word_gen.gen_word(full_path, country, firm, year)
    if al != None:
        status(2, alarm=al)
    else:
        status(5)
    window3.destroy()


def gen_ean13():
    barcode_excel_gen.gen_excel(full_path, 'ean13')
    status(1)
    window2.destroy()


def gen_code128():
    barcode_excel_gen.gen_excel(full_path, 'code128')
    status(1)
    window2.destroy()


def reset():
    status(0)
    tit.configure(text='')


def status(num=0, *percent, **alarm):
    if num == 0:
        sts.configure(bg=YELLOW, text='IDLE')
    elif num == 1:
        sts.configure(bg=LIGHT_GREEN, text='.xlsx gen is complete')
        progress.pack_forget()
    elif num == 2:
        sts.configure(bg=RED, text=str(alarm))
    elif num == 3:
        sts.configure(bg=LIGHT_GRAY, text='')
        progress.pack()
        progress['value'] = percent
        window.update_idletasks()
    elif num == 4:
        sts.configure(bg=YELLOW, text='.docx gen in progress')
    elif num == 5:
        sts.configure(bg=LIGHT_GREEN, text='.docx gen is complete')
    elif num == 6:
        sts.configure(bg=YELLOW, text='File found. Choose a method to be applied')
    else:
        sts.configure(bg=YELLOW, text='IDLE')


def create_circle(x, y, r, canvasName):
    x0 = x-r
    y0 = y-r
    x1 = x+r
    y1 = y+r
    return canvasName.create_oval(x0, y0, x1, y1, fill='green')


def browse_file():
    global full_path
    full_path = filedialog.askopenfilename(filetypes=(("Excel file", "*.xlsx"), ("All files", "*")))
    directory, path, file, ext = barcode_excel_gen.pathSplit(full_path)
    res = 'File: {}'.format(path)
    tit.configure(text=res)
    status(6)


def clicker():
    # Creating window
    global window, txt, tit, sts, progress
    window = Tk()
    window.title("Wildberries Code128 generator ver.7")
    window.geometry('1200x160')
    window.config(bg=LIGHT_GRAY)

    ### User interface here ###

    # Общий фрейм
    UI_frame = Frame(window, width=1200, height=120, bg=LIGHT_GRAY)
    UI_frame.grid(row=0, column=0, padx=10, pady=5)

    # Фрейм с лейблом
    label_frame = Frame(UI_frame, width=1200, height=40, bg=LIGHT_GRAY)
    label_frame.grid(row=0, column=0, padx=10, pady=5)
    # Author
    lbl = Label(label_frame, text='Wildberries Code128 generator ver.7 \n'
                             'Author: Rumiantcev Roman', bg=LIGHT_GRAY)
    lbl.grid(row=0, column=0, sticky=E)

    # Фрейм с статусом
    status_frame = Frame(UI_frame, width=1200, height=40, bg=LIGHT_GRAY)
    status_frame.grid(row=1, column=0, padx=20, pady=10)
    # Programm status
    sts = Label(window, text='Status of the APP')
    sts.grid(row=0, sticky=W+E)

    # Loading line
    progress = ttk.Progressbar(sts, orient=HORIZONTAL, length=1200, mode='determinate')

    # Фрейм с путем и генерацией
    path_frame = Frame(UI_frame, width=1200, height=40, bg=LIGHT_GRAY)
    path_frame.grid(row=3, column=0, padx=30, pady=15)

    # Reset button
    b_reset = Button(path_frame, text='RESET', command=reset)
    b_reset.grid(column=0, row=0, sticky=W, padx=2.5)
    # Search button
    search = Button(path_frame, text='Search', command=browse_file)
    search.grid(row=0, column=1, padx=2.5)
    # Entered path
    tit = Label(path_frame, bg=WHITE, width=60, text='Your file', borderwidth=2)
    tit.grid(row=0, column=2, padx=2.5)
    # Start excel_main()
    b1 = Button(path_frame, text='Generate barcodes', command=generate_excel_barcodes, bg=WHITE, width=15)
    b1.grid(row=0, column=3, padx=2.5)
    # Start word_main()
    b3 = Button(path_frame, text='Generate docx', command=generate_docx, bg=WHITE, width=15)
    b3.grid(row=0, column=4, padx=2.5)

    # create_circle(225, 100, 50, myCanvas)
    # myCanvas.create_text(225, 100, text='HELLO', fill=BLACK)

    window.mainloop()


clicker()
