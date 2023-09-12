import tkinter
from tkinter import *

root=Tk()
root.title("To-Do-List")
root.geometry("500x650+400+100")
root.resizable(False,False)

task_list=[]

def addTask():
    task = writing_tasks.get()
    writing_tasks.delete(0, END)

    if task :
         with open("tasklist.txt",'a') as taskfile:
              taskfile.write(f"\n{task}")
              task_list.append(task)
              Listbox.insert( END,task)

def deleteTask():
     global task_list
     task =str(Listbox.get(ANCHOR))
     if task in task_list:
          task_list.remove(task)
          with open("tasklist.txt",'w') as taskfile:
               for task in task_list:
                    taskfile.write(task+"\n")
          Listbox.delete(ANCHOR)


def openTaskFile():

    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
             tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                Listbox.insert(END, task)
    except:
                file=open('tasklist.txt','w')
                file.close()



Image_icon=PhotoImage(file="D:\\project images\\taskboard.png")
root.iconphoto(False,Image_icon)

TopImage=PhotoImage(file="D:\\project images\\topbar.png")
Label(root,image=TopImage).pack()

ThreelinesImage=PhotoImage(file="D:\\project images\\images.png")
Label(root,image=ThreelinesImage,bg="#32405b").place(x=30,y=20)

ClipboarImage=PhotoImage(file="D:\\project images\\taskboard.png")
Label(root,image=ClipboarImage,bg="#32405b").place(x=440,y=15)

heading = Label(root,text="TASK LIST",font="arial 20 bold",fg="white",bg="#32405b")
heading.place(x=170,y=12)

Enter_Task = Frame(root,width=500,height=60,bg="white")
Enter_Task.place(x=0,y=180)

task=StringVar()
writing_tasks=Entry(Enter_Task,width=18,font="arial 20",bd=0)
writing_tasks.place(x=10,y=7)
writing_tasks.focus()

ADD_button=Button(Enter_Task,text="ADD",font="arial 20 bold",width=8,bg="#5a95ff",fg="#fff",bd=0,command=addTask)
ADD_button.place(x=380,y=5)


taskbox = Frame(root,bd=3,width=800,height=280,bg="#32405b")
taskbox.pack(pady=(200,0))
Listbox= Listbox(taskbox,font=('arial',12),width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
Listbox.pack(side=LEFT,fill=BOTH, padx=2)
Scrollbar=Scrollbar(taskbox)
Scrollbar.pack(side=RIGHT , fill=BOTH)


Listbox.config(yscrollcommand=Scrollbar.set)
Scrollbar.config(command=Listbox.yview)

openTaskFile()

delete_image=PhotoImage(file="D:\\project images\\delete.png")
Button(root,image=delete_image,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)


root.mainloop()