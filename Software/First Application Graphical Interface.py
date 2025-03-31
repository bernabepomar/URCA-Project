import tkinter as tk

root = tk.Tk()

# para definir el tamaño de la ventana y su nombre
root.geometry("500x500")
root.title("URCA C.I.")

# label es para el cabezeo del texto con su mensaje y la fuente que queremos etc.
label = tk.Label(root, text="URCA Control Interface" , font=('Times New Roman', 16))
label.pack (padx=30, pady=10)

#para hacer un tabla de botones 1,2 y 3 filas de botones
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

#configuración del primer botón, esta vez el master es buttonframe y no root
btn1 = tk.Button(buttonframe, text="1", font=('Times New Roman', 12))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=('Times New Roman', 12))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=('Times New Roman', 12))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=('Times New Roman', 12))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=('Times New Roman', 12))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=('Times New Roman', 12))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

btn7 = tk.Button(buttonframe, text="7", font=('Times New Roman', 12))
btn7.grid(row=2, column=0, sticky=tk.W+tk.E)

btn8 = tk.Button(buttonframe, text="8", font=('Times New Roman', 12))
btn8.grid(row=2, column=1, sticky=tk.W+tk.E)

btn9 = tk.Button(buttonframe, text="9", font=('Times New Roman', 12))
btn9.grid(row=2, column=2, sticky=tk.W+tk.E)

btn10 = tk.Button(buttonframe, text="10", font=('Times New Roman', 12))
btn10.grid(row=3, column=0, sticky=tk.W+tk.E)

btn11 = tk.Button(buttonframe, text="11", font=('Times New Roman', 12))
btn11.grid(row=3, column=1, sticky=tk.W+tk.E)

#esto nos dice que los botones de la tabla van a repartirse por todo el eje x
buttonframe.pack(fill="x")

root.mainloop()