# REGISTATION FORM USING GUI

from tkinter import *
from tkinter import messagebox as mb
from tkcalendar import DateEntry
import datetime
import csv


root = Tk()
root.geometry('500x500')
root.title("Welcome to Registration Form")



#defining function msg() using messagebox
def msg():
    select = var.get()
    if(select == 1 or select == 2):
        # get the index of the last character in the widget,if it is zero,it is empty
        if (entry_1.index("end") == 0):
            mb.showwarning('Missing details', 'enter your name')
        elif(entry_3.index("end") == 0):
            mb.showwarning('Missing details', 'enter your Phone number')
        elif(entry_4.index("end")==0):
            mb.showwarning('Missing detail','enter your email')
        elif(entry_5.index("end")==0):
            mb.showwarning("Missing detail","enter your password")
        else:
            mb.showinfo('Success', 'Registration done successfully! ')
    else:
            mb.showinfo('Missing details', 'enter your gender')




#exporting entered data
def save():
    g = var.get()
    db = date.get_date()
    d = db.strftime('%d/%m/%Y')
    now = datetime.datetime.now()
    if(g==1):
        gender ='male'
    else:
        gender ='female'



    # save data in txt file

    s = '\n' + now.strftime("%d-%m-%Y %H:%M") +'\t' + entry_1.get() + '\t' + entry_3.get() + '\t' + entry_4.get() + '\t' + d +'\t' + entry_5.get()
    f = open(('regdetails.txt'), 'a')
    f.write(s)
    f.close()

    # save data in csv file
    with open('Registrationfile.csv', 'a') as fs:
        w = csv.writer(fs, dialect='excel-tab')
        w.writerow([now.strftime("%d-%m-%Y %H:%M"),entry_1.get()   , entry_3.get()  , entry_4.get()     ,entry_5.get()     ,d, gender])
        fs.close()


def saveinfo():
    save()
    msg()





#creating labels and widgets



label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Full Name",width=20,font=("bold", 10),anchor="w")
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)


label_2 = Label(root, text="Date",width=20,font=("bold", 10),anchor="w")
label_2.place(x=80,y=170)

entry_2 = Entry(root)
entry_2.place(x=240,y=170)

date = DateEntry(root, width=27, background='brown', foreground='white',date_pattern='dd/mm/Y', borderwidth=3)
date.place(x=240,y=170)


label_3 = Label(root, text="Phone No. ",width=20,font=("bold", 10),anchor="w")
label_3.place(x=80,y=210)

entry_3 = Entry(root)
entry_3.place(x=240,y=210)


label_4 = Label(root, text="Email Address",width=20,font=("bold", 10),anchor="w")
label_4.place(x=80,y=250)

entry_4 = Entry(root)
entry_4.place(x=240,y=250)


label_5 = Label(root, text="Password",width=20,font=("bold", 10),anchor="w")
label_5.place(x=80,y=290)

entry_5 = Entry(root,show="*")
entry_5.place(x=240,y=290)

label_6 = Label(root, text="Gender ",width=20,font=("bold", 10),anchor="w")
label_6.place(x=80,y=310)

# radiobuttons
var = IntVar()
r1 = Radiobutton(root, text="Male", variable=var, value=1, font=("times",12))
r1.place(x=240,y=310)
r2 = Radiobutton(root, text="Female", variable=var, value=2, font=("times",12))
r2.place(x=310,y=310)



#submit button and cancel button

Button(root, text='Submit',command=saveinfo,width=20,bg='Green',fg='White').place(x=80,y=380)

Button(root, text='Cancel',command=root.destroy,width=20,bg='Brown',fg='white').place(x=250,y=380)
root.mainloop()

