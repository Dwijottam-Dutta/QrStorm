import qrcode
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk import Progressbar
import time
import os

file = ""
path = ""
textarea = None
filearea = None
root = None
window = None
filepath = None
w = ''
progress = {}


# ######################################Startup#################################
def startup_screen():
    startup()
    bar()
    bar_two()
    w.destroy()


def default_bar():
    global w
    a = 'light green'
    l4 = Label(w, text='Software developed by Dwijottam Dutta', fg='white', bg=a)
    lst4 = ('Calibri (Body)', 9)
    l4.config(font=lst4)
    l4.place(x=10, y=210)
    import time
    r = 0
    for i in range(110):
        progress['value'] = r
        w.update_idletasks()
        time.sleep(0.00001)
        r = r + 1


def bar():
    global w
    a = '#E99497'
    l4 = Label(w, text='Software developed by Dwijottam Dutta', fg='white', bg=a)
    lst4 = ('Calibri (Body)', 9)
    l4.config(font=lst4)
    l4.place(x=10, y=210)
    import time
    r = 0
    for i in range(110):
        progress['value'] = r
        w.update_idletasks()
        time.sleep(0.05)
        r = r + 1


def bar_two():
    global l4
    global w
    r = 0
    for i in range(100):
        progress['value'] = r
        w.update_idletasks()
        time.sleep(0.02)
        r = r + 1


def startup():
    global w
    global progress
    w = Tk()
    width_of_window = 427
    height_of_window = 250
    screen_width = w.winfo_screenwidth()
    screen_height = w.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (width_of_window / 2)
    y_coordinate = (screen_height / 2) - (height_of_window / 2)
    w.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

    w.overrideredirect(1)

    s = ttk.Style()
    s.theme_use('clam')
    s.configure("red.Horizontal.TProgressbar", foreground='light green', background='#D83A56')
    progress = Progressbar(w, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=500, mode='determinate')

    progress.place(x=-10, y=235)
    default_bar()

    a = '#E99497'
    Frame(w, width=427, height=241, bg="#E99497").place(x=0, y=0)  # 249794

    l1 = Label(w, text='QrStorm 3.0.1', fg='white', bg=a)
    lst1 = ('System', 30, 'bold')
    l1.config(font=lst1)
    l1.place(x=30, y=70)

    l3 = Label(w, text='Simple QrCode Maker, written in Python', fg='white', bg=a)
    lst3 = ('System', 15)
    l3.config(font=lst3)
    l3.place(x=30, y=120)
    
# ##############################################################################


# Funtion which opens the about in which about us is described
def aboutmore():
    aboutus = Tk()
    aboutus.configure(background="#66DE93")
    aboutus.title(" About QrStorm")
    aboutus.geometry("340x190")
    aboutus.iconbitmap("./assets/qr-code.ico")
    aboutus.resizable(0, 0)
    # Label(aboutus, text='''About''', bg='#10caeb', font=('System', 18, 'bold')).place(x=5, y=10)
    Label(aboutus, text='''QrStorm is Simple Qr Code Maker by''', bg='#66DE93', font=('System', 17, 'bold')).place(x=5,
                                                                                                                   y=20)
    Label(aboutus, text='''which you can make Qr Code for free ''', bg='#66DE93', font=('System', 17, 'bold')).place(
        x=5, y=50)
    Label(aboutus, text='''also without any Account or Log in''', bg='#66DE93', font=('System', 17, 'bold')).place(x=5,
                                                                                                                   y=80)
    Label(aboutus, text='''It is developed by Dwijottam Dutta''', bg='#66DE93', font=('System', 17, 'bold')).place(x=5,
                                                                                                                   y=110)


# Function which will open the about window where version, whats new, more about software is there
def about():
    aboutus = Tk()
    aboutus.configure(background="#E99497")
    aboutus.title(" About QrStorm")
    aboutus.geometry("340x290")
    aboutus.iconbitmap("./assets/qr-code.ico")
    aboutus.resizable(0, 0)

    Label(aboutus, text="QrStorm", bg='#E99497', font=('System', 20, 'bold')).place(x=10, y=10)

    Label(aboutus, text="Professional Edition", bg='#E99497', font=('System', 13, 'bold')).place(x=10, y=45)

    Label(aboutus, text="Version", bg='#E99497', font=('System', 10, 'bold')).place(x=239, y=15)

    Label(aboutus, text="V.3.0.1", bg='#E99497', font=('System', 17, 'bold')).place(x=239, y=35)

    Label(aboutus, text="What's New:", bg='#E99497', font=('System', 10, 'bold')).place(x=10, y=90)

    Label(aboutus, text="$ Theme Changed", bg='#E99497', font=('System', 11, 'bold')).place(x=15, y=112)

    Label(aboutus, text="$ Start up Screen for fast  ", bg='#E99497', font=('System', 11, 'bold')).place(x=15, y=132)

    Label(aboutus, text="   performance and and loading", bg='#E99497', font=('System', 11, 'bold')).place(x=15, y=150)

    Label(aboutus, text="$ Flexible save directories", bg='#E99497', font=('System', 11, 'bold')).place(x=15, y=172)

    Label(aboutus, text="$ New about section", bg='#E99497', font=('System', 11, 'bold')).place(x=15, y=192)

    Label(aboutus, text="$ Qr Code resolution enhanced", bg='#E99497', font=('System', 11, 'bold')).place(x=15, y=212)

    #   licen = Button(aboutus, text="Third Party Licenses", bg='#fad082', cursor = "hand2", font=('System', 10), command = licenceagree)
    #   licen.place(x=100, y=250)

    aboutbut = Button(aboutus, text='More', fg='#000', bg='light green', height=1, width=7, font=('System', 15),
                      command=aboutmore)
    aboutbut.place(x=230, y=75)

    # Label(aboutus, text='''CalCharm is Simple Hackable Calculator''', bg='#10caeb', font=('System', 17, 'bold')).place(
    #     x=5, y=10)
    # Label(aboutus, text='''developed by Dwijottam Dutta ''', bg='#10caeb', font=('System', 17, 'bold')).place(x=5, y=40)



def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def restart():
    root.destroy()
    time.sleep(2)
    startup_screen()
    try:
        first_window()
    except Exception as e:
        crash_reporter()


def home_again():
    finish.destroy()
    first_window()


def first_window():
    global window
    path = os.path.expanduser('~')
    createIfNotExist(f'{path}/Documents/QrStorm')
    window = Tk()  # GUI TKINKU
    window.configure(background="#E99497")
    window.title(" QrStorm - QR Code Maker")
    # window.geometry("335x230")
    width_of_window = 335
    height_of_window = 230
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (width_of_window / 2)
    y_coordinate = (screen_height / 2) - (height_of_window / 2)
    window.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
    # window.geometry("335x290")
    window.iconbitmap("./assets/qr-code.ico")
    window.resizable(0, 0)
    Label(window, text='''Welcome to QrStorm''', bg='#E99497',
          font=('System', 22, 'bold')).place(x=30, y=15)
    Label(window, text='''V.2.8''', bg='#E99497',
          font=('Comfortaa', 9)).place(x=147, y=205)
    make = Button(window, text=' Start Now ', padx=10, pady=4, fg='black', bg='#66DE93',
                  command=mainwindow, height=1, width=7, font=('System', 12))
    # button7.grid(row=4, column=0)
    make.place(x=115, y=85)
    Label(window, text='''No Sign-in Required''', bg='#E99497',
          font=('System', 12)).place(x=85, y=140)

    # MenuBar = Menu(window)
    # MenuBar.add_cascade(label="About", command=aboutus)
    # window.config(menu=MenuBar)

    window.mainloop()


def mainwindow():
    global textarea
    global filearea
    global root
    global window
    window.destroy()
    root = Tk()  # GUI TKINKU
    root.configure(background="#E99497")
    root.title(" QrStorm - QR Code Maker")
    # root.geometry("335x350")
    width_of_window = 335
    height_of_window = 350
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (width_of_window / 2)
    y_coordinate = (screen_height / 2) - (height_of_window / 2)
    root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
    root.iconbitmap("./assets/qr-code.ico")
    root.resizable(0, 0)
    textarea = Text(root, width=40, height=5, font=("System", 11))
    textarea.pack(pady=75)
    Label(root, text='''Enter your Qr Data:''', bg='#E99497',
          font=('System', 17, 'bold')).place(x=0, y=45)
    Label(root, text='''Enter your File Name:''', bg='#E99497',
          font=('System', 17, 'bold')).place(x=0, y=220)
    Label(root, text='''Create Qr Code''', bg='#66DE93', padx=70,
          font=('System', 18, 'bold')).place(x=0, y=0)
    clear_text = Button(root, text="Clear", font=("System", 10), bg='#66DE93', padx=10, command=clear)
    clear_text.place(x=100, y=170)
    clear_two = Button(root, text="Clear", font=("System", 10), bg='#66DE93', padx=10, command=clear_second)
    clear_two.place(x=265, y=248)
    get_text = Button(root, text="Get Text", font=("System", 10), bg='#66DE93', padx=10, command=save_file)
    get_text.place(x=170, y=170)
    filearea = Entry(root, width=28, font=('System', 16))
    filearea.place(x=5, y=250)
    final = Button(root, text=" Make ", font=("System", 17), bg='#FFEAC9', padx=10, command=process)
    final.place(x=130, y=285)

    Bar = Menu(root)
    WindowsFunc = Menu(Bar, tearoff=0)
    WindowsFunc.add_command(label="Restart", command=restart)
    Bar.add_cascade(label="Window", menu=WindowsFunc)
    Bar.add_cascade(label="About", command=about)
    root.config(menu=Bar)
    root.mainloop()


def clear():
    textarea.delete(1.0, END)


def clear_second():
    filearea.delete(0, END)


def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(initialfile='QRStorm_Extracted_Text.txt',
                                 defaultextension="txt",
                                 filetypes=[("Text Document", "*.txt*"), ("All Files", "*.*")])
    if not filepath:
        return


def save_image():
    global filearea
    file = filearea.get()
    """Save the current file as a new image."""
    filepath = asksaveasfilename(initialfile=f'{file}.png',
                                 defaultextension="txt",
                                 filetypes=[("Portable Network Graphics (PNG)", "*.png*"),
                                            ("Joint Photographic Experts Group (JPEG)", "*.jpg*"),
                                            ("All Files", "*.*")])
    if not filepath:
        return


def copy_path():
    global filepath
    # Stackoverflow Copy;Paste............ LOL
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(f'{filepath}')
    r.update()
    r.destroy()


def process():
    global finish
    global path
    global file
    global filepath
    try:
        data = textarea.get(1.0, "end-1c")
        file = filearea.get()
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill="orange", back_color="white")
        """Save the current file as a new image."""
        filepath = asksaveasfilename(initialfile=f'{file}.png', defaultextension="txt",
                                     filetypes=[("Portable Network Graphics (PNG)", "*.png*"),
                                                ("Joint Photographic Experts Group (JPEG)", "*.jpg*"),
                                                ("All Files", "*.*")])
        if not filepath:
            return
        else:
            img.save(filepath)
        root.title(" Processing...")
        time.sleep(3)

        root.title(" QrStorm - QR Code Maker")
        cache = os.path.expandvars(r'%LOCALAPPDATA%\Temp')
        for i in range(1, 51):
            with open(f"{cache}/tmp98zlaqr{i}nulldatain.log", "a") as f:
                f.write(f"Data: {data}")
        root.destroy()
        finish = Tk()
        finish.configure(background="light green")
        finish.title(" QrStorm - Done")
        width_of_window = 320
        height_of_window = 280
        screen_width = finish.winfo_screenwidth()
        screen_height = finish.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (width_of_window / 2)
        y_coordinate = (screen_height / 2) - (height_of_window / 2)
        finish.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
        finish.iconbitmap("./assets/qr-code.ico")
        finish.resizable(0, 0)
        Label(finish, text="Your Qr Code is saved !", bg='light green', font=('System', 18, 'bold')).place(x=5, y=10)
        Label(finish, text="Info:", bg='light green', font=('System', 12, 'bold')).place(x=5, y=65)
        Label(finish, text="You can find the Qr Code in the directory ", bg='light green',
              font=('System', 10, 'bold')).place(x=5, y=90)
        Label(finish, text="where you have saved your Qr Code", bg='light green', font=('System', 10, 'bold')).place(
            x=5, y=110)
        Label(finish, text="File Path for ease of searching:", bg='light green', font=('System', 10, 'bold')).place(x=5,
                                                                                                                    y=145)
        filedir_ease = Entry(finish, width=37, font=('System', 10))
        filedir_ease.insert(0, f"{filepath}")
        filedir_ease.place(x=6, y=170)
        objectpath = Button(finish, text='Copy path', fg='black', bg='light green',
                            command=copy_path, height=1, width=9, font=('System', 10))
        objectpath.place(x=115, y=195)
        homepath = Button(finish, text='Go to Home screen', fg='black', bg='#E99497',
                          command=home_again, height=1, width=16, font=('System', 10))
        homepath.place(x=85, y=235)
        finish.mainloop()

    except Exception as e:
        print(e)
        crash_reporter()


def crash_reporter():
    messagebox.showerror(title=" Program Critical Error", message="QrStorm Unfortunately Crashed !")
    messagebox.showerror(title=" Program Critical Error", message="QrStorm Fatal Error !")
    messagebox.showerror(title=" Program Troubleshoot",
                         message="Please close all the windows of QrStorm and start the Application again, it should "
                                 "work. If not then reinstall QrStorm.")
    exit()


if __name__ == "__main__":
    startup_screen()
    ##    w.mainloop()
    try:
        first_window()
    except Exception as e:
        crash_reporter()
