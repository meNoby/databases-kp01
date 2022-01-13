import psycopg2
import random
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename, askdirectory
import tkinter.font as font
import tkinter.messagebox
import module

conn  =  psycopg2.connect(dbname = 'weather', user = 'postgres', 
                        password = 'postgrepass', host = 'localhost')
cursor  =  conn.cursor()
conn.autocommit  =  True


def danger_to_file(lst):
    fin = open(module.dirname + '/res.txt', 'w')
    for item in lst:
        fin.write(item + "\n")

def read_constants_from_file():
    fin = open(module.fileconsts, 'r')
    res = {}
    for line in fin:
        line.replace(' ', '')
        lst  =  line.split(':')
        lst_from_to = lst[1].split('to')
        res[lst[0]] = (float(lst_from_to[0]), float(lst_from_to[1]))
    return res


def get_lst_locals():
    fin = open(module.filelocals, 'r')
    lst = []
    for line in fin:
        lst.append(line)
    return lst

def random_input(constants):
    lst  =  get_lst_locals()
    for i in range(60):
        locate = (lst[int(random.uniform(0,45))]).replace('\n', '')
        temp_wat = float(random.uniform((constants['temp_water'][0]) - 1,(constants['temp_water'][1])+1))
        temp_air = float(random.uniform((constants['temp_air'][0]) -1,(constants['temp_air'][1]) + 2))
        humidity_air = float(random.uniform((constants['humidity_air'][0]),(constants['humidity_air'][1]) + 1))
        danger = float(random.uniform((constants['danger_air'][0]),(constants['danger_air'][1]))+1)
        if humidity_air<0:
            humidity_air = 0.01
        if danger < 0:
            danger = 0.01
        cursor.execute("INSERT INTO weather_stats(location, temp_air, temp_water, humidity_air, danger_air) VALUES ('{}', '{}', {}, {}, {})".format(locate, temp_wat, temp_air, humidity_air, danger))


def analyze(constants):
    cursor.execute('SELECT * FROM weather_stats')
    id_danger = []
    for row in cursor:
        if row[1] < ((constants['temp_water'])[0]) or row[1] > ((constants['temp_water'])[1]):
            id_danger.append(str(row[5]) + " is dangerous")
            continue    
        if row[2] < ((constants['temp_air'])[0]) or row[2] > ((constants['temp_air'])[1]):
            id_danger.append(str(row[5]) + " is dangerous")
            continue
        if row[3] < ((constants['humidity_air'])[0]) or row[3] > ((constants['humidity_air'])[1]):
            id_danger.append(str(row[5]) + " is dangerous")
            continue
        if row[4] < ((constants['danger_air']))[0] or row[4] > ((constants['danger_air'])[1]):
            id_danger.append(str(row[5]) + " is dangerous")
            continue
        id_danger.append(str(row[5]) + " is not dangerous")
    dangers = set(id_danger)
    danger_to_file(dangers)


def clear():
    cursor.execute(f"DELETE FROM weather_stats")


def browse_const():
    module.fileconsts = askopenfilename()
    module.const['text'] = 'File containing const values was chosen'


def browse_local():
    module.filelocals = askopenfilename()
    module.locals['text'] = 'File with location names was chosen'

def browse_resp():
    module.dirname = askdirectory(parent = window, initialdir = "/",title = 'Please select a directory')
    module.res['text'] = "Directory for result output was chosen"


def start():
    clear()
    constants = read_constants_from_file()
    random_input(constants)
    analyze(constants)
    tkinter.messagebox.showinfo(title = "Success", message = "Data was analized and saved")



window  =  Tk() 
window.geometry('680x550')
window.resizable(False, False)
window.title("Weather analysis") 

myFont = font.Font(family = "Courier", size = 15, weight = "bold")

module.const = Label(window, text = "File containing const values wasn\'t chosen", font = myFont)
module.const.place(relx = 0.5, rely = 0.1, anchor = CENTER)
module.locals = Label(window, text = "File containing location names wasn\'t chosen",  font = myFont)
module.locals.place(relx = 0.5, rely = 0.35, anchor = CENTER)
module.res = Label(window, text = "Directory for result output wasn\'t chosen",  font = myFont)
module.res.place(relx = 0.5, rely = 0.6, anchor = CENTER)

btn_consts = Button(text = "Choose file", width = 30, command = browse_const).place(relx = 0.5, rely = 0.2, anchor = CENTER)
btn_locals = Button(text = "Choose file", width = 30, command = browse_local).place(relx = 0.5, rely = 0.45, anchor = CENTER)
btn_locals = Button(text = "Choose folder", width = 30, command = browse_resp).place(relx = 0.5, rely = 0.7, anchor = CENTER)
btn_start = Button(text = "Begin analysis", width = 45, command = start).place(relx = 0.5, rely = 0.85, anchor = CENTER)

window.mainloop()