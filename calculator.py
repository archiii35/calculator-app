from tkinter import*
import ast


root = Tk()

#To get the command for a particular button clicked.
i = 0
def getnumber(num):
    global i 
    display.insert(i,num)
    i+=1

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i+=length

def clear_all():
    display.delete(0,END)

def calculate():
    entire_string = display.get()
    try:
        node = ast.parse(entire_string, mode="eval")
        result = eval(compile(node, '<string>', 'eval'))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"ERROR")

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"")




# To display the numbers and the entry screen.

display = Entry(root)
display.grid(row = 0, columnspan= 6)
numbers = [1,2,3,4,5,6,7,8,9]
count = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[count]
        button = Button(root, text = button_text, width=4, height=3, command = lambda text = button_text: getnumber(text))
        button.grid(row = x+1, column = y, padx = 3, pady = 3)
        count += 1
button1 = Button(root, text = '0', width=4, height = 3, command = lambda: getnumber(0))
button1.grid(row = 4, column = 1, padx = 3, pady = 3)



#To display the operations in the calculator.

counter = 0
operations = ['+', '-', '*', '/', '*3.14', '(', "**", ')', "**2"]
for x in range(4):
    for y in range(3):
        if counter<len(operations):
            button = Button(root, text=operations[counter], width = 4, height = 3, command = lambda text = operations[counter]: get_operation(text))
            counter +=1
            button.grid(row = x+1, column=y+3, padx = 5, pady = 5)


Button(root, text="AC", width=4, height=3, command = clear_all).grid(row =4, column = 0)
Button(root, text="=", width=4, height=3, command = calculate).grid(row =4, column = 2)
Button(root, text = "<-", width=4, height = 3, command = lambda :undo()).grid(row=4, column = 4)
root.mainloop()