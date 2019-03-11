from tkinter import *
from tkinter.filedialog import askopenfilename
import os
root = Tk()
label_1 = Label(root, text="Course Name: ")
course = Entry(root)
fPath=''
global allPaths
allPaths=[]
allCoursesInputed=[]
fileNames=[]
label_2= Label(root, text="")
matrixA=[]
matrixA.append([])
matrixA.append([])
def convert():
    print('hi')
    error = Label(root)
    error.configure(background='yellow')
    error.config(text="Folders converted")
    error.grid(row=0, column=2)
    cleaner(fileNames)
def setFile():
    filePath = askopenfilename()
    fPath=filePath
    return fPath

def buttonClick():
    global allPaths
    fPath = setFile()
    if course.get() == '':
        error.config(text="No course detected")
    elif fPath == '':
        error.config(text="")
    else:
        allCoursesInputed.append(course.get())
        matrixA[0].append(course.get())
        matrixA[1].append(fPath)
        allPaths.append(fPath)
        fileNames.append(os.path.basename(fPath))
        for x in range (len(allPaths)):
            y=x
            y = str(y)
            error.config(text="")
            #label_3 = Label(root, textvariable=y, text=""+allCoursesInputed[x]+" ("+fileNames[x]+")")
            label_3=Label(root,text=""+allCoursesInputed[x]+" ("+fileNames[x]+")")
            label_3.grid(row=x+1, column=1)
            button2 = Button(root, command=convert,text="Convert")
            button2.pack_forget()
            button2.grid(row=len(allPaths)+1,column=1)
    print(matrixA)

def reset():
    os.execl(sys.executable, sys.executable, *sys.argv)
button1 = Button(root,command=buttonClick,text="Add File")
buttonReset=Button(root,command=reset,text="Reset")
buttonReset.grid(row=2,column=0)

button1.grid(row=1)
label_2.grid(row=1)
label_1.grid(row=0)
course.grid(row=0,column=1)
error = Label(root)
error.configure(background='red')
error.grid(row=0, column=2)
root.configure(background='green')
root.mainloop()