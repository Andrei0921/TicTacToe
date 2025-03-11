import tkinter as tk
import time

playerX = "X"
playerO = "O"
current = playerX
tabla=[[0,0,0],[0,0,0],[0,0,0]]
over=False
turns=0

backround_cl="#472502"
x_color="#fa0202"
o_color="#07fc03"
light_bg="#8a3a04"
winner_cl="#edbf07"

window=tk.Tk()
window.title("TicTacToe")

window.resizable(False, False)

frame=tk.Frame(window)

label=tk.Label(frame,text=current+"'s turn",font=("Arial",15),background=backround_cl, foreground="#ffffff")
label.grid(column=0,row=0,columnspan=3,sticky="we")

def set_title(row,col):
    global current
    if over or tabla[row][col]["text"]!="":
        return
    tabla[row][col]["text"]=current
    if not over:
      if current==playerX:
            current=playerO
            tabla[row][col]["foreground"]=x_color
      else:
            current=playerX
            tabla[row][col]["foreground"]=o_color
      label["text"]=current+"'s turn"
    check_win()



def check_win():
    global over,turns
    turns+=1
    for row in range(3):
        if tabla[row][0]["text"]==tabla[row][1]["text"]==tabla[row][2]["text"] and tabla[row][0]["text"]!="":
            label.config(text=tabla[row][0]["text"]+" won!", foreground=winner_cl)
            for col in range(0,3):
                tabla[row][col].config(fg=winner_cl,background=light_bg)
            over=True
            window.after(3000, new_game)
            return


    for col in range(3):
        if tabla[0][col]["text"]==tabla[1][col]["text"]==tabla[2][col]["text"] and tabla[0][col]["text"]!="" :
            label.config(text=tabla[col][0]["text"]+" won!", foreground=winner_cl)
            for row in range(0,3):
                tabla[row][col].config(foreground=winner_cl,background=light_bg)
            over=True
            window.after(3000, new_game)
            return

    if tabla[0][0]["text"] ==tabla[1][1]["text"] == tabla[2][2]["text"] and tabla[0][0]["text"]!="":
        label.config(text=tabla[0][0]["text"]+" won!", foreground=winner_cl)
        for i in range(0,3):
            tabla[i][i].config(foreground=winner_cl,background=light_bg)
        over=True
        window.after(3000, new_game)
        return

    if tabla[0][2]["text"] ==tabla[1][1]["text"] == tabla[2][0]["text"] and tabla[0][2]["text"]!="":
        label.config(text=tabla[0][2]["text"]+" won!", foreground=winner_cl)
        tabla[0][2].config(foreground=winner_cl,background=light_bg)
        tabla[1][1].config(foreground=winner_cl,background=light_bg)
        tabla[2][0].config(foreground=winner_cl,background=light_bg)
        over=True
        window.after(3000, new_game)
        return
    if turns==9:
        over=True
        label.config(text="Draw!",foreground=winner_cl)
        window.after(3000, new_game)
        return
def new_game():
    global over,turns
    turns=0
    over=False
    label.config(text=current+"'s turn",foreground="#ffffff")
    for row in range(3):
        for col in range(3):
            tabla[row][col].config(text="",background=backround_cl)


for rows in range(3):
    for col in range(3):
        tabla[rows][col]=tk.Button(frame,text="",font=("Arial",50,"bold"),bg=backround_cl,width=4,height=1,
                                  command=lambda row=rows,column=col: set_title(row,column))
        tabla[rows][col].grid(row=rows+1,column=col)

restart_btn=tk.Button(frame,text="Restart",font=("Arial",12),background=backround_cl, foreground="#ffffff", command=new_game)
restart_btn.grid(column=0,row=4,columnspan=3,sticky="we")

frame.pack()
window.mainloop()