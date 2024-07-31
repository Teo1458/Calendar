import calendar
import tkinter as tk


window = tk.Tk()
window.geometry("300x300")
window.title("Calendario")
window.configure(background="white")
window.resizable(False, False)

def input():
    global year
    year = entry.get()
   

label = tk.Label(text="Ciao, inserisci l'anno")
entry=tk.Entry (fg="black", bg="white",width=10)


first_button = tk.Button(text="Start", command=input)


label = tk.Label(text="Ora inserisci il mese")
entry=tk.Entry (fg="black", bg="white",width=10)

second_button = tk.Button(text="Start", command= input)

print (calendar (year,month))
label.pack()
entry.pack()

first_button.pack()
second_button.pack()
#print (calendar.month ( year, month ) )

if __name__ == "__main__":
    window.mainloop()

