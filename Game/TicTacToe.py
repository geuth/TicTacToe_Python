from tkinter import *
counter = 9
def game_entry(val):
    global counter
    
    if (counter %2) == 0:
        if val == "number_one":
            counter = counter - 1
            button_one.config(text = "X", state = DISABLED, disabledforeground="red")
        elif val == "number_two":
            button_two.config(text = "X", state = DISABLED, disabledforeground="red")
            counter = counter - 1
            
        elif val == "number_three":
            button_three.config(text = "X", state = DISABLED, disabledforeground="red")
            counter = counter - 1
            
        elif val == "number_four":
            button_four.config(text = "X", state = DISABLED, disabledforeground="red")
            counter = counter - 1
            
        elif val == "number_five":
            button_five.config(text = "X", state = DISABLED, disabledforeground="red")
            counter = counter - 1
            
        elif val == "number_six":
            button_six.config(text = "X", state = DISABLED, disabledforeground="red")
            counter = counter - 1
            
        elif val == "number_seven":
            button_seven.config(text = "X", state = DISABLED, disabledforeground="red")
            counter = counter - 1
            
        elif val == "number_eight":
            button_eight.config(text = "X", state = DISABLED, disabledforeground="red")
            counter = counter - 1
            
        elif val == "number_nine":
            button_nine.config(text = "X", state = DISABLED, disabledforeground="red")
            counter = counter - 1
    else:
        if val == "number_one":
            counter = counter - 1
            button_one.config(text = "O", state = DISABLED, disabledforeground="blue")
            
        elif val == "number_two":
            button_two.config(text = "O", state = DISABLED, disabledforeground="blue")
            counter = counter - 1
            
        elif val == "number_three":
            button_three.config(text = "O", state = DISABLED, disabledforeground="blue")
            counter = counter - 1
            
        elif val == "number_four":
            button_four.config(text = "O", state = DISABLED, disabledforeground="blue")
            counter = counter - 1
        elif val == "number_five":
            button_five.config(text = "O", state = DISABLED, disabledforeground="blue")
            counter = counter - 1
        elif val == "number_six":
            button_six.config(text = "O", state = DISABLED, disabledforeground="blue")
            counter = counter - 1
            
        elif val == "number_seven":
            button_seven.config(text = "O", state = DISABLED, disabledforeground="blue")
            counter = counter - 1
            
        elif val == "number_eight":
            button_eight.config(text = "O", state = DISABLED, disabledforeground="blue")
            counter = counter - 1
            
        elif val == "number_nine":
            button_nine.config(text = "O", state = DISABLED, disabledforeground="blue")
            counter = counter - 1
    check()
def check():
    box_one = button_one.cget('text')
    box_two = button_two.cget('text')
    box_three = button_three.cget('text')
    box_four = button_four.cget('text')
    box_five = button_five.cget('text')
    box_six = button_six.cget('text')
    box_seven = button_seven.cget('text')
    box_eight = button_eight.cget('text')
    box_nine = button_nine.cget('text')
    
    if box_one == "X" and box_two == "X" and box_three == "X" or box_one == "X" and box_five == "X" and box_nine == "X" or\
    box_one == "X" and box_four == "X" and box_seven == "X" or box_two == "X" and box_five == "X" and box_eight == "X" or\
    box_three == "X" and box_six == "X" and box_nine == "X" or box_three == "X" and box_five == "X" and box_seven == "X" or\
    box_four == "X" and box_five == "X" and box_six == "X" or box_seven == "X" and box_eight == "X" and box_nine == "X" :
        result_label.config(text = "Player 2 won")
        button_one.config(state = DISABLED)
        button_two.config(state = DISABLED)
        button_three.config(state = DISABLED)
        button_four.config(state = DISABLED)
        button_five.config(state = DISABLED)
        button_six.config(state = DISABLED)
        button_seven.config(state = DISABLED)
        button_eight.config(state = DISABLED)
        button_nine.config(state = DISABLED)
            
    if box_one == "O" and box_two == "O" and box_three == "O" or box_one == "O" and box_five == "O" and box_nine == "O" or\
    box_one == "O" and box_four == "O" and box_seven == "O" or box_two == "O" and box_five == "O" and box_eight == "O" or\
    box_three == "O" and box_six == "O" and box_nine == "O" or box_three == "O" and box_five == "O" and box_seven == "O" or\
    box_four == "O" and box_five == "O" and box_six == "O" or box_seven == "O" and box_eight == "O" and box_nine == "O" :
        result_label.config(text = "Player 1 won")
        button_one.config(state = DISABLED)
        button_two.config(state = DISABLED)
        button_three.config(state = DISABLED)
        button_four.config(state = DISABLED)
        button_five.config(state = DISABLED)
        button_six.config(state = DISABLED)
        button_seven.config(state = DISABLED)
        button_eight.config(state = DISABLED)
        button_nine.config(state = DISABLED)
        
def reset():
    button_one.config(state = NORMAL, text="")
    button_two.config(state = NORMAL, text="")
    button_three.config(state = NORMAL, text="")
    button_four.config(state = NORMAL, text="")
    button_five.config(state = NORMAL, text="")
    button_six.config(state = NORMAL, text="")
    button_seven.config(state = NORMAL, text="")
    button_eight.config(state = NORMAL, text="")
    button_nine.config(state = NORMAL, text="")
    result_label.config(text = "")
root = Tk()
root.geometry("430x335")
root.title("Tic Tac Toe")

frame = Frame(root)
title = Label(root, text="Tic Tac Toe")
title.pack()
frame.pack()

game_frame = Frame(root)

button_one = Button(game_frame, command= lambda: game_entry("number_one"))
button_one.config(bg="black",width ="10", height="5")
button_one.pack(side=LEFT)


button_two = Button(game_frame,command= lambda: game_entry("number_two"))
button_two.config(bg="black",width ="10", height="5")
button_two.pack(side=LEFT)

button_three = Button(game_frame,command= lambda: game_entry("number_three"))
button_three.config(bg="black",width ="10", height="5")
button_three.pack(side=LEFT)


game_frame.pack(fill=BOTH, padx="65")

game_frame2 = Frame(root)

button_four = Button(game_frame2, command= lambda: game_entry("number_four"))
button_four.config(bg="black",width ="10", height="5")
button_four.pack(side=LEFT)


button_five = Button(game_frame2,command= lambda: game_entry("number_five"))
button_five.config(bg="black",width ="10", height="5")
button_five.pack(side=LEFT)

button_six = Button(game_frame2,command= lambda: game_entry("number_six"))
button_six.config(bg="black",width ="10", height="5")
button_six.pack(side=LEFT)


game_frame2.pack(fill=BOTH, padx="65")


game_frame3 = Frame(root)

button_seven = Button(game_frame3, command= lambda: game_entry("number_seven"))
button_seven.config(bg="black",width ="10", height="5")
button_seven.pack(side=LEFT)


button_eight = Button(game_frame3,command= lambda: game_entry("number_eight"))
button_eight.config(bg="black",width ="10", height="5")
button_eight.pack(side=LEFT)

button_nine = Button(game_frame3,command= lambda: game_entry("number_nine"))
button_nine.config(bg="black",width ="10", height="5")
button_nine.pack(side=LEFT)


game_frame3.pack(fill=BOTH, padx="65")

result_frame = Frame(root)
result_label = Label(result_frame)

result_label.pack()
result_frame.pack()

reset_frame = Frame(root)
reset_button = Button(reset_frame, text="Reset", command = reset)
reset_button.pack()
reset_frame.pack()

root.mainloop()
