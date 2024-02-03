from tkinter import * 
import random

root=Tk()
root.title("Random")
root.geometry("400x400")

headingLabel = Label(root)
headingLabel["text"] = "Click the button to find out what item (out of the items shown below) you should put in your bag."
headingLabel.place(relx= 0.5, rely= 0.1, anchor = CENTER)

list1 = ["a bottle", "a tiffin", "an ID Card", "some chocolates", "some chips", "some tickets", "a hanky"]
print(list1)

itemLabel = Label(root)
randomItemLabel = Label(root)

itemLabel["text"] = "Items: a bottle, a tiffin, an ID card, chocolates, chips, tickets, a hanky"

def random_number():
    random_no = random.randint(0, 6)
    print(random_no)
    random_item = list1[random_no]
    randomItemLabel["text"] = "Put " + str(random_item) + " in your bag."
    print("Put " + random_item + " in your bag.")
    
btn1 = Button(root)
btn1 = Button(root, text = "Item that should be put inside your bag", command = random_number)
btn1.place(relx=0.5, rely=0.5, anchor = CENTER)

itemLabel.place(relx= 0.5, rely= 0.3, anchor = CENTER)
randomItemLabel.place(relx= 0.5, rely= 0.7, anchor = CENTER)

root.mainloop()