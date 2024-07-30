import tkinter as tk
import tkinter.messagebox as msgbox
import sqlite3 as sql

con=sql.connect("student.db")
cur=con.cursor()
form=tk.Tk()
form.title("Student Login page")
lblh=tk.Label(form,text="U15IG22S0020",font=("Arial",22,"bold"),fg="blue")
lblh.grid(row=0,column=1,sticky=tk.W,padx=10,pady=5)
form.geometry('600x500')
lbluno=tk.Label(form,text="UUCMSNO")
lbluno.grid(row=1,column=0,sticky=tk.W)
etuno=tk.Entry(form,width=20)
etuno.grid(row=1,column=1,padx=10,pady=5)
lblpas=tk.Label(form,text="Password")
lblpas.grid(row=2,column=0,sticky=tk.W)
etpas=tk.Entry(form,width=20)
etpas.grid(row=2,column=1,padx=10,pady=5)
def log():
        uno=etuno.get()
        pas=etpas.get()
        cur.execute("select * from students where uno=? and pas=?",(uno,pas))
        student=cur.fetchall()
        if student:
                msgbox.showinfo("Message","login Successfully")
        else:
                msgbox.showerror("message","invalid uno or password")
btnlog=tk.Button(form,text="Login",command=log)
btnlog.grid(row=3,column=0,columnspan=1,padx=50,pady=15)
def reg():
        form.destroy()
        import main as m   
        m.setup_database()
btnreg=tk.Button(form,text="Register",command=reg)
btnreg.grid(row=3,column=1,columnspan=2,padx=50,pady=20)
form.mainloop()
