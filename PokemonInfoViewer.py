from tkinter import *
from tkinter import ttk



def main():

#create the window
    root = Tk()
    root.title("Pokemon Info Viewer")
    root.iconbitmap('pokeball.ico')

#create the frames
    frm_input = ttk.Frame(root)
    frm_input.grid(row=1, column=1, columnspan=2)

    frm_stats = ttk.LabelFrame(root, text="Stats")
    frm_stats.grid(row=2, column=2)

    frm_info = ttk.LabelFrame(root, text="Stats")
    frm_info.grid(row=2, column=1, padx=10, pady=10)

#populate user input frame
    lbl_name = ttk.Label(frm_input, text="Pokemon Name:")
    lbl_name.grid(row=1, column=1, padx=10, pady=10)

    ent_name = ttk.Entry(frm_input)
    ent_name.grid(row=1, column=2)

    btn_get_info = ttk.Button(frm_input, text='Get Info')
    btn_get_info.grid(row=1, column=3, padx=10, pady=10)

#populate pokemon info frame
    lbl_height = ttk.Label(frm_info, text="Height:")
    lbl_height.grid(row=1, column=1, padx=10, pady=10)
    lbl_height_val = ttk.Label(frm_info, text='TBD')
    lbl_height_val.grid(row=1, column=2)

    lbl_weight = ttk.Label(frm_info, text='Weight:')
    lbl_weight.grid(row=2, column=1, padx=10, pady=10)
    lbl_weight_val = ttk.Label(frm_info, text="TBD")
    lbl_weight_val.grid(row=2, column=2)

    lbl_type = ttk.Label(frm_info, text='Type:')
    lbl_type.grid(row=3, column=1, padx=10, pady=10)
    lbl_weight_val = ttk.Label(frm_info, text="TBD")
    lbl_weight_val.grid(row=3, column=2)
    








    root.mainloop()   





main()