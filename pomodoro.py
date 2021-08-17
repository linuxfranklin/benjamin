from  tkinter import  *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time
count=5
while True :
    time.sleep(1)
    count-=1

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=150, pady=150, bg=PINK, highlightthickness=0)

timer=Label(text="Timer", font=(FONT_NAME, 35),fg=GREEN)
timer.grid(column=1, row = 0)

canvas=Canvas(width=300, height=300)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(135,135, image=tomato_img)
canvas.create_text(135,135, text="00:00", fill="white", font=(FONT_NAME,30, "bold"))
canvas.grid(column=1, row=1)

start_button=Button(text="Start")
start_button.grid(column=0, row =5)


text1=Label(text="✔")
text1.grid(column=1, row = 5)

reset_button=Button(text="Reset")
reset_button.grid(column=2, row =5)








window.mainloop()