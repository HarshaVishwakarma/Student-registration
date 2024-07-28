import tkinter
from tkinter import *
from tkinter.ttk import Combobox
from numpy import place


class Gui:

    def __init__(self):
        self.ses = Tk()
        self.ses.title("My gui window")
        self.ses.geometry("800x800")
        self.ses.configure(bg="light pink")


        #add photo to the gui
        # Load an image using PIL
        self.image = PhotoImage(file="images - Copy.png")

        self.bg=PhotoImage(file="bag1 - Copy.jpg")
        self.label1=Label(master=self.ses, image=self.bg)
        self.label1.place(x=0,y=0)

        # Create a Label widget to display the image
        label = Label(image=self.image)
        label.pack()

        self.labelname=Label(master=self.ses,text="student id")
        self.labelname.place(x=20,y=300,width=200,height=30)

        self.entryid=Entry(master=self.ses,show="*")
        self.entryid.place(x=260,y=300,width=200,height=30)

        self.studname = Label(master=self.ses, text="name")
        self.studname.place(x=20, y= 350, width=200, height=30)

        self.entryname = Entry(master=self.ses)
        self.entryname.place(x=260, y=350, width=200, height=30)

        self.department = Label(master=self.ses, text="Department")
        self.department.place(x=20, y=400, width=200, height=30)

        # Department Label and Combobox
        self.entrydep = Entry(master=self.ses)
        self.choices=['CSE','ETC','IT','CT','AIDS']
        self.entrydep.place(x=260, y=400, width=200, height=30)
        self.dept_combobox = Combobox(master=self.ses, values=self.choices, state="readonly",
                                          font=('consolas', 18, 'bold'))
        self.dept_combobox.place(x=260, y=400, width=200, height=30)

        self.studclg = Label(master=self.ses, text="College name")
        self.studclg.place(x=20, y=450, width=200, height=30)

        self.entryclg = Entry(master=self.ses)
        self.entryclg.place(x=260, y=450, width=200, height=30)

        # Gender Label and Radio Buttons

        self.gender=Label(master=self.ses,text="enter your gender")
        self.gender.place(x=20, y=500, width=200, height=30)

        #radiobuttons

        self.rd=Radiobutton(master=self.ses,text='Male',value=1)
        self.rd.place(x=260,y=500)

        self.rd = Radiobutton(master=self.ses, text='Female',value=2)
        self.rd.place(x=350, y=500)

        self.lang = Label(master=self.ses, text="choose your language")
        self.lang.place(x=20, y=550, width=500, height=30)

        #checkbutton
        self.check_button0=Checkbutton(master=self.ses,text="C")
        self.check_button0.place(x=20, y=600, width=100, height=30)

        self.check_button1 = Checkbutton(master=self.ses, text="C++")
        self.check_button1.place(x=140, y=600, width=100, height=30)


        self.check_button2 = Checkbutton(master=self.ses, text="Python")
        self.check_button2.place(x=260, y=600, width=100, height=30)

        self.check_button3= Checkbutton(master=self.ses, text="Java")
        self.check_button3.place(x=380, y=600, width=100, height=30)
        #checkbox with a label

        self.check_button4 = Checkbutton(master=self.ses, text="YES")
        self.check_button4.place(x=10, y=640, width=100, height=30)

        self.gender = Label(master=self.ses, text="I hereby confirmed that the above information is correct and we can proceed for next process")
        self.gender.place(x=80, y=640, width=590, height=30)

        #submit button
        self.submit = Button(master=self.ses, text="SUBMIT", font=('consolas', 18, 'bold'))
        self.submit.place(x=250, y=700, width=100, height=30)

        self.ses.mainloop()  # hold the window


if __name__== '__main__':
    ses=Gui()