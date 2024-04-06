import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

from classes.lista_piatti import ListaPiatti
from classes.costanti import *

def start_gui():
    main_window()

def path_window():
    filetypes = [('Excel files', '*.xlsx')]
    filename = fd.askopenfilename(title='Scegli il file Excel', initialdir='.', filetypes=filetypes)
    return filename

def main_window():
    window = tk.Tk()

    # apertura file e creazione istanza della lista piatti ----------
    filename = path_window()
    lista_piatti = ListaPiatti()
    lista_piatti.read(filename)

    # sezione input -------------------------------------------------
    frame_input = tk.Frame()

    # linea 1 -------------------------------------------------------
    frame_line1 = tk.Frame(master=frame_input)

    label_portata = tk.Label(master=frame_line1, text="Portata:")
    label_portata.pack(side=tkinter.LEFT)

    n1 = tk.StringVar()
    combobox_portata = ttk.Combobox(master=frame_line1, textvariable=n1)
    combobox_portata["values"] = PORTATE
    combobox_portata["state"] = "readonly"
    combobox_portata.current(2)
    combobox_portata.pack(side=tkinter.RIGHT)

    frame_line1.pack()

    # linea 2 -------------------------------------------------------
    frame_line2 = tk.Frame(master=frame_input)

    label_base = tk.Label(master=frame_line2, text="Base:")
    label_base.pack(side=tkinter.LEFT)

    n2 = tk.StringVar()
    combobox_portata = ttk.Combobox(master=frame_line2, textvariable=n2)
    combobox_portata["values"] = BASI
    combobox_portata["state"] = "readonly"
    combobox_portata.current(0)
    combobox_portata.pack(side=tkinter.RIGHT)

    frame_line2.pack()

    # linea 3 -------------------------------------------------------
    frame_line3 = tk.Frame(master=frame_input)

    label_ingredienti = tk.Label(master=frame_line3, text="Ingredienti:")
    label_ingredienti.pack(side=tkinter.LEFT)

    n3 = tk.StringVar()
    combobox_portata = ttk.Combobox(master=frame_line3, textvariable=n3)
    combobox_portata["values"] = lista_piatti.ingredienti
    combobox_portata["state"] = "readonly"
    combobox_portata.current(0)
    combobox_portata.pack(side=tkinter.RIGHT)

    frame_line3.pack()

    # linea 4 -------------------------------------------------------
    frame_line4 = tk.Frame()

    button_piatto_caso = ttk.Button(master=frame_line4, text="Piatto a caso")
    button_piatto_caso.pack(side=tkinter.LEFT)

    button_tutti_piatti = ttk.Button(master=frame_line4, text="Tutti i piatti")
    button_tutti_piatti.pack(side=tkinter.RIGHT)

    frame_line4.pack(side=tkinter.BOTTOM)

    frame_input.pack()

    # sezione output ------------------------------------------------
    frame_output = tk.Frame()
    frame_output.pack()

    window.mainloop()


#--------------------Test-------------------
if __name__ == "__main__":
    start_gui()