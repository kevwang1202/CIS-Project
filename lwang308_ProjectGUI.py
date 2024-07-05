# Li Kuei Wang CIS345 12:00PM Project
from lwang308_ProjectClass import *
from tkinter import *
from PIL import Image, ImageTk
from os import path
import json
import random
import time

orders = []
doubos_num = 0
cheebos_num = 0
hambos_num = 0
double_num = 0
cheese_num = 0
ham_num = 0
fries_num = 0
softdrinks_num = 0
softdrinkm_num = 0
softdrinkl_num = 0
softdrinkxl_num = 0
chocoshakes_num = 0
strawshakes_num = 0
vanishakes_num = 0
order_num = 0
order_time = ''
order_name = ''
order_phone = 0
order_note = ''


def get_num():
    global doubos_num, cheebos_num, hambos_num, double_num, cheese_num, ham_num, fries_num, softdrinks_num, \
        softdrinkm_num, softdrinkl_num, softdrinkxl_num, chocoshakes_num, strawshakes_num, vanishakes_num

    doubos_num = int(doubos.get())
    cheebos_num = int(cheebos.get())
    hambos_num = int(hambos.get())
    double_num = int(double.get())
    cheese_num = int(cheese.get())
    ham_num = int(ham.get())
    fries_num = int(fries.get())
    softdrinks_num = int(softdrinks.get())
    softdrinkm_num = int(softdrinkm.get())
    softdrinkl_num = int(softdrinkl.get())
    softdrinkxl_num = int(softdrinkxl.get())
    chocoshakes_num = int(chocoshakes.get())
    strawshakes_num = int(strawshakes.get())
    vanishakes_num = int(vanishakes.get())


def get_custdetail():
    global order_num, order_time, order_name, order_phone, order_note
    order_num = random.randint(1, 9999)
    order_time = time.ctime()
    order_name = name_entry.get()
    order_phone = int(phone.get())
    order_note = note_entry.get()


def next_page():
    home_frame.grid_forget()
    contact_frame.grid_forget()
    final_frame.grid_forget()
    summary_frame.grid(columnspan=3)

    contact_clear()
    get_num()

    result_lbl.config(text=f'{doubos_num}*DOUBLE-DOUBLE COMBOS\t{softdrinks_num}*SOFT DRINK (S)\n'
                           f'{cheebos_num}*CHEESEBURGER COMBOS\t{softdrinkm_num}*SOFT DRINK (M)\n'
                           f'{hambos_num}*HAMBURGER COMBOS\t\t{softdrinkl_num}*SOFT DRINK (L)\n'
                           f'{double_num}*DOUBLE-DOUBLE\t\t{softdrinkxl_num}*SOFT DRINK (XL)\n'
                           f'{cheese_num}*CHEESEBURGER\t\t{chocoshakes_num}*CHOCOLATE SHAKES\n'
                           f'{ham_num}*HAMBURGER\t\t          {strawshakes_num}*STRAWBERRY SHAKES\n'
                           f'{fries_num}*FRENCH FRIES\t\t\t{vanishakes_num}*VANILLA SHAKES\n')


def submit():
    global order_cost, order_phone
    while True:
        try:
            order_phone = int(phone.get())
            if order_phone < 10**9:
                raise ValueError
        except (TypeError, ValueError):
            error_label.config(text="Please enter valid phone number")
            return
        else:
            break

    home_frame.grid_forget()
    summary_frame.grid_forget()
    contact_frame.grid_forget()
    final_frame.grid(columnspan=3)

    get_custdetail()
    order_fname = order_name.split(' ')
    get_num()

    order_cost = (doubos_num * 8.75 + cheebos_num * 7.35 + hambos_num * 7.00 + double_num * 4.70 + cheese_num * 3.30 +
                      ham_num * 2.95 + fries_num * 2.15 + softdrinks_num * 1.75 + softdrinkm_num * 1.90 +
                      softdrinkl_num * 2.10 + softdrinkxl_num * 2.30 + chocoshakes_num * 2.70 + strawshakes_num * 2.70 +
                      vanishakes_num * 2.70) * 1.0812
    order_cost = round(order_cost, 2)

    final_lbl.config(text=f'\n\nOrder Time: {order_time}\n' 
                          f'Order Number: {order_num}\n'
                          f'Order Name: {order_name}\n' 
                          f'Phone Number: {order_phone}\n\n'
                          f'{doubos_num}*DOUBLE-DOUBLE COMBOS\t{softdrinks_num}*SOFT DRINK (S)\n'
                          f'{cheebos_num}*CHEESEBURGER COMBOS\t{softdrinkm_num}*SOFT DRINK (M)\n'
                          f'{hambos_num}*HAMBURGER COMBOS\t\t{softdrinkl_num}*SOFT DRINK (L)\n'
                          f'{double_num}*DOUBLE-DOUBLE\t\t{softdrinkxl_num}*SOFT DRINK (XL)\n'
                          f'{cheese_num}*CHEESEBURGER\t\t{chocoshakes_num}*CHOCOLATE SHAKES\n'
                          f'{ham_num}*HAMBURGER\t\t          {strawshakes_num}*STRAWBERRY SHAKES\n'
                          f'{fries_num}*FRENCH FRIES\t\t\t{vanishakes_num}*VANILLA SHAKES\n\n'
                          f'p.s. {order_note}\n\n')

    cost_label.config(text=f"Order total cost is $ {order_cost}!")
    thank_label.config(text=f"Thank you {order_fname[0]}, your order will be ready soon!")
    save_data()


def save_data():
    global order_data

    if not path.isfile('orders.json'):
        with open('orders.json', 'w') as fp:
            json.dump([], fp)

    with open('orders.json') as fp:
        all_orders = json.load(fp)

    order_data = {'Order Time': order_time, 'Order Number': order_num, 'Order Name': order_name,
                  'Phone Number': order_phone, 'Order Cost': order_cost, 'DOUBLE-DOUBLE COMBOS': doubos_num,
                  'CHEESEBURGER COMBOS': cheebos_num, 'HAMBURGER COMBOS': hambos_num, 'DOUBLE-DOUBLE': double_num,
                  'CHEESEBURGER': cheese_num, 'HAMBURGER': ham_num, 'FRENCH FRIES': fries_num,
                  'SOFT DRINK (S)': softdrinks_num, 'SOFT DRINK (M)': softdrinkm_num, 'SOFT DRINK (L)': softdrinkl_num,
                  'SOFT DRINK (XL)': softdrinkxl_num, 'CHOCOLATE SHAKES': chocoshakes_num,
                  'STRAWBERRY SHAKES': strawshakes_num, 'VANILLA SHAKES': vanishakes_num, 'Notes': order_note}

    all_orders.append(order_data)

    with open('orders.json', 'w') as fp:
        json.dump(all_orders, fp)

    order = Orders(order_time, order_num, order_name, order_phone, order_cost, doubos_num, cheebos_num, hambos_num,
                   double_num, cheese_num, ham_num, fries_num, softdrinks_num, softdrinkm_num, softdrinkl_num,
                   softdrinkxl_num, chocoshakes_num, strawshakes_num, vanishakes_num, order_note)
    orders.append(order)


def contact():
    home_frame.grid_forget()
    final_frame.grid_forget()
    summary_frame.grid_forget()
    contact_frame.grid_forget()
    contact_frame.grid(columnspan=3)


def home():
    summary_frame.grid_forget()
    final_frame.grid_forget()
    contact_frame.grid_forget()
    home_frame.grid(columnspan=3)
    clear()


def clear():
    doubos.set(0)
    cheebos.set(0)
    hambos.set(0)
    double.set(0)
    cheese.set(0)
    ham.set(0)
    fries.set(0)
    softdrinks.set(0)
    softdrinkm.set(0)
    softdrinkl.set(0)
    softdrinkxl.set(0)
    chocoshakes.set(0)
    strawshakes.set(0)
    vanishakes.set(0)
    error_label.config(text="")


def contact_clear():
    name.set('')
    phone.set(0)
    note.set('')


def back():
    summary_frame.grid_forget()
    final_frame.grid_forget()
    contact_frame.grid_forget()
    home_frame.grid(columnspan=3)
    error_label.config(text="")


def close():
    window.destroy()


# Create the GUI
window = Tk()
window.title('IN-N-OUT BURGER Online Order App')
window.geometry('600x800')
window.columnconfigure(0, weight=1)
window.config(bg='black')

# Configure variables
doubos = IntVar(value=0)
cheebos = IntVar(value=0)
hambos = IntVar(value=0)
double = IntVar(value=0)
cheese = IntVar(value=0)
ham = IntVar(value=0)
fries = IntVar(value=0)
softdrinks = IntVar(value=0)
softdrinkm = IntVar(value=0)
softdrinkl = IntVar(value=0)
softdrinkxl = IntVar(value=0)
chocoshakes = IntVar(value=0)
strawshakes = IntVar(value=0)
vanishakes = IntVar(value=0)
note = StringVar(value='')
name = StringVar(value='')
phone = StringVar(value='')

# Create a Canvas
canvas = Canvas(window, width=300, height=150, bg='black')
canvas.grid(columnspan=3, pady=10)

# Add the image to the Canvas
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(columnspan=3, column=0, row=0, pady=10)

# Home page
home_frame = Frame(window, width=550, height=650, bg='black')
home_frame.grid(columnspan=3)

# Create greeting labels
greeting_label = Label(home_frame, text='Welcome to IN-N-OUT BURGER ', width=30,
                       fg='white', bg='black', font=('Arial', 24))
greeting_label.grid(columnspan=3, pady=5)

# Box 1 label
fmenu_label = Label(home_frame, text='Food Menu',
                    width=30, fg='white', bg='black', font=('Arial', 26))
fmenu_label.grid(columnspan=3, pady=5)

# Create a Frame
box1 = Frame(home_frame, bg='white', width=550, height=140, borderwidth=5, relief=RIDGE)
box1.grid(row=4, column=0, columnspan=3)
box1.grid_propagate(False)
box1.columnconfigure(0, weight=1)
box1.columnconfigure(1, weight=2)
box1.columnconfigure(2, weight=1)
box1.columnconfigure(3, weight=2)
box1.rowconfigure(0, weight=1)
box1.rowconfigure(1, weight=1)
box1.rowconfigure(2, weight=1)
box1.rowconfigure(3, weight=1)
box1.rowconfigure(4, weight=1)
box1.rowconfigure(5, weight=1)
box1.rowconfigure(6, weight=1)

# Create items on Food Menu
# DOUBLE-DOUBLE COMBOS
doubos_entry = Entry(box1, textvariable=doubos, justify=CENTER, width=3,
                     font=('chalkboard', 12), bg='white', fg='black')
doubos_entry.grid(row=0, column=0, pady=(5, 2), sticky=W)
doubos_label = Label(box1, text='DOUBLE-DOUBLE COMBOS    $6.83', justify=LEFT, width=30, fg='red', bg='white',
                     font=('Arial', 14))
doubos_label.grid(row=0, column=1, sticky=W)
# DOUBLE-DOUBLE
double_entry = Entry(box1, textvariable=double, justify=CENTER, width=3,
                     font=('chalkboard', 12), bg='white', fg='black')
double_entry.grid(row=0, column=2, pady=(5, 2), sticky=W)
double_label = Label(box1, text='DOUBLE-DOUBLE    $3.52', justify=LEFT, width=24, fg='red', bg='white', font=('Arial', 14))
double_label.grid(row=0, column=3, columnspan=2, sticky=W)
# CHEESEBURGER COMBOS
cheebos_entry = Entry(box1, textvariable=cheebos, justify=CENTER, width=3,
                      font=('chalkboard', 12), bg='white', fg='black')
cheebos_entry.grid(row=1, column=0, pady=2, sticky=W)
cheebos_label = Label(box1, text='CHEESEBURGER COMBOS   $5.76', justify=LEFT, width=29, fg='red', bg='white',
                      font=('Arial', 14))
cheebos_label.grid(row=1, column=1, sticky=W)
# CHEESEBURGER
cheese_entry = Entry(box1, textvariable=cheese, justify=CENTER, width=3,
                     font=('chalkboard', 12), bg='white', fg='black')
cheese_entry.grid(row=1, column=2, pady=2, sticky=W)
cheese_label = Label(box1, text='CHEESEBURGER    $2.45', justify=LEFT, width=24, fg='red', bg='white', font=('Arial', 14))
cheese_label.grid(row=1, column=3, sticky=W)
# HAMBURGER COMBOS
hambos_entry = Entry(box1, textvariable=hambos, justify=CENTER, width=3,
                     font=('chalkboard', 12), bg='white', fg='black')
hambos_entry.grid(row=2, column=0, pady=2, sticky=W)
hambos_label = Label(box1, text='HAMBURGER COMBOS    $5.46', justify=LEFT, width=26, fg='red', bg='white', font=('Arial', 14))
hambos_label.grid(row=2, column=1, sticky=W)
# HAMBURGER
ham_entry = Entry(box1, textvariable=ham, justify=CENTER, width=3,
                  font=('chalkboard', 12), bg='white', fg='black')
ham_entry.grid(row=2, column=2, pady=2, sticky=W)
ham_label = Label(box1, text='HAMBURGER    $2.14', justify=LEFT, width=21, fg='red', bg='white', font=('Arial', 14))
ham_label.grid(row=2, column=3, sticky=W)
# FRENCH FRIES
fries_entry = Entry(box1, textvariable=fries, justify=CENTER, width=3,
                    font=('chalkboard', 12), bg='white', fg='black')
fries_entry.grid(row=3, column=0, pady=(2, 5), sticky=W)
fries_label = Label(box1, text='FRENCH FRIES   $1.63', justify=LEFT, width=19, fg='red', bg='white', font=('Arial', 14))
fries_label.grid(row=3, column=1, sticky=W)

# Box 2 label
dmenu_label = Label(home_frame, text='Drink Menu',
                    width=30, fg='white', bg='black', font=('Arial', 26))
dmenu_label.grid(columnspan=3, pady=5)

# Create a Frame for Drink Menu
box2 = Frame(home_frame, bg='white', width=500, height=150, borderwidth=5, relief=RIDGE)
box2.grid(row=6, column=0, columnspan=3, pady=5)
box2.grid_propagate(False)
box2.columnconfigure(0, weight=1)
box2.columnconfigure(1, weight=2)
box2.columnconfigure(2, weight=1)
box2.columnconfigure(3, weight=2)
box2.rowconfigure(0, weight=1)
box2.rowconfigure(1, weight=1)
box2.rowconfigure(2, weight=1)
box2.rowconfigure(3, weight=1)
box2.rowconfigure(4, weight=1)
box2.rowconfigure(5, weight=1)
box2.rowconfigure(6, weight=1)

# Create items on Drink Menu
# SOFT DRINK (S)
softdrinks_entry = Entry(box2, textvariable=softdrinks, justify=CENTER, width=3,
                         font=('chalkboard', 12), bg='white', fg='black')
softdrinks_entry.grid(row=0, column=0, pady=(5, 2), sticky=W)
softdrinks_label = Label(box2, text='SOFT DRINK (S)     $1.53', justify=LEFT, width=20,
                         fg='red', bg='white', font=('Arial', 14))
softdrinks_label.grid(row=0, column=1, sticky=W)
# CHOCOLATE SHAKES
chocoshakes_entry = Entry(box2, textvariable=chocoshakes, justify=CENTER, width=3,
                          font=('chalkboard', 12), bg='white', fg='black')
chocoshakes_entry.grid(row=0, column=2, pady=(5, 2), sticky=W)
chocoshakes_label = Label(box2, text='CHOCOLATE SHAKES   $2.19', justify=LEFT, width=24,
                          fg='red', bg='white', font=('Arial', 14))
chocoshakes_label.grid(row=0, column=3, columnspan=2, sticky=W)
# SOFT DRINK (M)
softdrinkm_entry = Entry(box2, textvariable=softdrinkm, justify=CENTER, width=3,
                         font=('chalkboard', 12), bg='white', fg='black')
softdrinkm_entry.grid(row=1, column=0, pady=2, sticky=W)
softdrinkm_label = Label(box2, text='SOFT DRINK (M)     $1.68', justify=LEFT, width=20,
                         fg='red', bg='white', font=('Arial', 14))
softdrinkm_label.grid(row=1, column=1, sticky=W)
# STRAWBERRY SHAKES
strawshakes_entry = Entry(box2, textvariable=strawshakes, justify=CENTER, width=3,
                          font=('chalkboard', 12), bg='white', fg='black')
strawshakes_entry.grid(row=1, column=2, pady=2, sticky=W)
strawshakes_label = Label(box2, text='STRAWBERRY SHAKES   $2.19', justify=LEFT, width=25,
                          fg='red', bg='white', font=('Arial', 14))
strawshakes_label.grid(row=1, column=3, sticky=W)
# SOFT DRINK (L)
softdrinkl_entry = Entry(box2, textvariable=softdrinkl, justify=CENTER, width=3,
                         font=('chalkboard', 12), bg='white', fg='black')
softdrinkl_entry.grid(row=2, column=0, pady=2, sticky=W)
softdrinkl_label = Label(box2, text='SOFT DRINK (L)     $1.89', justify=LEFT, width=20,
                         fg='red', bg='white', font=('Arial', 14))
softdrinkl_label.grid(row=2, column=1, sticky=W)
# VANILLA SHAKES
vanishakes_entry = Entry(box2, textvariable=vanishakes, justify=CENTER, width=3,
                         font=('chalkboard', 12), bg='white', fg='black')
vanishakes_entry.grid(row=2, column=2, pady=2, sticky=W)
vanishakes_label = Label(box2, text='VANILLA SHAKES   $2.19', justify=LEFT, width=20,
                         fg='red', bg='white', font=('Arial', 14))
vanishakes_label.grid(row=2, column=3, sticky=W)
# SOFT DRINK (XL)
softdrinkxl_entry = Entry(box2, textvariable=softdrinkxl, justify=CENTER, width=3,
                          font=('chalkboard', 12), bg='white', fg='black')
softdrinkxl_entry.grid(row=3, column=0, pady=(2, 5), sticky=W)
softdrinkxl_label = Label(box2, text='SOFT DRINK (XL)   $2.09', justify=LEFT, width=20,
                          fg='red', bg='white', font=('Arial', 14))
softdrinkxl_label.grid(row=3, column=1, sticky=W)

# Add buttons
clear_button = Button(home_frame, command=clear, font=("Arial", 18), text='Clear', width=20)
clear_button.grid(row=10, column=0, pady=(40, 8), padx=10, sticky=W)
next_button = Button(home_frame, command=next_page, font=("Arial", 18), text='Next', width=20)
next_button.grid(row=10, column=1, pady=(40, 8), padx=10, sticky=W)
contact_button = Button(home_frame, command=contact, font=("Arial", 18), text='Contact', width=20)
contact_button.grid(row=11, column=0, pady=8, padx=10, sticky=W)
exit_button = Button(home_frame, command=close, font=("Arial", 18), text='Exit', width=20)
exit_button.grid(row=11, column=1, pady=8, padx=10, sticky=W)

# Copy right label
company_label = Label(home_frame, text='© 2023 In-N-Out Burgers', width=20,
                      fg='white', bg='black', font=('Arial', 9))
company_label.grid(row=12, columnspan=2, pady=10)

# Order Summary page
summary_frame = Frame(window, width=550, height=650, bg='black')
summary_frame.grid(columnspan=3)

# Create summary label
summary_label = Label(summary_frame, text='Order Summary', width=32,
                      fg='white', bg='black', font=('Arial', 30))
summary_label.grid(columnspan=2)

# Display Order Summary
result_lbl = Label(summary_frame, width=55, height=10,
                   justify=LEFT, font=("Arial", 16), bg='white', fg='black')
result_lbl.grid(row=3, column=0, columnspan=2, padx=18, ipadx=10, pady=(10, 5))

# Create note label
note_label = Label(summary_frame, text='Additional Notes', width=32,
                   fg='white', bg='black', font=('Arial', 26))
note_label.grid(row=4, columnspan=2, pady=5)

# Entry for Additional Notes
note_entry = Entry(summary_frame, textvariable=note, justify=CENTER, width=30,
                   font=('chalkboard', 20), bg='white', fg='black')
note_entry.grid(row=5, column=0, columnspan=2)

# Create name and phone label
name_label = Label(summary_frame, text='Enter your name:', width=20,
                   fg='white', bg='black', font=('Arial', 20))
name_label.grid(row=6, column=0, pady=(15, 5))
phone_label = Label(summary_frame, text='Enter your phone number:', width=20,
                    fg='white', bg='black', font=('Arial', 20))
phone_label.grid(row=6, column=1, pady=(15, 5))

# Create entry boxes for name and phone
name_entry = Entry(summary_frame, textvariable=name, justify=CENTER, width=25,
                   bg='white', fg='black', font=('chalkboard', 16))
name_entry.grid(row=7, column=0, pady=(5, 20))
phone_entry = Entry(summary_frame, textvariable=phone, justify=CENTER, width=25,
                    bg='white', fg='black', font=('chalkboard', 16))
phone_entry.grid(row=7, column=1, pady=(5, 20))

# Label for error message
error_label = Label(summary_frame, width=45, justify=LEFT, font=('Arial', 20), bg='black', fg='white')
error_label.grid(row=8, column=0, columnspan=2, padx=18, pady=10)

# Add buttons
clear_button = Button(summary_frame, command=contact_clear, font=("Arial", 18), text='Clear', width=20)
clear_button.grid(row=9, column=0, pady=7, padx=10, sticky=W)
submit_button = Button(summary_frame, command=submit, font=("Arial", 18), text='Submit', width=20)
submit_button.grid(row=9, column=1, pady=7, padx=10, sticky=W)
back_button = Button(summary_frame, command=back, font=("Arial", 18), text='Back', width=20)
back_button.grid(row=10, column=0, pady=7, padx=10, sticky=W)
exit_button = Button(summary_frame, command=close, font=("Arial", 18), text='Exit', width=20)
exit_button.grid(row=10, column=1, pady=7, padx=10, sticky=W)


# Copy right label
company_label = Label(summary_frame, text='© 2023 In-N-Out Burgers', width=20,
                      fg='white', bg='black', font=('Arial', 9))
company_label.grid(row=11, columnspan=2, pady=4)

# Final page
final_frame = Frame(window, width=550, height=650, bg='black')
final_frame.grid(columnspan=3)

# Final Order Detail Label
finalOrder_label = Label(final_frame, text='Final Order Detail', width=32,
                         fg='white', bg='black', font=('Arial', 30))
finalOrder_label.grid(columnspan=2, pady=10)

# Display Final Order Summary
final_lbl = Label(final_frame, width=55, height=15, justify=LEFT,
                  font=("Arial", 16), bg='white', fg='black')
final_lbl.grid(row=3, column=0, columnspan=2, padx=18, ipadx=10, pady=10)

# Thank you message label
cost_label = Label(final_frame, width=50, bg='black', fg='white', font=('Arial', 20))
cost_label.grid(row=4, columnspan=2, pady=10)
thank_label = Label(final_frame, width=50, bg='black', fg='white', font=('Arial', 20))
thank_label.grid(row=5, columnspan=2, pady=10)
bye_label = Label(final_frame, text='We hope we will see you soon!!', width=50,
                  bg='black', fg='white', font=('Arial', 20))
bye_label.grid(row=6, columnspan=2, pady=5)

# Add buttons
home_button = Button(final_frame, command=home, font=("Arial", 20), text='Home', width=15)
home_button.grid(row=7, column=0, pady=20, padx=(35, 0), sticky=W)
exit_button = Button(final_frame, command=close, font=("Arial", 20), text='Exit', width=15)
exit_button.grid(row=7, column=1, pady=20, padx=(35, 0), sticky=W)

# Copy right label
company_label = Label(final_frame, text='© 2023 In-N-Out Burgers', width=20,
                      fg='white', bg='black', font=('Arial', 9))
company_label.grid(row=8, columnspan=2, pady=10)

# Contact page
contact_frame = Frame(window, width=550, height=650, bg='black')
contact_frame.grid(columnspan=3)

# Create labels for contact page
greeting_label = Label(contact_frame, text='Welcome to IN-N-OUT BURGER',
                       width=30, fg='white', bg='black', font=('Arial', 20))
greeting_label.grid(columnspan=2, pady=10)
address_label = Label(contact_frame, text='Address: 4199 Campus Drive, 9th Floor Irvine, CA 92612',
                      width=50, fg='white', bg='black', font=('Arial', 18))
address_label.grid(columnspan=2, pady=10)
phone_label = Label(contact_frame, text='Phone: 1-800-786-1000', width=30, fg='white', bg='black', font=('Arial', 20))
phone_label.grid(columnspan=2, pady=10)

# Add buttons
home_button = Button(contact_frame, command=home, font=("Arial", 20), text='Home', width=15)
home_button.grid(row=8, column=0, pady=10, padx=(35, 0), sticky=W)
exit_button = Button(contact_frame, command=close, font=("Arial", 20), text='Exit', width=15)
exit_button.grid(row=8, column=1, pady=10, padx=(35, 0), sticky=W)

# Copy right label
company_label = Label(contact_frame, text='© 2023 In-N-Out Burgers', width=20,
                      fg='white', bg='black', font=('Arial', 9))
company_label.grid(row=12, columnspan=2, pady=10)

window.mainloop()
