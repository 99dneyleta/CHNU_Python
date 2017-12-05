from tkinter import *
from tkinter import messagebox


def isEven(number):
  if number % 2 == 0:
    return True
  else:
    return False


class CheckOddForm:

  def say(self, phrase):
    messagebox.showinfo("Msg", phrase)

  def command(self):
    try:
      value = float(self.eInputNumber.get())
      if self.activeRb.get() == "Even":
        self.say(str(isEven(value)))
      else:
        self.say(str(not isEven(value)))
    except ValueError as e:
      print(e)

    return False




  def __init__(self, master):

    self.master = master
    master.title("Check Number")

    self.activeRb = StringVar()
    self.eInputNumber = Entry(master)

    self.rbIsEven = Radiobutton(master, text="Is Even", command=self.command, value="Even", variable=self.activeRb)
    self.rbIsOdd = Radiobutton(master, text="Is Odd?", command=self.command, value="Odd", variable=self.activeRb)

    self.rbIsEven.pack()
    self.rbIsOdd.pack()
    self.eInputNumber.pack()

root = Tk()
gui = CheckOddForm(root)
root.mainloop()