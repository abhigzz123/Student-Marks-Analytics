import os
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.metrics import accuracy_score as score
from sklearn.model_selection import train_test_split
data = pd.read_csv('D:\\all prOJECT\project sem 5\pract\data.csv' , names = ["10th" , "12th"  , "cgpa" , "automata" , "automata_fix" ,"computer sc","computer sc perc" , "writex" , "logitcal" ,  "logical perc" , "computer programming" , "computer programming perc" , "Quant" , "Quant perc" , "English" , "English Perc" , "total" , "y_label" ])
data["total"] = data["total"].astype(float)
data["y_label"][data.total > 4500] = 1
data["y_label"][data.total <= 4500] = 0
X_train , X_test , Y_train , Y_test =train_test_split(data.iloc[:,0:16] , data.iloc[:,17] , test_size = 0.2 , random_state = 1)
X_train , X_cv , Y_train , Y_cv = train_test_split(X_train ,Y_train , test_size = 0.2 , random_state = 1)
model = knn(n_neighbors = 75)
model.fit(X_train , Y_train)
from tkinter import *
from tkinter import messagebox
# connect to the databse.

# cursor to move around the databse

# empty list to later append the ids from the database
ids = []

# tkinter window
class Application:
    def __init__(self, master):
        self.master = master

        # creating the frames in the master
        self.left = Frame(master, width=1000, height=720, bg='lightgreen')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

        # labels for the window
        self.heading = Label(self.left, text="Placement Prediction System", font=('arial 40 bold'), fg='black', bg='lightgreen')
        self.heading.place(x=0, y=0)
        # ten
        self.ten = Label(self.left, text="10th", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.ten.place(x=0, y=100)

        # twelve
        self.twelve = Label(self.left, text="12th", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.twelve.place(x=550, y=100)

        # gender
        self.cgpa = Label(self.left, text="cgpa", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.cgpa.place(x=0, y=140)

        
        self.writex = Label(self.left, text="Writex", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.writex.place(x=550, y=140)
        
        # location
        self.automata = Label(self.left, text="Automata", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.automata.place(x=0, y=180)

        # appointment time
        self.automata_fix = Label(self.left, text="Automata Fix", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.automata_fix.place(x=550, y=180)

        # phone
        self.cs = Label(self.left, text="Computer Sc.", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.cs.place(x=0, y=220)
        
        self.cs_perc = Label(self.left, text="CS percentile", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.cs_perc.place(x=550, y=220)

        self.logical = Label(self.left, text="Logical", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.logical.place(x=0, y=260)

        self.logical_perc = Label(self.left, text="Logical Percentile", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.logical_perc.place(x=550, y=260)

        self.cp = Label(self.left, text="Comp. Programming", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.cp.place(x=0, y=300)

        self.cp_perc = Label(self.left, text="Comp. Prog. Perc.", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.cp_perc.place(x=550, y=300)

        self.quant = Label(self.left, text="Quant", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.quant.place(x=0, y=340)

        self.quant_perc = Label(self.left, text="Quant percentile", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.quant_perc.place(x=550, y=340)

        self.eng = Label(self.left, text="English", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.eng.place(x=0, y=380)
        
        self.eng_perc = Label(self.left, text="English Percentile", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.eng_perc.place(x=550, y=380)

#efewfwef

        # ten
        self.ten = Entry(self.left, width=30)
        self.ten.place(x=300, y=100)

        # twelve
        self.twelve = Entry(self.left, width=30)
        self.twelve.place(x=800, y=100)

        # gender
        self.cgpa = Entry(self.left, width=30)
        self.cgpa.place(x=300, y=140)

        
        self.writex = Entry(self.left, width=30)
        self.writex.place(x=800, y=140)
        
        # location
        self.automata = Entry(self.left, width=30)
        self.automata.place(x=300, y=180)

        # appointment time
        self.automata_fix = Entry(self.left, width=30)
        self.automata_fix.place(x=800, y=180)

        # phone
        self.cs = Entry(self.left, width=30)
        self.cs.place(x=300, y=220)
        
        self.cs_perc = Entry(self.left, width=30)
        self.cs_perc.place(x=800, y=220)

        self.logical = Entry(self.left, width=30)
        self.logical.place(x=300, y=260)

        self.logical_perc = Entry(self.left, width=30)
        self.logical_perc.place(x=800, y=260)

        self.cp = Entry(self.left, width=30)
        self.cp.place(x=300, y=300)

        self.cp_perc = Entry(self.left, width=30)
        self.cp_perc.place(x=800, y=300)

        self.quant = Entry(self.left, width=30)
        self.quant.place(x=300, y=340)

        self.quant_perc = Entry(self.left, width=30)
        self.quant_perc.place(x=800, y=340)

        self.eng = Entry(self.left, width=30)
        self.eng.place(x=300, y=380)
        
        self.eng_perc = Entry(self.left, width=30)
        self.eng_perc.place(x=800, y=380)


        # Entries for all labels============================================================


        # button to perform a command
        self.submit = Button(self.left, text=" RESULT ", width=20, height=2, bg='steelblue', command=self.add_appointment)
        self.submit.place(x=300, y=450)
    
        # getting the number of appointments fixed to view in the log
     # funtion to call when the submit button is clicked
    def add_appointment(self):
        # getting the user inputs\

        # checking if the user input is empty
        a1=self.ten.get()
        a2=self.twelve.get()
        a3=self.cgpa.get()
        a4=self.automata.get()
        a5=self.automata_fix.get()
        a6=self.cs.get()
        a7=self.cs_perc.get()
        a8=self.writex.get()
        a9=self.logical.get()
        a10=self.logical_perc.get()
        a11=self.cp.get()
        a12=self.cp_perc.get()
        a13=self.quant.get()
        a14=self.quant_perc.get()
        a15=self.eng.get()
        a16=self.eng_perc.get()
        if  a1 == '' or a2 == '' or a3 == '' or a4 == '' or a5 == '' or a6 == '' or a7 == '' or a8 == '' or a9 == '' or a10 == '' or a11 == '' or a12 == '' or a13 == '' or a14 == '' or a15 == '' or a16 == '':
            messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            # now we add to the database
            x=pd.DataFrame([(float(a1),float(a2),float(a3),float(a4),float(a5),float(a6),float(a7),float(a8),float(a9),float(a10),float(a11),float(a12),float(a13),float(a14),float(a15),float(a16))],columns = ["10th" , "12th"  , "cgpa" , "automata" , "automata_fix" ,"computer sc","computer sc perc" , "writex" , "logitcal" ,  "logical perc" , "computer programming" , "computer programming perc" , "Quant" , "Quant perc" , "English" , "English Perc"])
            x.iloc[0,:].astype(float)
            y=model.predict(x)
            if y== 1:
                s="PLACED"
            else: s="NOT PLACED"    
            messagebox.showinfo(" PREDICTION     ",  f"          {s}           ")
            
# creating the object
root = Tk()
b = Application(root)

# resolution of the window
root.geometry("1200x720+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()