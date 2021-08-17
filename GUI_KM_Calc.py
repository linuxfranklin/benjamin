from tkinter import *


def button_clicked():
    print("I got clicked")
    miles_label = miles_input.get()
    miles = int(miles_label) * 1.609
    kilometer_result_label.config(text=miles)




window = Tk()
window.title("Miles to KM")
window.config(padx=10, pady=20)

miles_lable=Label(text="Miles")
miles_lable.grid(row=1, column=1)
miles_input=Entry(width=5)
miles_input.grid(row=1, column=2)



is_equal_label=Label(text="Is equal to")
is_equal_label.grid(row=3, column=1)
kilometer_result_label=Label(text="0")
kilometer_result_label.grid(row=3, column=2)
kilometer_label=Label(text="KM")
kilometer_label.grid(row=3, column=3)

calculate_button=Button(text="Calculate",command=button_clicked)
calculate_button.grid(row=6, column=1)


#window.minsize(width=500, height=300)
#window.config(padx=500, pady=300)


window.mainloop()