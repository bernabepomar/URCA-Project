import tkinter as tk
from tkinter import ttk

#----------------------|| WINDOW ||---------------------------------
root= tk.Tk() #definimos variable window como ventana
root.title('URCA Control Panel') #asignamos un título a la ventana
root.geometry('800x500') #tamaño de la ventana

#----------------------|| TITLE ||---------------------------------
title_label=ttk.Label(master=root, text='Aircraft Control Panel',font='Calibri 24 bold') #hacemos un label (un widget que es texto) y definimos su master como windows
title_label.pack()#para que aparezca el texto

#----------------------|| EVENTS ||---------------------------------
events_frame=ttk.Frame(master=root) #creamos un cuadro donde meter cosas dentro de window
title_events_label=ttk.Label(master=events_frame,text='Events',font='Calibri 12')
title_events_label.pack(side='top',pady=5) #definimos donde ponerlo y el padding entre los distintos objetos
events_frame.pack(side='right',padx=5,pady=5)#hacemos que aparezca el frame

#----------------------|| END SESSION||---------------------------------
ttk.Button(root, text='End session', command=root.destroy).pack(side='bottom')



#----------------------|| RUN ||---------------------------------
root.mainloop() #para que la ventana aparezca, asignamos el mainloop a window

