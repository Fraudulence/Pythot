'''
KRISH PATEL
'''

#function to check whether a string could be a number
def is_number(n):
    try:
        float(n)
        return True
    except:
        return False

#function to round a number if the number's decimal part is greater than or equal to .5
def rounder(n):
    if float(n) - int(n) >= .5:
        n = int(n) + 1
    return n 

from tkinter import * #doesnt import messagebox for some reason 
from tkinter import messagebox 

#creating window
window= Tk()
window.title("Grade Program")
window.geometry('500x300')

#creating label + class entry box
Label(window,text = "Programming: ",pady = 10,padx = 10).grid(column = 0, row = 0)
class1 = Entry(window)
class1.grid(column = 1, row = 0)
Label(window,text = "Art: ",pady = 10, padx = 10).grid(column = 0, row = 1)
class2 = Entry(window)
class2.grid(column = 1, row = 1)
Label(window,text = "Science: ",pady = 10,padx = 10).grid(column = 0, row = 2)
class3 = Entry(window)
class3.grid(column = 1, row = 2)
Label(window,text = "Math: ",pady = 10,padx = 10).grid(column = 0, row = 3)
class4 = Entry(window)
class4.grid(column = 1, row = 3)
Label(window,text = "History: ",pady = 10,padx= 10).grid(column = 0, row = 4)
class5 = Entry(window)
class5.grid(column = 1, row = 4)

#function for adding grades
class1_grades = []
class2_grades = []
class3_grades = []
class4_grades = []
class5_grades =[]
def success():
    messagebox.showinfo("SUCCESS","Grade has been added!")
def add1():
    grade = class1.get().strip()
    if is_number(grade) and float(grade) >= 0:
        class1_grades.append(float(grade)) #adds to respective grade array
        success()
    else:
        messagebox.showerror("ERROR","Please only enter positive numeric grades!")
def add2():
    grade = class2.get().strip()
    if is_number(grade) and float(grade) >= 0:
        class2_grades.append(float(grade))
        success()
    else:
        messagebox.showerror("ERROR","Please only enter positive numeric grades!")
    
def add3():
    grade = class3.get().strip()
    if is_number(grade) and float(grade) >= 0:
        class3_grades.append(float(grade))
        success()
    else:
        messagebox.showerror("ERROR","Please only enter positive numeric grades!")
    
def add4():
    grade = class4.get().strip()
    if is_number(grade) and float(grade) >= 0:
        class4_grades.append(float(grade))
        success()
    else:
        messagebox.showerror("ERROR","Please only enter positive numeric grades!")
def add5():
    grade = class5.get().strip()
    if is_number(grade) and float(grade) >= 0:
        class5_grades.append(float(grade))
        success()
    else:
        messagebox.showerror("ERROR","Please only enter positive numeric grades!")
    
#creating button to add grades
add_class1 = Button(window,text = "ADD GRADE",command = add1)
add_class2 = Button(window,text = "ADD GRADE",command = add2)
add_class3 = Button(window,text = "ADD GRADE",command = add3)
add_class4 = Button(window,text = "ADD GRADE",command = add4)
add_class5 = Button(window,text = "ADD GRADE",command = add5)
add_class1.grid(column = 2,row = 0)
add_class2.grid(column = 2,row = 1)
add_class3.grid(column = 2, row = 2)
add_class4.grid(column = 2, row = 3)
add_class5.grid(column = 2, row = 4)



#creating calculate,clear, and exit buttons
Label(window,text = "").grid(column = 0, row = 5) #free space
def display(arr,name):
    #print(arr) debug
    lowest = 10**8
    highest = -1
    #finds highest and lowest grade
    for i in arr:
        if i < lowest:
            lowest = i
        if i > highest:
            highest = i
    
    #rounds numbers in array if the fit certain criteria and calculates average
    copy_arr = arr[:]
    for i in range(0,len(copy_arr)):
        copy_arr[i] = rounder(copy_arr[i])
    if len(copy_arr) != 0:
        average = sum(copy_arr)/len(copy_arr)
        messagebox.showinfo("Stats for " + name, name + "\nScores Entered: " + str(arr) + 
        "\nCurrent Average: " + str(round(average,2)) + '\nHighest Grade: ' + str(round(highest,2)) 
        + '\nLowest Grade: ' + str(round(lowest,2)))
    else:
        messagebox.showerror("ERROR","No grades have been entered for: " + name)
    
def Calculate():
    display(class1_grades,"Programming")
    display(class2_grades,"Art")
    display(class3_grades,"Science")
    display(class4_grades,"Math")
    display(class5_grades,"History")
def Clear():
    #clearing entry boxes
    class1.delete(0,END)
    class2.delete(0,END)
    class3.delete(0,END)
    class4.delete(0,END)
    class5.delete(0,END)

    #clearing grade arrays
    class1_grades.clear()
    class2_grades.clear()
    class3_grades.clear() 
    class4_grades.clear()
    class5_grades.clear()
    #print(class1_grades) 
    messagebox.showinfo("Cleared","Your grades have been reset!")
def Exit():
    window.destroy()

    
calculate = Button(window, text = "Calculate",command = Calculate)
calculate.grid(column = 0, row = 6)
clear = Button(window,text = "Clear",command = Clear)
clear.grid(column = 1, row = 6)
exit = Button(window,text = "Exit",command = Exit)
exit.grid(column = 2, row = 6)
	
window.mainloop() #keeps window going
