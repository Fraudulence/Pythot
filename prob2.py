'''
KRISH PATEL
SKILLS USA 2017 GRADE PROGRAM
'''

def is_number(n): #returns whether string could be a float number
    try:
        float(n)
        return True
    except:
        return False

def rounder(n): #rounds numbers that have a decimal portion of .5 or greater to the next whole number
    if float(n) - int(n) >= .5:
        return int(n) + 1
    return float(n)

def initialize():
    
    Label(window,text = "Grade Calculator",pady = 10,padx = 10).grid(column = 0, row = 1)

    #creating grade arrays for each class
    progArr = []
    artArr = []
    sciArr = []
    mathArr = []
    hisArr = []
        
    def classAdder(entry,gradeArray): #adding grade to a specific class
        grade = entry.get().strip()
        if all(grade) and is_number(grade) and float(grade) >= 0:
            gradeArray.append(float(grade))
            messagebox.showinfo("SUCCESS","Grade has been added!")
            #print(grade,end = " ") 
            #print(gradeArray)
        else:
            messagebox.showerror("ERROR","Please enter a numeric, positive/zero value for your grade!")

    #creating labels, entry boxes, and buttons for each class
    Label(window,text = "Programming:",pady = 10,padx = 10).grid(column = 0, row = 2)
    programmingEntry = Entry(window)
    programmingEntry.grid(column = 1,row = 2)
    programmingButton = Button(window,text = "ADD GRADE",padx = 10,command = partial(classAdder,programmingEntry,progArr))
    programmingButton.grid(column = 2, row = 2)
    programmingEntry.focus()

    Label(window,text = "Art:",pady = 10,padx = 10).grid(column = 0, row = 3)
    artEntry = Entry(window)
    artEntry.grid(column = 1, row = 3)
    artButton = Button(window,text = "ADD GRADE",padx = 10,command = partial(classAdder,artEntry,artArr))
    artButton.grid(column = 2, row = 3)

    Label(window,text = "Science:",pady = 10,padx = 10).grid(column = 0, row = 4)
    scienceEntry = Entry(window)
    scienceEntry.grid(column = 1, row = 4)
    scienceButton = Button(window,text = "ADD GRADE",padx = 10,command = partial(classAdder,scienceEntry,sciArr))
    scienceButton.grid(column = 2, row = 4)

    Label(window,text = "Math:",pady = 10,padx = 10).grid(column = 0, row = 5)
    mathEntry = Entry(window)
    mathEntry.grid(column = 1,row = 5)
    mathButton = Button(window,text = "ADD GRADE",padx = 10,command = partial(classAdder,mathEntry,mathArr))
    mathButton.grid(column = 2,row = 5)

    Label(window,text = "History:",pady = 10,padx = 10).grid(column =0,row = 6)
    historyEntry = Entry(window)
    historyEntry.grid(column = 1, row = 6)
    historyButton = Button(window,text = "ADD GRADE",padx = 10,command = partial(classAdder,historyEntry,hisArr))
    historyButton.grid(column = 2, row = 6)

    Label(window,text = "").grid(column = 0, row = 7) #free space

    def gradeChecker(gradeArr,className):
        if len(gradeArr) > 0:
            maxi = -1
            mini = 10**8
            originalGrades = gradeArr[:] #creating copy of gradeArray that contain original values 
            for i in range(len(gradeArr)):
                if gradeArr[i] > maxi:
                    maxi = gradeArr[i]
                if gradeArr[i] < mini:
                    mini = gradeArr[i]
                gradeArr[i] = rounder(gradeArr[i]) #rounding grades of .5  or higher to the next whole number
            gradeAverage = round(sum(gradeArr)/len(gradeArr),2)
            messagebox.showinfo("Grades for "+ className, "Class: " + className + "\nGrades entered: "+str(originalGrades)+'\nGrade average: ' +str(gradeAverage)+'\nHighest Grade: '+str(maxi)+'\nLowest Grade: ' +str(mini))
        else:
            messagebox.showerror("NO GRADES","No grades have been entered for " + className)
            
    def calculate():
        gradeChecker(progArr,"Programming")
        gradeChecker(artArr,"Art")
        gradeChecker(sciArr,"Science")
        gradeChecker(mathArr,"Math")
        gradeChecker(hisArr,"History")
        
    def clear():
        #clearing grade arrays
        progArr.clear()
        mathArr.clear()
        sciArr.clear()
        hisArr.clear()
        artArr.clear()

        #clearing text fields
        mathEntry.delete(0,END)
        scienceEntry.delete(0,END)
        programmingEntry.delete(0,END)
        historyEntry.delete(0,END)
        artEntry.delete(0,END)
        programmingEntry.focus()

        messagebox.showinfo("ClEARED","Grades have been cleared and scores have been reset!")
        
    def exit():
        window.destroy() #closes application

    #buttons for clear, calculate, and exit
    Calculate = Button(window,text = "Calculate",command = calculate)
    Calculate.grid(column = 0, row = 8)
    Clear = Button(window,text= "Clear",command = clear)
    Clear.grid(column = 1, row = 8)
    Exit = Button(window,text = "Exit",command = exit)
    Exit.grid(column = 2, row = 8)

    
'''important modules'''
from tkinter import *
from tkinter import messagebox
from functools import partial #allows one to pass parameters in a tkinter command without invoking function immediately

window = Tk() #declaring window
window.geometry('600x400') #setting size of window
window.title("Grade Calculator") #title

initialize() #declaring and creating all buttons, labels, etc.
window.mainloop() #keeps window going
