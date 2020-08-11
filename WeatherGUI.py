from tkinter import Tk, Frame, Label
from tkinter.ttk import Notebook
from DublinWeather import AnalyseWeather

window=Tk()
window.title("Dublin Weather")
window.geometry("1000x500")

frame2=Frame(window)
frame2.pack(fill="both")

tablayout=Notebook(frame2)

#tab1
tab1=Frame(tablayout)
tab1.pack(fill="both")

for row in range(13):
    if row == 0:
        for column in range(6):
            if column == 1:
                label = Label(tab1, text='Time', bg="green", fg="black", padx=3, pady=3)
                label.config(font=('Arial', 14))
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            if column == 2:
                label = Label(tab1, text='Temp', bg="green", fg="black", padx=3, pady=3)
                label.config(font=('Arial', 14))
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            if column == 3:
                label = Label(tab1, text='Weather', bg="green", fg="black", padx=3, pady=3)
                label.config(font=('Arial', 14))
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            if column == 4:
                label = Label(tab1, text='Rain', bg="green", fg="black", padx=3, pady=3)
                label.config(font=('Arial', 14))
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            if column == 5:
                label = Label(tab1, text='Wind', bg="green", fg="black", padx=3, pady=3)
                label.config(font=('Arial', 14))
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
    else:
        for column in range(7):
            if column == 1:
                for i in AnalyseWeather.Weather3['Time']:
                    for row in range(1, 14):
                        if AnalyseWeather.Weather3['Time'].index(i) == range(1, 14).index(row):
                            label = Label(tab1, text=i, bg="green", fg="black", padx=3, pady=3)
                            label.config(font=('Arial', 12))
                            label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                            tab1.grid_columnconfigure(column, weight=1)
            if column == 2:
                for i in AnalyseWeather.Weather3['Temp']:
                    for row in range(1, 14):
                        if AnalyseWeather.Weather3['Temp'].index(i) == range(1, 14).index(row):
                            label = Label(tab1, text=str(i), bg="red", fg="black", padx=3, pady=3)
                            label.config(font=('Arial', 12))
                            label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                            tab1.grid_columnconfigure(column, weight=1)
            if column == 3:
                for i in AnalyseWeather.Weather3['Weather']:
                    for row in range(1, 14):
                        if AnalyseWeather.Weather3['Weather'].index(i) == range(1, 14).index(row):
                            label = Label(tab1, text=str(i), bg="blue", fg="black", padx=3, pady=3)
                            label.config(font=('Arial', 12))
                            label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                            tab1.grid_columnconfigure(column, weight=1)
            if column == 4:
                for i in AnalyseWeather.Weather3['Rain']:
                    for row in range(1, 14):
                        if AnalyseWeather.Weather3['Rain'].index(i) == range(1, 14).index(row):
                            label = Label(tab1, text=i, bg="green", fg="black", padx=3, pady=3)
                            label.config(font=('Arial', 12))
                            label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                            tab1.grid_columnconfigure(column, weight=1)
            if column == 5:
                for i in AnalyseWeather.Weather3['Wind']:
                    for row in range(1, 14):
                        if AnalyseWeather.Weather3['Wind'].index(i) == range(1, 14).index(row):
                            label = Label(tab1, text=i, bg="grey", fg="black", padx=3, pady=3)
                            label.config(font=('Arial', 12))
                            label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                            tab1.grid_columnconfigure(column, weight=1)

tablayout.add(tab1,text="Hourly Weather")

#tab2
tab1=Frame(tablayout)
tab1.pack(fill="both")

for row in range(8):
    if row == 0:
        for column in range(7):
            if column == 1:
                label = Label(tab1, text='Day', bg="green", fg="black", padx=3, pady=3)
                label.config(font=('Arial', 14))
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            if column == 2:
                label = Label(tab1, text='Temp-High', bg="green", fg="black", padx=3, pady=3)
                label.config(font=('Arial', 14))
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            if column == 3:
                label = Label(tab1, text='Temp-Low', bg="green", fg="black", padx=3, pady=3)
                label.config(font=('Arial', 14))
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            if column == 4:
                label = Label(tab1, text='Weather', bg="green", fg="black", padx=3, pady=3)
                label.config(font=('Arial', 14))
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            if column == 5:
                label = Label(tab1, text='Rain', bg="green", fg="black", padx=3, pady=3)
                label.config(font=('Arial', 14))
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            if column==6:
                label = Label(tab1, text="Wind", bg="green", fg="black", padx=3, pady=3)
                label.config(font=('Arial', 14))
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
    else:
        for column in range(7):
            if column == 1:
                for i in AnalyseWeather.Weather2['Day']:
                    for row in range(1, 8):
                        if AnalyseWeather.Weather2['Day'].index(i) == range(1, 8).index(row):
                            label = Label(tab1, text=i, bg="green", fg="black", padx=3, pady=3)
                            label.config(font=('Arial', 12))
                            label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                            tab1.grid_columnconfigure(column, weight=1)
            if column == 2:
                for i in AnalyseWeather.Weather2['Temp-High']:
                    for row in range(1, 8):
                        if AnalyseWeather.Weather2['Temp-High'].index(i) == range(1, 8).index(row):
                            print(i)
                            label = Label(tab1, text=str(i), bg="red", fg="black", padx=3, pady=3)
                            label.config(font=('Arial', 12))
                            label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                            tab1.grid_columnconfigure(column, weight=1)
            if column == 3:
                for i in AnalyseWeather.Weather2['Temp-Low']:
                    for row in range(1, 8):
                        if AnalyseWeather.Weather2['Temp-Low'].index(i) == range(1, 8).index(row):
                            label = Label(tab1, text=str(i), bg="blue", fg="black", padx=3, pady=3)
                            label.config(font=('Arial', 12))
                            label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                            tab1.grid_columnconfigure(column, weight=1)
            if column == 4:
                for i in AnalyseWeather.Weather2['Weather']:
                    for row in range(1, 8):
                        if AnalyseWeather.Weather2['Weather'].index(i) == range(1, 8).index(row):
                            label = Label(tab1, text=i, bg="green", fg="black", padx=3, pady=3)
                            label.config(font=('Arial', 12))
                            label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                            tab1.grid_columnconfigure(column, weight=1)
            if column == 5:
                for i in AnalyseWeather.Weather2['Rain']:
                    for row in range(1, 8):
                        if AnalyseWeather.Weather2['Rain'].index(i) == range(1, 8).index(row):
                            label = Label(tab1, text=i, bg="grey", fg="black", padx=3, pady=3)
                            label.config(font=('Arial', 12))
                            label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                            tab1.grid_columnconfigure(column, weight=1)
            if column == 6:
                for i in AnalyseWeather.Weather2['Wind']:
                    for row in range(1, 8):
                        if AnalyseWeather.Weather2['Wind'].index(i) == range(1, 8).index(row):
                            label = Label(tab1, text=i, bg="grey", fg="black", padx=3, pady=3)
                            label.config(font=('Arial', 12))
                            label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                            tab1.grid_columnconfigure(column, weight=1)

tablayout.add(tab1,text="Daily Weather")

tablayout.pack(fill="both")

window.mainloop()
