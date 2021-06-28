import os
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.metrics import accuracy_score as score
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.model_selection import train_test_split
dict={1:'10th_percentage', 2:'12th_percentage', 3:'collegePercentage',
       4:'WriteX_Total Score', 5:'English Comprehension(Score_1)',
       6: 'Logical Ability(Score_13)',
        7:'Quantitative Ability (Advanced)(Score_2)',
       8:'Computer Programming(Score_5)',9:'Automata(Score_812)', 10:'Computer Science(Score_189)'}
data = pd.read_csv('D:\\all prOJECT\project sem 5\data1.csv' , header='infer')
d=data.iloc[:,[8,9,10,16,17,18,19,20,21,22,23,24,25,26,27,30,32]].copy()
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

       
        # phone
        self.cs = Label(self.left, text="Computer Sc.", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.cs.place(x=0, y=220)

        self.logical = Label(self.left, text="Logical", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.logical.place(x=0, y=260)

        self.cp = Label(self.left, text="Comp. Programming", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.cp.place(x=0, y=300)

        self.quant = Label(self.left, text="Quant", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.quant.place(x=0, y=340)
        
        self.eng = Label(self.left, text="English", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.eng.place(x=0, y=380)
        
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
        
        # phone
        self.cs = Entry(self.left, width=30)
        self.cs.place(x=300, y=220)
 
        self.logical = Entry(self.left, width=30)
        self.logical.place(x=300, y=260)

        self.cp = Entry(self.left, width=30)
        self.cp.place(x=300, y=300)

        self.quant = Entry(self.left, width=30)
        self.quant.place(x=300, y=340)

        self.eng = Entry(self.left, width=30)
        self.eng.place(x=300, y=380)
    
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
        a5=self.cs.get()      
        a6=self.writex.get()
        a7=self.logical.get()
        a8=self.cp.get()
        a9=self.quant.get()
        a10=self.eng.get()
        if  a1 == '' or a2 == '' or a3 == '' or a4 == '' or a5 == '' or a6 == '' or a7 == '' or a8 == '' or a9 == '' or a10 == '':
            messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            # now we add to the database
            l=[]
            f=[]
            if a1!=0:
                l.append(a1)
                r.append(dict[1])
            elif a2!=0:
                l.append(a1)
                r.append(dict[2])
            elif a3!=0:
                l.append(a1)
                r.append(dict[3])
            elif a4!=0:
                l.append(a1)
                r.append(dict[9])
            elif a5!=0:
                l.append(a1)
                r.append(dict[10])            
            elif a6!=0:
                l.append(a1)
                r.append(dict[4])            
            elif a7!=0:
                l.append(a1)
                r.append(dict[6])            
            elif a8!=0:
                l.append(a1)
                r.append(dict[8])            
            elif a9!=0:
                l.append(a1)
                r.append(dict[7])            
            elif a10!=0:
                l.append(a1)
                r.append(dict[5])
            X = np.asarray(d[r])
            Y = np.asarray(d['Total'])
            X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, shuffle= True)
            lineReg = LinearRegression()
            lineReg.fit(X_train, y_train)
            X = np.asarray([l])
            
            if y== 1:
                s="PLACED"
            else: s="NOT PLACED"    
            messagebox.showinfo(" PREDICTION     ",  f"          {print(lineReg.predict(X))}  ")
            
# creating the object
root = Tk()
b = Application(root)

# resolution of the window
root.geometry("1200x720+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()